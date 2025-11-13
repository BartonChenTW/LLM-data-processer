# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `InfoExtractor` class for structured information extraction
  - Custom Pydantic schema support for defining data structures
  - Automatic retry logic with malformed output fixing
  - LangChain integration for robust JSON parsing
  - Validation system to ensure proper setup before extraction
  - Support for complex field types (str, int, float, bool, List, Dict)
- PDF processing utilities
  - `read_pdf2text()` function for extracting text from PDF documents
  - Integration with pdfplumber for reliable PDF parsing
  - LangChain text splitter support
- Enhanced documentation
  - InfoExtractor API reference with complete method documentation
  - Structured extraction usage patterns and examples
  - Batch processing examples for multiple documents
  - PDF analysis examples
- New example scripts
  - `examples/info_extractor_usage.py` with 4 comprehensive examples

### Changed
- **BREAKING**: `AIHelper.add_guideline()` now requires `guideline_name` parameter
  - Old: `ai.add_guideline("Use bullet points")`
  - New: `ai.add_guideline('format', "Use bullet points")`
- **BREAKING**: `AIHelper.attach_data()` now requires `data_name` parameter
  - Old: `ai.attach_data(df)`
  - New: `ai.attach_data('employees', df)`
- `AIHelper.guideline` changed from `List[str]` to `Dict[str, str]`
- `AIHelper.attached_data` changed from `List[pd.DataFrame]` to `Dict[str, Union[pd.DataFrame, str]]`
- `AIHelper.attach_data()` now supports both DataFrame and string data types

### Fixed
- Chat widget input now clears after sending message
- Improved error handling in InfoExtractor with detailed validation messages

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
