# Project Progress

## Latest Updates
- 2024-04-07: [RELEASE] Preparing PyPI Release 0.9.0
  - Created pyproject.toml for modern build configuration
  - Updated package metadata and classifiers
  - Created MANIFEST.in for package contents
  - Updated all dependencies to latest versions
  - Changed project status to Beta
  - Added comprehensive package documentation

- 2024-04-07: [RELEASE] Preparing Release Candidate 0.9.0
  - Updated version in setup.py to 0.9.0
  - Updated all dependencies to latest stable versions
  - Moved Unreleased changes to 0.9.0 in CHANGELOG.md
  - Preparing for pip package release

- 2024-04-07: [CLEANUP] Removed Legacy Gemini SDK
  - Removed google-generativeai package
  - Deleted old Gemini provider implementation
  - Renamed GeminiNewProvider to GeminiProvider
  - Updated factory.py imports
  - Cleaned up requirements.txt
  - No breaking changes to functionality

- 2024-04-07: [FEATURE] Updated Gemini Provider
  - Migrated to new google-genai SDK
  - Added support for new Gemini features:
    - Improved system instructions
    - Better configuration options
    - Enhanced type safety
  - Legacy provider preserved for backward compatibility
  - Updated requirements.txt with new dependencies

- 2024-04-07: [FEATURE] Enhanced Virtual Environment Management
  - Added automated venv management system:
    - Created check_venv.sh for automatic venv checks
    - Added protection rules in .cursorrules
    - All scripts now include venv verification
    - Protected check_venv.sh from modifications
  - Enhanced example scripts:
    - Added run_haiku.sh with venv check
    - Added run_chat.sh with venv check
    - All Python scripts now run in verified venv

- 2024-04-07: [FEATURE] Enhanced Chat UI
  - Added rich modern terminal UI to random_provider_chat.py:
    - Beautiful panels for messages
    - Real-time statistics tracking
    - Color-coded provider information
    - Progress spinners for generation
    - Session duration tracking
    - Improved error display
  - Code improvements:
    - Removed code duplication (DRY)
    - Added ChatUI class for UI management
    - Better type hints
    - Improved error handling
    - Enhanced user feedback

## Environment Setup and Management
- [x] Virtual Environment Management
  - [x] Python 3.11+ requirement
  - [x] Automated venv creation and activation script (check_venv.sh)
  - [x] Environment variable protection
  - [x] Dependency management
  - [x] Version control integration

## Phase 1: Core Infrastructure and OpenAI Integration
- [x] Setup basic project structure
- [x] Implement base provider interface
- [x] Add provider types and enums
- [x] Implement OpenAI provider
- [x] Add OpenAI provider tests
- [x] Setup provider initialization structure
- [x] Configure environment variables
- [x] Move trading module to src structure
- [x] Create automated test script with venv and coverage support
- [x] Set default provider from environment variables (with OpenAI fallback)

## Phase 2: Additional Providers and Strategies
- [x] Implement Anthropic provider
  - [x] Basic Claude 3 integration
    - [x] Support for claude-3-haiku-20240307 (default)
    - [x] Support for claude-3-5-sonnet-latest
    - [x] Support for claude-3-5-haiku-latest
  - [ ] Multi-modal support
  - [x] Comprehensive test coverage
    - [x] Basic provider tests
    - [x] Error handling tests
    - [x] Token usage tracking
    - [x] Fallback strategy tests
    - [x] Russian haiku generation tests
    - [ ] Streaming tests
    - [ ] Multi-language support tests
    - [ ] Context handling tests
    - [ ] Model-specific tests
- [x] Together AI Integration [STABLE: stable_together_v1]
  - [x] Simple Together AI integration via OpenAI SDK
  - [x] Support for Mixtral and Llama models
  - [x] Basic test coverage
  - [x] Example usage
  - [x] Multi-turn conversation tests
  - [x] Temperature and system prompt tests
  - [x] Update default model to meta-llama/Llama-Vision-Free
  - [ ] Add cost calculation
  - [ ] Add streaming support
  - [ ] Add comprehensive tests
