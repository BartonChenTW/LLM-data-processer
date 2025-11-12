# LLM Data Processer Documentation

This directory contains the documentation source files for LLM Data Processer, built with [MkDocs](https://www.mkdocs.org/) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).

## Building Documentation Locally

### Prerequisites

```bash
pip install mkdocs-material
```

### Build and Serve

```bash
# Serve locally with live reload
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages (maintainers only)
mkdocs gh-deploy
```

The documentation will be available at `http://127.0.0.1:8000/`

## Documentation Structure

```
docs/
├── index.md              # Home page
├── installation.md       # Installation guide
├── usage.md              # Usage guide
├── api-reference.md      # API documentation
├── examples.md           # Code examples
└── contributing.md       # Contributing guide
```

## Writing Documentation

### Markdown Extensions

The documentation supports:

- **Admonitions**: Notes, warnings, tips
- **Code blocks**: With syntax highlighting
- **Tabs**: For multi-platform instructions
- **Tables**: For reference data
- **Emojis**: For visual emphasis

### Examples

#### Admonition

```markdown
!!! note
    This is a note.

!!! warning
    This is a warning.
```

#### Code Block with Tabs

```markdown
=== "Python"
    ```python
    print("Hello World")
    ```

=== "JavaScript"
    ```javascript
    console.log("Hello World");
    ```
```

#### Code Block with Highlighting

```markdown
```python hl_lines="2 3"
def example():
    x = 1  # This line will be highlighted
    y = 2  # This line too
    return x + y
\```
```

## Contributing to Docs

1. Edit the `.md` files in the `docs/` directory
2. Test locally with `mkdocs serve`
3. Submit a pull request

## Deployment

Documentation is automatically deployed to GitHub Pages when changes are pushed to the `main` branch via GitHub Actions (`.github/workflows/docs.yml`).

The docs will be available at: https://bartonchenTW.github.io/LLM-data-processer/
