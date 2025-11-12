# Contributing

Thank you for your interest in contributing to LLM Data Processer!

## Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit code changes
- ✅ Add tests
- 💬 Help others in discussions

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/LLM-data-processer.git
cd LLM-data-processer
```

### 2. Set Up Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install -r requirements.txt
pip install -e ".[dev]"
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

## Development Guidelines

### Code Style

Follow PEP 8 and use type hints:

```python
def add_guideline(self, guideline: str) -> None:
    """Add a custom guideline to influence model behavior.
    
    Args:
        guideline: A string describing the desired behavior
    
    Returns:
        None
    """
    self.guideline.append(guideline)
```

### Docstring Format

Use Google-style docstrings:

```python
def ask(self, prompt: str, with_history: bool = True) -> str:
    """Generate a response from the LLM.
    
    Args:
        prompt: The question or instruction to send
        with_history: Whether to include conversation context
    
    Returns:
        The model's response as a string
    
    Raises:
        ValueError: If prompt is empty
    """
```

### Testing

Test your changes manually:

```python
# Test basic functionality
from llm_helper import AIHelper

ai = AIHelper(model_name='Llama-3.1', display_response=False)
response = ai.ask("Test question")
assert isinstance(response, str)
```

## Adding New Features

### Adding a New LLM Provider

1. Create a new class in `llm_helper/ai_helper.py`:

```python
class AIHelper_NewProvider:
    def __init__(self, model: str = 'default-model', display_response: bool = True):
        self.client = NewProviderClient()
        self.model = model
        self.display_response = display_response
        self.history = []
    
    def ask(self, prompt: str, display_response: bool = None) -> str:
        """Generate response using NewProvider."""
        # Implementation
        pass
```

2. Update `__init__.py`:

```python
from .ai_helper import AIHelper, AIHelper_Google, AIHelper_NewProvider

__all__ = ["AIHelper", "AIHelper_Google", "AIHelper_NewProvider"]
```

3. Add documentation
4. Add examples
5. Update README

### Adding New Methods

1. Add method to class
2. Add docstring
3. Update API reference
4. Add usage example
5. Test thoroughly

## Submitting Changes

### Commit Guidelines

```bash
# Good commit messages
git commit -m "Add: Support for Claude API"
git commit -m "Fix: Memory leak in chat_widget"
git commit -m "Docs: Update installation guide"

# Bad commit messages
git commit -m "updates"
git commit -m "fix stuff"
```

### Pull Request Process

1. **Update documentation** if needed
2. **Test your changes**
3. **Update CHANGELOG.md**
4. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** on GitHub
6. **Address review feedback**

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
How you tested your changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Examples added (if applicable)
```

## Documentation

### Updating Docs

Documentation is in the `docs/` folder using Markdown.

```bash
# Edit docs
vim docs/usage.md

# Preview locally (if MkDocs is installed)
mkdocs serve
```

### Adding Examples

Add to `examples/` folder with clear comments:

```python
"""
Example: Analyzing customer data with AI.

This example shows how to...
"""

from llm_helper import AIHelper
import pandas as pd

# Step 1: Load data
df = pd.DataFrame({...})

# Step 2: Initialize AI
ai = AIHelper(...)

# Step 3: Query
response = ai.ask(...)
```

## Community Guidelines

### Be Respectful

- Be welcoming to newcomers
- Provide constructive feedback
- Respect different viewpoints
- Focus on the code, not the person

### Getting Help

- 📖 Read the [documentation](https://bartonchenTW.github.io/LLM-data-processer/)
- 💬 Ask in [GitHub Discussions](https://github.com/BartonChenTW/LLM-data-processer/discussions)
- 🐛 Check [existing issues](https://github.com/BartonChenTW/LLM-data-processer/issues)

## Development Tips

### Testing Locally

```python
# Quick smoke test
python -c "from llm_helper import AIHelper; ai = AIHelper(); print('OK')"

# Run examples
python examples/basic_usage.py
```

### Debugging

```python
# Enable verbose logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Test in interactive mode
python -i -m llm_helper.ai_helper
```

### Performance

- Keep responses under 2 seconds for simple queries
- Optimize DataFrame serialization for large datasets
- Cache repeated queries when appropriate

## Release Process

Maintainers follow this process:

1. Update version in `__init__.py` and `setup.py`
2. Update `CHANGELOG.md`
3. Create git tag: `git tag v0.0.2`
4. Push tag: `git push --tags`
5. Create GitHub release
6. Deploy documentation

## Recognition

Contributors will be:

- Added to `CONTRIBUTORS.md`
- Mentioned in release notes
- Credited in documentation

## Questions?

Open an issue with the `question` label or ask in Discussions.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing!** 🎉