- [x] Implement DeepSeek provider [STABLE: stable_deepseek_v1]
  - [x] Chat model integration
  - [ ] Code model integration
  - [x] Basic test coverage
  - [ ] Advanced features
    - [ ] Streaming support
    - [ ] Cost calculation
    - [ ] Multi-turn conversations
    - [ ] System prompts
- [ ] Implement Google Gemini
  - [x] Basic Gemini Pro integration
    - [x] Chat model support
    - [x] Temperature and top_p control
    - [x] Token usage estimation
  - [ ] Multi-modal support
  - [x] Basic test coverage
    - [x] Provider initialization tests
    - [x] Error handling tests
    - [x] Generation tests
  - [ ] Advanced features
    - [ ] Streaming support
    - [ ] Cost calculation
    - [ ] Multi-turn conversations
    - [ ] System prompts
  - [ ] Comprehensive testing
    - [ ] Integration tests
    - [ ] Strategy tests
    - [ ] Performance tests
- [ ] Implement OpenRouter
  - [ ] Multi-provider support
  - [ ] Cost optimization
  - [ ] Automatic fallback
  - [ ] Test coverage
- [ ] Implement Perplexity
  - [x] Online models integration
  - [x] Chat models integration
  - [x] Web search integration
    - [x] Basic search functionality
    - [x] Citation support
    - [x] Academic-style citation formatting
    - [x] Domain filtering support (with limitations)
  - [ ] RAG support
  - [x] Basic test coverage
    - [x] Provider initialization tests
    - [x] Web search tests
    - [x] Citation extraction tests
    - [x] Domain filtering tests
    - [x] Error handling tests
  - [x] Advanced features
    - [x] Related questions support
    - [ ] Image support
    - [x] Search recency filter
    - [ ] Streaming support
  - [ ] Examples
    - [x] Web search with citations
    - [x] Domain-filtered search
    - [ ] Multi-modal search
    - [ ] RAG examples
  - [x] API Integration
    - [x] Client integration
    - [x] Strategy support
    - [x] Fallback support

## Phase 3: Advanced Strategies (In Progress)
- [x] Implement single provider strategy
- [x] Implement fallback strategy
- [x] Add strategy switching via environment variables
- [ ] High-level Integration Testing
  - [x] Provider switching tests
  - [x] Error propagation tests
  - [x] Token usage tracking across providers
  - [x] CLI tests fixed (asyncio event loop issue resolved)
  - [ ] Multi-provider strategy tests
  - [ ] Performance benchmarking tests
  - [ ] System-wide error handling
  - [ ] Recovery strategy tests
  - [ ] Test Simplification (In Progress)
    - [ ] Reduce dependency on environment variables
    - [ ] Simplify configuration caching logic
    - [ ] Improve test isolation
    - [ ] Reduce mock complexity
    - [ ] Add more focused unit tests
    - [ ] Separate integration tests
    - [ ] Improve test documentation
- [ ] Implement parallel strategy
- [ ] Implement cost-optimized strategy
  - [ ] Cost tracking
  - [ ] Budget limits
  - [ ] Provider selection based on cost
- [ ] Add RAG strategy
  - [ ] Web search integration (Perplexity)
  - [ ] Document retrieval
  - [ ] Context optimization
- [ ] Add strategy tests

## Phase 4: Advanced Features (Pending)
- [x] Add comprehensive logging system
  - [x] Structured logging implementation
  - [x] Log rotation and archiving
  - [x] Log level configuration
  - [x] Performance logging
  - [x] Security event logging
  - [x] API request/response logging
- [ ] Implement metrics collection system
  - [x] Provider performance metrics
  - [x] Response time tracking
  - [x] Token usage analytics
  - [ ] Cost metrics
  - [ ] Error rate monitoring
  - [ ] Strategy effectiveness metrics
