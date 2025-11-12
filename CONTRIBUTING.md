# Contributing to LLM Data Processer

Thank you for considering contributing to LLM Data Processer! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior vs actual behavior
- Your environment (OS, Python version, package versions)
- Code samples or error messages

### Suggesting Enhancements

Feature requests are welcome! Please create an issue with:
- A clear description of the feature
- Use cases and examples
- Why this feature would be useful
- Any relevant API designs or mockups

### Pull Requests

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/LLM-data-processer.git
   cd LLM-data-processer
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set Up Development Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e ".[dev]"  # Install dev dependencies
   ```

4. **Make Your Changes**
   - Write clear, commented code
   - Follow PEP 8 style guidelines
   - Add docstrings to new functions/classes
   - Update documentation if needed

5. **Test Your Changes**
   ```bash
   # Run any existing tests
   pytest tests/
   
   # Test manually in notebook
   jupyter notebook
   ```

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```
   
   Commit message guidelines:
   - Use present tense ("Add feature" not "Added feature")
   - Be concise but descriptive
   - Reference issues: "Fix #123: Description"

7. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then open a Pull Request on GitHub.

## Development Guidelines

### Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints where applicable
- Keep functions focused and modular
- Add docstrings to all public methods

Example:
```python
def add_guideline(self, guideline: str) -> None:
    """Add a custom guideline to influence model behavior.
    
    Args:
        guideline: A string describing the desired behavior
    
    Returns:
        None
    """
    self.guideline.append(guideline)
    print("Guideline added.")
```

### Adding New LLM Providers

To add support for a new LLM provider:

1. Create a new class in `llm_helper/ai_helper.py`
2. Implement the standard interface:
   - `__init__()`
   - `ask(prompt: str) -> str`
   - Optional: `chat_widget()`
3. Add configuration in the module
4. Update README with examples
5. Add to `__init__.py` exports

### Testing

- Test with different models
- Verify Jupyter notebook widgets work
- Check API key handling
- Test error conditions

### Documentation

- Update README.md for new features
- Add docstrings to new code
- Update CHANGELOG.md
- Include usage examples

## Code Review Process

1. Maintainers will review your PR
2. Address any feedback or requested changes
3. Once approved, your PR will be merged
4. You'll be added to contributors!

## Community

- Be respectful and constructive
- Help others in issues and discussions
- Share your use cases and examples

## Questions?

Feel free to open an issue with the "question" label or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
