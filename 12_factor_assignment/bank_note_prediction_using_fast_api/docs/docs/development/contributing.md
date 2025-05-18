# Contributing Guidelines

## Project Structure
This project follows the cookiecutter data science project structure:

```
├── data/
│   ├── external/       # Data from third party sources
│   ├── interim/        # Intermediate data
│   ├── processed/      # Final, canonical data sets
│   └── raw/           # Original, immutable data
├── models/            # Trained models
├── notebooks/         # Jupyter notebooks
├── docs/             # Documentation
├── references/       # Data dictionaries, manuals, etc.
├── reports/          # Generated analysis
│   └── figures/      # Generated graphics
└── src/             # Source code
```

## Development Process

1. Create a new branch for your feature
```bash
git checkout -b feature/your-feature-name
```

2. Follow code style guidelines
- Use PEP 8 for Python code style
- Add type hints to function parameters
- Write docstrings for functions and classes

3. Write tests
- Add unit tests in the `tests/` directory
- Ensure all tests pass before submitting PR

4. Documentation
- Update relevant documentation in `docs/`
- Include docstrings for new functions/classes
- Update API documentation if endpoints change

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the requirements.txt if you add dependencies
3. Run all tests and ensure they pass
4. Submit the pull request with a clear description

## Running Tests
```bash
pytest tests/
```