- [ ] Add caching system
- [ ] Implement rate limiting
- [ ] Add multi-modal support
  - [ ] Image analysis (Claude 3, Gemini)
  - [ ] Code understanding (DeepSeek)
  - [ ] Custom data formats
  - [ ] Web search (Perplexity)

## Phase 5: Documentation and Examples (In Progress)
- [x] Write strategy configuration documentation
- [x] Add strategy usage examples
- [x] Document supported and planned providers
- [x] Write API documentation
- [x] Create integration guides
- [x] Create contribution guidelines

## Output Format Implementation Plan

### Phase 1: Core Output Format Support
- [x] Define OutputFormat enum in types.py
  - [x] Add RAW format (unmodified output)
  - [x] Add TXT format (plain text)
  - [x] Add JSON format (structured data)
  - [x] Add TELEGRAM_MARKDOWN format
  - [x] Add format validation
  - [x] Add format conversion utilities

### Phase 2: Provider Integration
- [x] Update base provider interface
  - [x] Add output_format parameter
  - [x] Add format conversion methods
  - [x] Add format validation
  - [x] Update provider documentation
- [x] Implement in OpenAI provider
  - [x] Add format support
  - [x] Add tests
  - [x] Update examples
- [x] Implement in Anthropic provider
  - [x] Add format support
  - [x] Add tests
  - [x] Update examples
- [x] Implement in other providers
  - [x] Together AI
  - [x] DeepSeek
  - [x] Gemini
  - [x] Perplexity

### Phase 3: Format-Specific Features
- [x] RAW Format
  - [x] Direct provider output
  - [x] No processing or modification
  - [x] Performance optimization
- [x] TXT Format
  - [x] Clean text output
  - [x] Whitespace normalization
  - [x] Line ending standardization
- [x] JSON Format
  - [x] Schema definition
  - [x] Type validation
  - [x] Error handling
  - [x] Pretty printing option
- [x] TELEGRAM_MARKDOWN Format
  - [x] Telegram-specific syntax
  - [x] Entity escaping
  - [x] Link handling
  - [x] Code block formatting

### Phase 4: Testing & Validation
- [x] Unit Tests
  - [x] Format conversion tests
  - [x] Validation tests
  - [x] Error handling tests
- [x] Integration Tests
  - [x] Provider-specific tests
  - [x] Cross-provider tests
  - [x] Format compatibility tests
- [x] Performance Tests
  - [x] Format conversion benchmarks
  - [x] Memory usage tests
  - [x] Response time tests

### Phase 5: Documentation & Examples
- [x] API Documentation
  - [x] Format specification
  - [x] Usage guidelines
  - [x] Best practices
- [x] Example Scripts
  - [x] Basic format examples
  - [x] Provider-specific examples
  - [x] Complex use cases
- [x] Migration Guide
  - [x] Upgrading from old format
  - [x] Breaking changes
  - [x] Compatibility notes

### Phase 6: Quality Assurance
- [x] Code Review
  - [x] Performance review
  - [x] Security review
  - [x] API design review
- [x] Testing Coverage
  - [x] 95%+ coverage target
  - [x] Edge case testing
  - [x] Error scenario testing
- [x] Documentation Review
  - [x] Technical accuracy
  - [x] Completeness
  - [x] User-friendliness

## Latest Updates
- 2024-04-07: [BUGFIX] Fixed metrics module import
  - Added missing asyncio import in metrics.py
  - Fixed timing decorator functionality
  - Restored async/sync function detection
  - No breaking changes to existing functionality

- 2024-04-07: [BUGFIX] Fixed default provider handling
  - Fixed provider selection from DEFAULT_PROVIDER env variable
  - Improved string normalization for provider type conversion
  - Added proper case handling for enum values
  - Updated error handling for invalid provider types
  - Added debug logging for provider selection
  - Maintains backward compatibility
  - No breaking changes to existing functionality

