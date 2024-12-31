# Configuration manager that orchestrates multiple providers to retrieve config values
from enum import Enum
from typing import Any, List, Optional, TypeVar, Union, overload, Dict
from pathlib import Path
import hashlib
import json

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
    _configs: Dict[str, Dict[str, Any]] = {}  # Store configurations for each instance

    @staticmethod
    def _generate_instance_name(config: Dict[str, Any]) -> str:
        """
        Generate a unique instance name based on configuration parameters.

        Args:
            config: Configuration parameter dictionary

        Returns:
            A unique instance name based on configuration parameters
        """
        # Create a serializable copy of the configuration
        serializable_config = {}
        for k, v in sorted(config.items()):
            if v is None:
                continue
            if isinstance(v, list) and v and isinstance(v[0], Provider):
                # Convert Provider enum list to list of names
                serializable_config[k] = sorted(p.name for p in v)
            elif isinstance(v, Path):
                # Convert Path to string
                serializable_config[k] = str(v)
            else:
                serializable_config[k] = v

        # Convert configuration to string and calculate hash
        config_str = json.dumps(serializable_config, sort_keys=True)
        return hashlib.md5(config_str.encode()).hexdigest()[:8]

    def __new__(
        cls,
        providers: Optional[List[Provider]] = None,
        env_file: Optional[PathLike] = None,
        project_id: Optional[str] = None,
        credentials_path: Optional[str] = None,
        secret_prefix: str = "",
        cache_enabled: bool = True,
        instance_name: Optional[str] = None,
    ) -> "ConfigManager":
        """
        Singleton pattern implementation with support for named instances.

        Args:
            instance_name: Optional name for the configuration instance.
                         If not provided, a unique name will be generated based on the configuration.
        """
        # Prepare configuration
        config = {
            "providers": providers or [Provider.ENV],
            "env_file": env_file,
            "project_id": project_id,
            "credentials_path": credentials_path,
            "secret_prefix": secret_prefix,
            "cache_enabled": cache_enabled,
        }

        # Generate instance name from configuration if not provided
        if instance_name is None:
            instance_name = cls._generate_instance_name(config)

        if instance_name not in cls._instances:
            instance = super().__new__(cls)
            instance._initialized = False
            cls._instances[instance_name] = instance
            cls._configs[instance_name] = config
        else:
            # Check parameter consistency
            stored_config = cls._configs[instance_name]
            if stored_config != config:
                if instance_name == "default":
                    # For default instance name, generate a new instance name
                    new_instance_name = cls._generate_instance_name(config)
                    logger.info(
                        f"Creating new instance '{new_instance_name}' with different parameters"
                    )
                    instance = super().__new__(cls)
                    instance._initialized = False
                    cls._instances[new_instance_name] = instance
                    cls._configs[new_instance_name] = config
                    return cls._instances[new_instance_name]
                else:
                    # For custom instance names, maintain original behavior
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
        instance_name: Optional[str] = None,
    ):
        """
        Args:
            providers: List of provider types to use for configuration
            env_file: Path to .env file
            project_id: GCP project ID (only if GCP in providers)
            credentials_path: GCP credentials path
            secret_prefix: Secret prefix for GCP
            cache_enabled: Enable caching
            instance_name: Optional name for the configuration instance
        """
        # Skip initialization if already initialized
        if getattr(self, "_initialized", False):
            return

        # Find configuration for current instance
        instance_name = next(
            name for name, instance in self._instances.items() if instance is self
        )
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
