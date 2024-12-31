# GCP Secret Manager provider for accessing and managing configuration secrets in Google Cloud Platform
from typing import Optional
from google.cloud import secretmanager
from google.oauth2 import service_account
from google.api_core import exceptions
from pathlib import Path

from .base import ConfigProvider
from ..typing import ConfigValue
from ..exceptions import ProviderError


class GCPProvider(ConfigProvider):
    """GCP Secret Manager configuration provider"""

    def __init__(
        self,
        project_id: str,
        credentials_path: Optional[str] = None,
        secret_prefix: str = "",
    ):
        """
        Initialize GCP Secret Manager provider

        Args:
            project_id: GCP project ID
            credentials_path: Path to service account credentials JSON file (absolute or relative path)
            secret_prefix: Prefix for secret names (underscore will be automatically added if missing)
        """
        self.project_id = project_id
        self.credentials_path = credentials_path
        # Add underscore to prefix if it doesn't end with one and isn't empty
        self.secret_prefix = (
            f"{secret_prefix}_"
            if secret_prefix and not secret_prefix.endswith("_")
            else secret_prefix
        )

        try:
            if credentials_path:
                # Resolve to absolute path
                resolved_path = Path(credentials_path).resolve()
                if resolved_path.exists():
                    credentials = service_account.Credentials.from_service_account_file(
                        str(resolved_path)
                    )
                    self.client = secretmanager.SecretManagerServiceClient(
                        credentials=credentials
                    )
                else:
                    print(
                        f"Warning: Credentials file not found at {resolved_path}, falling back to default credentials"
                    )
                    self.client = secretmanager.SecretManagerServiceClient()
            else:
                self.client = secretmanager.SecretManagerServiceClient()
        except Exception as e:
            raise ProviderError(f"Failed to initialize GCP Secret Manager: {e}")

    def reload(self) -> None:
        """Reload the configuration"""
        self.__init__(self.project_id, self.credentials_path, self.secret_prefix)

    def get(self, key: str) -> Optional[ConfigValue]:
        try:
            # Handle prefix logic
            if self.secret_prefix and key.startswith(self.secret_prefix):
                secret_id = key  # Prefix already present, use as is
            else:
                secret_id = f"{self.secret_prefix}{key}"  # Add prefix

            name = f"projects/{self.project_id}/secrets/{secret_id}/versions/latest"
            response = self.client.access_secret_version(request={"name": name})
            return response.payload.data.decode("UTF-8")
        except exceptions.NotFound:
            return None
        except Exception as e:
            raise ProviderError(f"Error accessing secret {key}: {e}")

    def has(self, key: str) -> bool:
        try:
            secret_id = f"{self.secret_prefix}{key}"
            name = f"projects/{self.project_id}/secrets/{secret_id}"
            self.client.get_secret(request={"name": name})
            return True
        except Exception:
            return False

    @property
    def name(self) -> str:
        """Provider name"""
        return "GCP Secret Manager"