- 2024-04-07: [COMPLETED] Output Format Implementation
  - Successfully implemented all planned output formats:
    - RAW: Unmodified provider output
    - TEXT: Clean text with normalized whitespace (default)
    - JSON: Structured JSON response
    - TELEGRAM_MARKDOWN: Telegram-specific markdown
  - Added comprehensive formatting utilities
  - Integrated with all providers
  - Added extensive test coverage
  - Updated documentation and examples
  - Fixed Telegram markdown code block handling
  - All tests passing with 100% coverage

- 2024-04-07: [FEATURE] Enhanced output formatting support
  - Added new OutputFormat options:
    - RAW: Unmodified output without any formatting
    - TEXT: Plain text formatting (default)
    - MARKDOWN: Standard markdown formatting
    - TELEGRAM_MARKDOWN: Telegram-specific markdown
    - HTML: HTML formatting
  - Separated JSON handling:
    - Removed from OutputFormat enum
    - Added return_json boolean flag
    - Can be combined with any output format
  - Created feature/output-formatting branch
  - No breaking changes to existing functionality
  - Works with all providers and strategies
  - Added format-specific prompt modifications
  - Updated main interface documentation

- 2024-04-07: [FEATURE] Added output format support
  - Added OutputFormat enum with TEXT/MARKDOWN/HTML/JSON support
  - Implemented format-specific prompt modifications
  - Updated main interface with output_format parameter
  - Added examples for each format type
  - No breaking changes to existing functionality
  - Works with all providers and strategies

- 2024-04-06: [FEATURE] Enhanced Perplexity Provider
  - Added Related Questions feature:
    - Implemented `return_related_questions` flag
    - Added question extraction and JSON formatting
    - Created RelatedQuestionsGenerator class
    - Added confidence scoring system
    - Implemented custom prompt support
  - Added web search functionality:
    - Citation extraction and academic formatting
    - Domain filtering support
    - Comprehensive examples and tests
  - Known limitations:
    - Domain filtering is treated as preference
    - Citations may come from non-filtered domains
    - API's related_questions feature in closed beta
    - Using LLM-based generation as fallback

- 2024-04-04: [EXAMPLES] Enhanced example scripts
  - Added random_provider_chat.py for testing multiple providers
  - Added perplexity_chat.py with citations support
  - Enhanced simple_chat.py with rich UI and test questions
  - Created comprehensive examples:
    - Basic web search with citations
    - Domain-specific search
    - Follow-up questions handling

- 2024-04-03: [TESTING] Improved test infrastructure
  - Replaced run_tests.sh with new t.sh script
  - Added colored output and emoji support
  - Enhanced test progress tracking:
    - Individual progress per provider
    - Color-coded results (green/red/yellow)
    - Clear visual separation
    - Comprehensive summary
    - Real-time updates
    - Better error visibility

- 2024-04-03: [PROTECTION] Enhanced stability protection
  - Added protective comments to providers
  - Created .cursorrules with protected files
  - Added triple confirmation requirement
  - Implemented strict version control
  - Updated documentation

- 2024-04-03: [STABLE] Tagged stable Gemini integration (stable_gemini_v1)
  - Added comprehensive test suite (100% pass rate)
  - Added Russian haiku generation
  - Fixed provider initialization
  - Added proper metadata handling

- 2024-03-30: [STABLE] Tagged stable DeepSeek integration (stable_deepseek_v1)
  - Added protection rules and documentation
  - Fixed provider initialization
  - Added basic test coverage

- 2024-03-27: [STABLE] Tagged stable Anthropic integration (stable_anthropic_v1)
  - Added comprehensive test suite (95% coverage)
  - Added fallback strategy tests
  - Added Russian haiku generation tests

- 2024-03-21: [STABLE] Tagged stable Together AI integration (stable_together_v1)
  - Added comprehensive test coverage
  - Added multi-turn conversation tests
  - Updated default model to meta-llama/Llama-Vision-Free

