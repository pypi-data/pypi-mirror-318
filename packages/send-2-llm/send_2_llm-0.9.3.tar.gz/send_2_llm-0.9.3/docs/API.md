# API Documentation

## CLI Interface

### Basic Usage

```bash
# Single request
send2llm "Your text"

# Interactive mode
send2llm interactive

# Show configuration
send2llm config

# Manage logs
send2llm logs
```

### Command Options

#### Send Command
```bash
send2llm [TEXT] [OPTIONS]

Options:
  --format, -f     Output format (raw/text/markdown/telegram_markdown/html)
  --json, -j       Return response in JSON format
  --provider, -p   Provider to use (default from .env)
  --model, -m      Model to use (default from .env)
  --debug, -d      Show debug output
```

#### Interactive Command
```bash
send2llm interactive [OPTIONS]

Options:
  --debug, -d      Show debug output
```

#### Config Command
```bash
send2llm config [OPTIONS]

Options:
  --debug, -d      Show debug output (includes API keys)
```

#### Logs Command
```bash
send2llm logs [OPTIONS]

Options:
  --action, -a     Action to perform (status/rotate/cleanup/analyze)
  --days, -d       Number of days for analysis/cleanup
  --max-size, -s   Maximum log file size in MB
  --max-backups, -b Maximum number of backup files
  --debug          Show debug output
```

## Python API

### Basic Usage

```python
from send_2_llm import send_2_llm
from send_2_llm.types import OutputFormat, ProviderType

# Simple request
response = await send_2_llm("Your text")

# With options
response = await send_2_llm(
    "Your text",
    output_format=OutputFormat.MARKDOWN,
    return_json=True,
    provider_type=ProviderType.OPENAI,
    model="gpt-4"
)
```

### Response Type

```python
class LLMResponse:
    text: str                # Response text
    metadata: ResponseMetadata  # Response metadata
    error_details: Optional[ErrorDetails]  # Error details if any

class ResponseMetadata:
    provider: ProviderType   # Provider used
    model: str              # Model used
    created_at: datetime    # Response timestamp
    usage: TokenUsage       # Token usage info
    latency: float         # Response time in seconds

class TokenUsage:
    prompt_tokens: int     # Input tokens count
    completion_tokens: int # Output tokens count
    total_tokens: int     # Total tokens used
    cost: float          # Request cost in USD
```

### Error Handling

```python
from send_2_llm.types import LLMError, ErrorDetails

try:
    response = await send_2_llm("Your text")
except LLMError as e:
    error_details: ErrorDetails = e.details
    print(f"Error: {error_details.message}")
    print(f"Type: {error_details.error_type}")
    print(f"Context: {error_details.context}")
```

### Providers

#### OpenAI
```python
from send_2_llm.providers import OpenAIProvider

provider = OpenAIProvider(
    api_key="your_api_key",
    model="gpt-4",
    temperature=0.7,
    max_tokens=1000
)
```

#### Perplexity
```python
from send_2_llm.providers import PerplexityProvider

provider = PerplexityProvider(
    api_key="your_api_key",
    model="sonar-medium-online",
    web_search=True
)
```

#### Anthropic
```python
from send_2_llm.providers import AnthropicProvider

provider = AnthropicProvider(
    api_key="your_api_key",
    model="claude-2",
    max_tokens=1000
)
```

### Strategies

#### Basic Strategy
```python
from send_2_llm.strategies import BasicStrategy

strategy = BasicStrategy(provider=provider)
response = await strategy.execute("Your text")
```

#### Retry Strategy
```python
from send_2_llm.strategies import RetryStrategy

strategy = RetryStrategy(
    provider=provider,
    max_retries=3,
    delay=1.0,
    exponential=True
)
```

#### Fallback Strategy
```python
from send_2_llm.strategies import FallbackStrategy

strategy = FallbackStrategy(
    providers=[openai_provider, anthropic_provider],
    fallback_on_errors=True
)
```

#### Chain Strategy
```python
from send_2_llm.strategies import ChainStrategy

strategy = ChainStrategy(
    providers=[provider1, provider2],
    aggregation="concat"  # or "best" or custom function
)
```

### Configuration

```python
from send_2_llm.config import Config

# Load config
config = Config.load()

# Get provider config
openai_config = config.get_provider_config("openai")
print(f"Model: {openai_config.model}")
print(f"Price: ${openai_config.price_per_1k_tokens}")

# Get system prompts
system_prompt = config.get_system_prompt("default")
```

### Logging

```python
from send_2_llm.cli.utils.logging import setup_logging
from send_2_llm.cli.utils.log_rotation import rotate_logs
from send_2_llm.cli.utils.log_analysis import analyze_requests

# Setup logging
setup_logging(debug=True)

# Rotate logs
rotate_logs(max_size_mb=10, max_backups=5)

# Analyze usage
stats = analyze_requests(days=7)
print(f"Total requests: {stats['total_requests']}")
``` 