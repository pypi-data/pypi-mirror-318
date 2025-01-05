# Configuration System

## Overview

The configuration system in send_2_llm is designed to provide a flexible, maintainable, and type-safe way to manage various settings across the application. It uses YAML files for configuration storage and Pydantic models for validation.

## Structure

The configuration is split into several specialized YAML files:

```
src/send_2_llm/constants/
├── model_pricing.yaml     # Model prices and token limits
├── provider_features.yaml # Provider and model capabilities
├── system_prompts.yaml   # System prompts for different tasks
└── defaults.yaml         # Default settings and parameters
```

### Model Pricing (`model_pricing.yaml`)

Contains pricing information and token limits for all models across different providers and sources:

```yaml
providers:
  direct:  # Direct API access
    openai:
      models:
        gpt-4o:
          prices:
            prompt: 2.50      # USD per million tokens
            completion: 10.00
          limits:
            max_total_tokens: 128000

  together:  # Through Together.ai
    deepseek:
      models:
        deepseek-chat:
          prices:
            prompt: 0.30      # Different pricing
            completion: 1.20
```

### Provider Features (`provider_features.yaml`)

Defines capabilities and features of each model:

```yaml
providers:
  direct:
    openai:
      models:
        gpt-4o:
          features:
            streaming: true
            function_calling: true
            vision: true

# Also includes model aliases for cross-provider mapping
model_aliases:
  "deepseek-chat":
    direct: "deepseek/deepseek-chat"
    together: "together/deepseek-chat"
```

### System Prompts (`system_prompts.yaml`)

Contains predefined system prompts for different tasks:

```yaml
system_prompts:
  general: "You are a helpful AI assistant..."
  code: "You are a code assistant..."
  math: "You are a math assistant..."
```

### Defaults (`defaults.yaml`)

Default settings for various aspects of the system:

```yaml
rate_limits:
  rpm: 10
  daily_quota: 1000

generation_defaults:
  temperature: 0.7
  top_p: 0.95

retry_policy:
  max_retries: 3
  initial_delay: 1.0
```

## Usage

### Basic Usage

```python
from send_2_llm.constants import config_manager

# Get model pricing
price = config_manager.get_model_price("openai", "direct", "gpt-4o")
print(f"Prompt price: ${price.prompt} per million tokens")

# Check model features
features = config_manager.get_model_features("openai", "gpt-4o")
if features['streaming']:
    # Use streaming...

# Get system prompt
prompt = config_manager.get_system_prompt("code")

# Get default configuration
rpm = config_manager.get_default_config("rate_limits.rpm")
```

### Type Safety

The configuration system uses Pydantic models for validation:

```python
class PriceConfig(BaseModel):
    prompt: float
    completion: float
    prompt_cache_hit: Optional[float] = None
    prompt_cache_write: Optional[float] = None
    prompt_cache_read: Optional[float] = None
```

### Error Handling

All configuration access methods include proper error handling:

```python
try:
    price = config_manager.get_model_price("unknown", "direct", "model")
except ValueError as e:
    print(f"Configuration error: {e}")
```

## Multi-Provider Support

The system supports different pricing and features for the same model through different providers:

1. Direct API access
2. Together.ai as a provider
3. Perplexity as a provider

This allows for:
- Price comparison between providers
- Feature availability checking
- Automatic fallback options

## Updating Configurations

Configurations can be reloaded at runtime:

```python
config_manager.reload_configs()
```

## Best Practices

1. Always use the global `config_manager` instance:
   ```python
   from send_2_llm.constants import config_manager
   ```

2. Use type hints with configuration objects:
   ```python
   from send_2_llm.constants import PriceConfig
   
   def calculate_cost(price: PriceConfig, tokens: int) -> float:
       return (price.prompt * tokens) / 1_000_000
   ```

3. Handle configuration errors appropriately:
   ```python
   try:
       features = config_manager.get_model_features(provider, model)
   except ValueError:
       features = {"streaming": False, "function_calling": False}
   ```

4. Use model aliases for cross-provider compatibility:
   ```yaml
   model_aliases:
     "deepseek-chat":
       direct: "deepseek/deepseek-chat"
       together: "together/deepseek-chat"
   ```

## Security Considerations

1. Configuration files are read-only during runtime
2. No sensitive information (API keys, etc.) should be stored in these files
3. Use environment variables for sensitive data

## Extending the System

To add new configuration types:

1. Create a new YAML file in the constants directory
2. Add the file to `config_files` in `ConfigManager`
3. Create appropriate Pydantic models
4. Add access methods to `ConfigManager`

Example:
```python
def get_custom_config(self, key: str) -> CustomConfig:
    try:
        config = self.configs['custom'][key]
        return CustomConfig(**config)
    except KeyError:
        raise ValueError(f"No custom config found for: {key}")
``` 