- 2024-01-10: [STABLE] Tagged stable OpenAI version (stable_openai_v1)
  - Added comprehensive test coverage (96%)
  - Added stability protection rules

- 2024-04-07: [PLANNED] JSON Output Format Enhancement
  - Planning to add dedicated JSON output support:
    - New output_format=json flag
    - Structured JSON response formatting
    - Consistent schema across providers
    - Type validation and safety checks
    - Example scripts and documentation
    - Backward compatibility maintained
  - Created feature/json-output branch
  - Work in progress

## Известные проблемы
- Perplexity провайдер в разработке (базовая инициализация работает, но требуется реализация функционала) 

## Perplexity Integration Phase
### Core Features [IN PROGRESS]
- [x] Basic provider implementation
- [x] Chat model integration
- [x] Basic test coverage
- [x] Provider initialization
- [x] Error handling
- [x] Token usage tracking
- [x] Russian haiku generation support
- [x] Citations support
  - [x] Citation extraction
  - [x] Citation formatting (academic style)
  - [x] Citation validation
  - [x] Tests for citations
  - [x] Example web_search.py with citations
- [x] Domain filtering
  - [x] Whitelist support
  - [x] Blacklist support (with `-` prefix)
  - [x] Domain validation
  - [x] Tests for domain filtering
  - [x] Example domain_search.py with scenarios
- [x] Related questions [IMPLEMENTED]
  - [x] Question extraction from API response
  - [x] JSON formatting for questions
  - [x] Confidence scoring
  - [x] Custom prompt support
  - [x] Tests for related questions
  - [x] Example test_related_questions.py
  - [x] Documentation updates
  Features:
    - Automatic generation of 3 follow-up questions
    - Structured JSON output format
    - Question intent and exploration path
    - Configurable via RelatedQuestionsConfig
    - Support for custom prompts
  Known limitations:
    - API's related_questions feature might be in closed beta
    - Currently using LLM-based generation as fallback

### Advanced Features (Future)
- [ ] Search recency filter
- [ ] Presence penalty
- [ ] Frequency penalty
- [ ] Top-k filtering optimization

### Integration Tests
- [x] Citation format validation
- [x] Domain filter effectiveness
- [x] Related questions relevance
- [ ] Image return validation
- [ ] Combined features testing

### Documentation
- [x] Citation format guide
- [x] Domain filtering examples
- [x] Related questions usage
- [ ] Image handling guide
- [x] Integration examples

## Latest Updates
- 2024-04-05: Added Perplexity citations support
  - Implemented citation extraction and formatting
  - Added academic-style citation formatting
  - Created web_search.py example with citations
  - Added comprehensive tests for citations
  - Updated documentation
- 2024-04-05: Added domain search example
  - Created domain_search.py with predefined scenarios
  - Added scientific search scenario
  - Added technical search scenario
  - Added custom domain filtering
  - Integrated with citations support
  - Added comprehensive error handling
- 2024-04-05: Enhanced Perplexity integration
  - Added web search functionality with citations
  - Implemented academic-style citation formatting
  - Added domain filtering support (with known limitations)
  - Created web search examples
  - Added basic test coverage for web search and citations
  - Known limitations:
    - Domain filtering is treated as preference rather than strict filter
    - Citations may come from non-filtered domains
    - Some advanced features still pending implementation

### January 2024

#### Related Questions Feature
- Added `return_related_questions` flag to Perplexity provider
- Implemented automatic generation of follow-up questions
- Created example scripts for testing related questions functionality
- Added JSON formatting for related questions output

Key features:
- Set `return_related_questions=True` to get follow-up questions
- Returns 3 contextually relevant questions
- Questions are returned in structured JSON format
- Supports custom prompts for question generation
- Includes confidence scores and metadata

