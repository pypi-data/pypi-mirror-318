# Config Manager

### tbi-config-manager (0.0.7)
A flexible configuration management library for Python with multiple provider support (Environment, GCP Secret Manager, etc.) and easy extensibility.


# Features

- **Multiple Provider Support**
  - Built-in Environment Variables (.env) support
  - Built-in GCP Secret Manager integration
  - Configurable provider priority
  - Easy to extend with custom providers

- **Type Safety & Flexibility**
  - Strong typing support
  - Optional value handling
  - Default value support
  - Attribute-style access

- **Developer Friendly**
  - Simple API
  - Clear error messages
  - Comprehensive logging
  - Easy to test


# Installation

```bash
$ pip install tbi-config-manager
```
### Prerequisites
- Python >=3.8
- GCP credentials (optional, GCP project Service Account, for Secret Manager support)


# How to Use

Basic usage example:
```python
from config_manager import ConfigManager, Provider

# Default to environment variables only
config = ConfigManager()
value = config.get("DATABASE_URL")

# With specific .env file
config = ConfigManager(env_file=".env.dev")

# ENV has higher priority than GCP.
config = ConfigManager(
    providers=[Provider.ENV, Provider.GCP],  
    project_id="your-project-id",
    credentials_path="path/to/credentials.json",
    secret_prefix="APP"                                  # Will use "APP_" as prefix
)

# GCP has higher priority than ENV.
config = ConfigManager(
    providers=[Provider.GCP, Provider.ENV]  
    ...
)

# Only use GCP Secret Manager
config = ConfigManager(
    providers=[Provider.GCP]  
    ...
)

DATABASE_URL = config.get("DATABASE_URL")
...
```

In your `config.py`:
```python
from config_manager import ConfigManager, Provider

config = ConfigManager(
    providers=[Provider.ENV, Provider.GCP],  
    project_id="config-manager",
    credentials_path="path/to/credentials.json",
    secret_prefix="PROD"                                 # Will use "PROD_" as prefix
)

# Access configs as attributes
DATABASE_URL = config.get("DATABASE_URL")
API_KEY = config.get("API_KEY")
ENV = config.get("ENV", default="dev")
PROVIDER = config.get("PROVIDER", "GCP") # Optional parameter with default
```


# How to Contribute

## Setup
```bash
git clone https://github.com/TaiwanBigdata/config-manager.git
cd readgen
python -m venv env
source env/bin/activate  # Linux/Mac
pip install -e .
```

## Implementing Custom Providers

The config-manager library is designed for extensibility. Here's how to implement your own configuration provider:

### 1. Add New Provider Type
Add your provider type to the enum
`src/config_manager/typing.py`
```python
from enum import Enum

class Provider(Enum):
    """Available configuration provider types"""
    ENV = "env"      # Environment variables
    GCP = "gcp"      # Google Cloud Secret Manager
    REDIS = "redis"  # Your new provider
```

### 2. Implement Provider Class
Create your provider implementation under providers directory 
`src/config_manager/providers/redis.py`

```python
from config_manager import ConfigProvider
from typing import Optional

# Inherit from the base abstract class ConfigProvider
class RedisProvider(ConfigProvider):
    def __init__(self, redis_url: str, prefix: str = ""):
        self.redis_url = redis_url
        self.prefix = prefix
        self._client = redis.Redis.from_url(redis_url)
    
    # Required interface implementations
    def get(self, key: str) -> Optional[str]: ...
    def has(self, key: str) -> bool: ...
    def reload(self) -> None: ...
    @property
    def name(self) -> str: ...
```
### 3. Register Provider
Register your provider in factory
`src/config_manager/providers/factory.py`

```python
class ProviderFactory:
    ...

# Register providers here
ProviderFactory.register(Provider.ENV, EnvProvider)
ProviderFactory.register(Provider.GCP, GCPProvider)
```

### 4. Export Provider

Export your provider in the module level
`src/config_manager/providers/__init__.py`
```python
from .redis import RedisProvider

__all__ = [
    ...
    "RedisProvider",
]
```

Export your provider in the package level
`src/config_manager/__init__.py`
```python
from .providers import ProviderFactory, EnvProvider, GCPProvider, RedisProvider

__all__ = [
    ...
    "RedisProvider",
]
```


### Examples of Potential Custom Providers
- AWS Secrets Manager
- Azure Key Vault
- HashiCorp Vault
- Redis
- MongoDB
- Local JSON/YAML files
- Remote HTTP endpoints

### Each provider needs to implement the ConfigProvider interface and handle:

- Configuration retrieval
- Key existence checking
- Reloading mechanism
- Error handling


# Dependencies

### Core
- python-dotenv>=1.0.0
- google-cloud-secret-manager>=2.0.0
- typing-extensions>=4.0.0


# License

This project is licensed under the MIT License.


# Project Structure

```
config-manager/
├── src/
│   └── config_manager/       # Register providers at the project level
│       ├── providers/        # Register providers at the model level
│       │   ├── base.py       # Abstract base class for configuration providers
│       │   ├── composite.py  # Implements composite pattern to aggregate multiple config providers in priority order
│       │   ├── env.py        # Local environment configuration for the `.env` provider
│       │   ├── factory.py    # Register and initialize providers in this file
│       │   └── gcp.py        # GCP Secret Manager provider for accessing and managing configuration secrets in Google Cloud Platform
│       ├── utils/
│       │   ├── cache.py
│       │   └── logger.py
│       ├── config.py         # Configuration manager that orchestrates multiple providers to retrieve config values
│       ├── exceptions.py
│       └── typing.py         # Type definitions and enums
├── LICENSE
├── pyproject.toml
├── readgen.toml              # ReadGen - Readme Generator CLI tool configuration file
├── README.md
└── requirements.txt
```


---
> This document was automatically generated by [ReadGen](https://github.com/TaiwanBigdata/readgen).
