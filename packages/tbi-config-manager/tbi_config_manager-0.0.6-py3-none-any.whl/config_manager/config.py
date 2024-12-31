# Configuration manager that orchestrates multiple providers to retrieve config values
from enum import Enum
from typing import Any, List, Optional, TypeVar, Union, overload, Dict
from pathlib import Path

from .providers.factory import ProviderFactory
from .providers.composite import CompositeProvider
from .typing import ConfigValue, PathLike, Provider
from .exceptions import ConfigError, ConfigNotFoundError
from .utils.logger import setup_logger
from .utils.cache import cached_property

logger = setup_logger()
T = TypeVar("T")


class ConfigManager:
    _instance: Optional["ConfigManager"] = None
    _instances: Dict[str, "ConfigManager"] = {}
    _configs: Dict[str, Dict[str, Any]] = {}  # 存儲每個實例的配置

    def __new__(
        cls,
        providers: Optional[List[Provider]] = None,
        env_file: Optional[PathLike] = None,
        project_id: Optional[str] = None,
        credentials_path: Optional[str] = None,
        secret_prefix: str = "",
        cache_enabled: bool = True,
        instance_name: str = "default",
    ) -> "ConfigManager":
        """
        Singleton pattern implementation with support for named instances.

        Args:
            instance_name: Name of the configuration instance. Useful when you need
                         multiple configurations in the same application.
        """
        if instance_name not in cls._instances:
            instance = super().__new__(cls)
            instance._initialized = False
            cls._instances[instance_name] = instance
            # 存儲配置
            cls._configs[instance_name] = {
                "providers": providers or [Provider.ENV],
                "env_file": env_file,
                "project_id": project_id,
                "credentials_path": credentials_path,
                "secret_prefix": secret_prefix,
                "cache_enabled": cache_enabled,
            }
        else:
            # 檢查參數一致性
            stored_config = cls._configs[instance_name]
            new_config = {
                "providers": providers or [Provider.ENV],
                "env_file": env_file,
                "project_id": project_id,
                "credentials_path": credentials_path,
                "secret_prefix": secret_prefix,
                "cache_enabled": cache_enabled,
            }
            if stored_config != new_config:
                logger.warning(
                    f"Attempting to create singleton instance '{instance_name}' with "
                    f"different parameters. Using existing instance with original parameters."
                )
        return cls._instances[instance_name]

    def __init__(
        self,
        providers: Optional[List[Provider]] = None,
        env_file: Optional[PathLike] = None,
        project_id: Optional[str] = None,
        credentials_path: Optional[str] = None,
        secret_prefix: str = "",
        cache_enabled: bool = True,
        instance_name: str = "default",
    ):
        """
        Args:
            providers: List of provider types to use for configuration
            env_file: Path to .env file
            project_id: GCP project ID (only if GCP in providers)
            credentials_path: GCP credentials path
            secret_prefix: Secret prefix for GCP
            cache_enabled: Enable caching
            instance_name: Name of the configuration instance
        """
        # Skip initialization if already initialized
        if getattr(self, "_initialized", False):
            return

        config = self._configs[instance_name]
        self.cache_enabled = config["cache_enabled"]
        self._setup_providers(
            config["providers"],
            config["env_file"],
            config["project_id"],
            config["credentials_path"],
            config["secret_prefix"],
        )
        self._initialized = True

    @classmethod
    def get_instance(
        cls, instance_name: str = "default", create_if_missing: bool = False
    ) -> "ConfigManager":
        """
        Get a named configuration instance.

        Args:
            instance_name: Name of the configuration instance
            create_if_missing: If True, create a new instance with default settings
                             when the requested instance doesn't exist

        Returns:
            The ConfigManager instance

        Raises:
            ConfigError: If instance doesn't exist and create_if_missing is False
        """
        if instance_name not in cls._instances:
            if create_if_missing:
                return cls(instance_name=instance_name)
            raise ConfigError(f"Configuration instance '{instance_name}' not found")
        return cls._instances[instance_name]

    @classmethod
    def reset_instance(cls, instance_name: str = "default") -> None:
        """
        Reset a named configuration instance.

        Args:
            instance_name: Name of the configuration instance to reset
        """
        if instance_name in cls._instances:
            del cls._instances[instance_name]
            del cls._configs[instance_name]

    def _setup_providers(
        self,
        providers: List[Provider],
        env_file: Optional[PathLike],
        project_id: Optional[str],
        credentials_path: Optional[str],
        secret_prefix: str,
    ) -> None:
        """Setup configuration providers"""
        provider_instances = []

        kwargs = {
            "env_file": env_file,
            "project_id": project_id,
            "credentials_path": credentials_path,
            "secret_prefix": secret_prefix,
        }

        for provider_type in providers:
            provider = ProviderFactory.create(provider_type, **kwargs)
            if provider:
                provider_instances.append(provider)

        if not provider_instances:
            raise ConfigError("No configuration providers available")

        self.provider = CompositeProvider(provider_instances)

    @overload
    def get(self, key: str) -> Optional[ConfigValue]: ...

    @overload
    def get(self, key: str, default: T) -> Union[ConfigValue, T]: ...

    def get(self, key: str, default: Any = None) -> Union[ConfigValue, Any]:
        """
        Get configuration value

        Args:
            key: Configuration key
            default: Default value

        Returns:
            Configuration value
        """
        try:
            # Get value from providers in order until a non-None value is found
            if isinstance(self.provider, CompositeProvider):
                for provider in self.provider.providers:
                    value = provider.get(key)
                    if value is not None:
                        return value
            return default
        except Exception as e:
            logger.error(f"Error getting config {key}: {e}")
            return default

    def __getattr__(self, name: str) -> Any:
        """Support accessing configuration as attributes"""
        return self.get(name)

    def require(self, key: str) -> ConfigValue:
        """
        Get required configuration value; raise exception if not found

        Args:
            key: Configuration key

        Returns:
            Configuration value

        Raises:
            ConfigNotFoundError: If configuration not found
        """
        value = self.get(key)
        if value is None:
            raise ConfigNotFoundError(f"Required config {key} not found")
        return value

    def reload(self) -> None:
        """Reload configurations from all providers"""
        if isinstance(self.provider, CompositeProvider):
            for provider in self.provider.providers:
                try:
                    provider.reload()
                except Exception as e:
                    logger.error(f"Failed to reload provider {provider.name}: {e}")