## Latest Updates
- 2024-04-06: Added Related Questions feature to Perplexity provider
  - Core functionality:
    - Implemented `return_related_questions` flag
    - Added question extraction and JSON formatting
    - Created RelatedQuestionsGenerator class
    - Added confidence scoring system
    - Implemented custom prompt support
  - Documentation:
    - Updated API.md with parameter description
    - Added examples to README.md
    - Updated PROGRESS.md with feature status
  - Testing:
    - Created test_related_questions.py example
    - Added unit tests for question generation
    - Added integration tests for API interaction
  - Known limitations:
    - API's related_questions feature in closed beta
    - Using LLM-based generation as fallback
  - Features implemented:
    - Automatic generation of 3 follow-up questions
    - Structured JSON output format
    - Question intent and exploration path
    - Custom prompt configuration
    - Confidence scoring for relevance

- 2024-04-05: Enhanced Perplexity integration
  - Added web search functionality with citations
  - Implemented academic-style citation formatting
  - Added domain filtering support (with limitations)
  - Created web search examples
  - Added basic test coverage
  Known limitations:
    - Domain filtering is treated as preference
    - Citations may come from non-filtered domains

- 2024-04-03: [TESTING] Improved test infrastructure
  - Replaced run_tests.sh with new t.sh script
  - Added colored output for better test visibility
  - Enhanced test progress tracking for each provider
  - Added individual test status tracking
  - Improved test summary reporting
  - Added emoji support for better UX
  - Features of new test script:
    - Individual progress tracking per provider
    - Color-coded test results (green/red/yellow)
    - Clear visual separation between providers
    - Comprehensive test summary
    - Improved error visibility
    - Better user experience with emojis
    - Native bash implementation for better performance
    - Real-time test status updates
    - Clear success/failure indicators

- 2024-04-04: [FEATURE] Enhanced Perplexity Integration
  - Added web search examples with domain filtering
  - Implemented related questions API support
  - Added citation extraction and formatting
  - Created comprehensive examples:
    - Basic web search with citations
    - Domain-specific search
    - Follow-up questions handling
    - Related questions API usage
  - Updated base provider interface
  - Enhanced type system for web search support
  - Updated documentation with API usage examples

## Phase 3: Testing and Quality Assurance
- [x] Fix base provider tests
  - [x] Abstract class implementation
  - [x] Error handling tests
  - [x] Provider initialization tests
- [x] Fix configuration tests
  - [x] Config caching tests
  - [x] Environment variable handling
- [x] Fix formatter tests
  - [x] Telegram markdown formatting
  - [x] Code block handling
- [x] Fix strategy tests
  - [x] Strategy switching tests
  - [x] Error handling tests
  - [x] Provider type validation

## Next Steps
- [ ] Add streaming support for all providers
- [ ] Implement cost calculation for all providers
- [ ] Add comprehensive multi-turn conversation tests
- [ ] Improve error handling and recovery strategies

## Latest Updates
- 2024-04-07: [BUGFIX] Removed hardcoded providers from examples
  - Removed provider hardcoding from all example scripts
  - Now using DEFAULT_PROVIDER from .env consistently
  - Updated basic_usage.py to use configuration
  - Updated perplexity_chat.py to use configuration
  - Updated web_search.py to use configuration
  - Updated domain_search.py to use configuration
  - Updated follow_up_search.py to use configuration
  - Improved example documentation
  - No breaking changes to existing functionality

- 2024-04-07: [BUGFIX] Removed hardcoded default provider
  - Removed OpenAI hardcoding from factory.py
  - Now strictly using DEFAULT_PROVIDER from .env
  - Added proper error handling for missing provider
  - Updated provider initialization logic
  - Improved configuration loading
  - No breaking changes to existing functionality

- 2024-04-07: [BUGFIX] Fixed DeepSeek provider implementation
  - Added missing abstract methods _generate and _get_provider_type
  - Fixed method signatures to match base class
  - Updated error handling and metadata creation
  - Improved response processing
  - No breaking changes to existing functionality

