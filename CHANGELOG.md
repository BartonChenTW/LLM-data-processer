# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Streaming response support
- Additional LLM providers (Anthropic, Cohere)
- Enhanced data visualization
- Model fine-tuning utilities
- Conversation history export
- Multi-language support

## [0.0.1] - 2025-11-12

### Added
- Initial release of LLM Data Processer
- `AIHelper` class for Hugging Face Inference API
  - Support for Llama-3.1 and Mistral-7B models
  - Interactive chat widget for Jupyter notebooks
  - Data attachment via pandas DataFrames
  - Custom guideline system
  - Conversation history tracking
- `AIHelper_Google` class for Google Gemini
  - Gemini 2.5 Flash model support
  - Google Search grounding integration
  - Simple ask interface
- Package structure with `__init__.py`
- Comprehensive README with usage examples
- Setup.py for pip installation
- Requirements.txt with all dependencies
- .env.example for API key configuration
- .gitignore for Python projects
- VS Code workspace settings
- CONTRIBUTING.md with contribution guidelines
- MIT License

### Documentation
- Complete API documentation
- Quick start guide
- Multiple usage examples
- Troubleshooting section
- Installation instructions for Windows/Linux/Mac

### Configuration
- Configurable temperature and max_tokens
- Support for HF_TOKEN, GEMINI_API_KEY, OPENAI_API_KEY
- VS Code integration for notebook kernels

[Unreleased]: https://github.com/BartonChenTW/LLM-data-processer/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/BartonChenTW/LLM-data-processer/releases/tag/v0.0.1