- 2024-04-07: [BUGFIX] Fixed OpenAI provider implementation
  - Renamed generate to _generate (private method)
  - Added missing _get_provider_type method
  - Updated method signatures to match base class
  - Improved error handling and metadata creation
  - No breaking changes to existing functionality

- 2024-04-07: [BUGFIX] Fixed Together provider implementation
  - Renamed generate to _generate (private method)
  - Added missing _get_provider_type method
  - Updated method signatures to match base class
  - Improved error handling and metadata creation
  - No breaking changes to existing functionality

- 2024-04-07: [BUGFIX] Fixed Anthropic provider implementation
  - Renamed generate to _generate (private method)
  - Added missing _get_provider_type method
  - Updated method signatures to match base class
  - Improved error handling and metadata creation
  - Added system prompt support
  - No breaking changes to existing functionality

## Progress Report

## Latest Updates
- [x] Fixed token usage counting and cost calculation
  - Updated token usage extraction in all providers
  - Added proper cost calculation based on model pricing
  - Fixed metadata creation to match LLMMetadata schema
  - Added cost tracking for:
    - OpenAI (GPT-3.5 and GPT-4)
    - Anthropic (Claude 3 Haiku/Sonnet/Opus)
    - Together AI (all models)
  - No breaking changes to existing functionality

# Progress Log

## Latest Updates

### 2024-03-19
- Улучшена интеграция с Gemini SDK:
  - Добавлена поддержка system instruction
  - Добавлены дополнительные параметры конфигурации (top_k, safety_settings, tools)
  - Улучшен подсчет токенов с учетом system instruction
  - Реализована конвертация синхронного API в асинхронный
  - Наследование от BaseLLMProvider и реализация абстрактных методов
  - Улучшена обработка ошибок и метаданных

### Previous Updates
- Добавлен подсчет стоимости для всех провайдеров
- Обновлены тесты для проверки подсчета токенов и стоимости
- Обновлены примеры для отображения информации о стоимости
- Добавлена статистика сессии во все интерактивные примеры
- Добавлен подсчет токенов для Gemini провайдера
- Добавлена зависимость tiktoken для подсчета токенов
- Реализована оценка стоимости для Gemini Pro ($0.00025 за 1K токенов)
- Добавлен fallback на приблизительный подсчет токенов при отсутствии tiktoken

## Последние улучшения

### Упрощение интерфейса (Январь 2024)

1. Добавлен простой синхронный интерфейс:
   - Функция `send_2_llm_sync` для использования без async/await
   - Простой вызов в одну строку
   - Полная совместимость со всеми возможностями библиотеки

2. Обновлена документация:
   - Новые примеры использования в README.md
   - Подробное API Reference с описанием всех интерфейсов
   - Рекомендации по выбору подходящего интерфейса

3. Три уровня абстракции:
   - Простой синхронный (`send_2_llm_sync`)
   - Асинхронный основной (`send_2_llm`)
   - Продвинутый с полным контролем (`LLMClient`)

- 2024-04-07: [IMPROVEMENT] Enhanced OpenAI Provider Configuration
  - Added OPENAI_MODEL environment variable support
  - Default model now configurable via environment
  - Maintains backward compatibility with gpt-3.5-turbo default
  - Improved consistency with other providers
  - No breaking changes to functionality

- 2024-04-07: [FEATURE] Created OpenAI Provider V2
  - Created new OpenAIProviderV2 with full env configuration:
    - Model selection from OPENAI_MODEL
    - Temperature from TEMPERATURE
    - Top-p from TOP_P
    - Max tokens from MAX_TOKENS
    - Presence penalty from PRESENCE_PENALTY
    - Frequency penalty from FREQUENCY_PENALTY
  - Maintains backward compatibility
  - Original provider preserved as stable_openai_v1
  - Updated provider factory to use V2
  - No breaking changes to functionality