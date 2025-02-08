# A reproducible Python project with multi-environment testing

A reproducible Python project template with multi-Python version testing, integrated Pixi workflows, and a Dockerized pre-commit setup. This template provides:

- **Cross-environment reproducibility:** Manage multiple Python versions (3.8 to 3.11) using Pixi.
- **Pre-commit hooks:** Automatically format, lint, and type-check your code using Black, Ruff, and Pyright.
- **Docker-based checks:** Run pre-commit hooks in a Docker container for a consistent environment.
- **Script-based automation:** Use Pixi tasks to run tests, build docs, and more.

## Features

- **Multi-Python Environment:** Define separate environments for Python 3.8, 3.9, 3.10, and 3.11.
- **Pre-commit Hooks:** Ensure code quality with automated checks on commit.
- **Docker Integration:** Use the provided Dockerfile to run pre-commit hooks inside a container.
- **Type Checking with Pyright:** Replace mypy with pyright for fast and accurate type checking.
- **Workflow Automation:** Tasks for testing, linting, documentation, building, and releasing are defined via Pixi.

## Requirements

- **Python ≥ 3.10:** For local development.
- **Docker:** To use the Docker-based pre-commit environment.
- **Node.js:** Required in the Docker image for Pyright.

## Getting Started

### Local Development

1. **Clone the repository:**

   ```bash
   git clone https://your.repo.url/your_project.git
   cd your_project
   ```

2. **Update submodules for Pyright type checking:**

    ```bash
    git submodule update --init --remote --merge typings
    ```

3. **Install Pixi**

    see: <https://pixi.sh/latest/>

4. **Set up environments:**

    ```bash
    pixi install
    ```

    - *PyPI Compatibility Layer Non-Pixi users can install with:*

        ```bash
        pip install .[test,docs,dev]  # Standard PyPI installation
        ```

5. **Install pre-commit hooks:**

    ```bash
    pre-commit install
    ```

6. **Run workflow tasks using Pixi:**
    - Testing:

        ```bash
        pixi run test
        ```

        *To test a specific Python version (e.g., Python 3.11):*

        ```bash
        pixi run -e py311 test
        ```

    - Linting:

        ```bash
        pixi run lint
        ```

    - Type Validation

        ```bash
        pixi run typecheck
        ```

    - Dead Code Detection

        ```bash
        pixi run deadcode
        ```

    - Building Documentation:

        ```bash
        pixi run docs
        ```

    - Building Distribution Packages:

        ```bash
        pixi run build
        ```

### Docker-based Pre-commit Checks

1. **Build the Docker image:**

    ```bash
    docker build -f .docker/precommit.Dockerfile -t precommit-check .
    ```

2. **Run the Docker container to execute pre-commit hooks:**

    ```bash
    docker run --rm -v "$(pwd)":/app precommit-check
    ```

This container will:

- Set up a consistent environment (including Node.js for Pyright).
- Install project dependencies via Pixi.
- Execute all pre-commit hooks defined in .pre-commit-config.yaml.

## Project Structure Overview

```plaintext
root
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── source/
│   │   ├── conf.py
│   │   └── index.rst
│   └── build/
├── src/
│   └── package_name/
│       ├── __init__.py
│       └── core.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── pyproject.toml
└── README.md
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and ensure all tests pass.
4. Submit a pull request with a clear description of your changes.

## License

MIT License

## Maintenance Benefits

- Single-file configuration reduces cognitive overhead
- Automatic environment isolation prevents version conflicts
- Cross-platform reproducibility through Conda ecosystem
- Gradual adoption path for Pixi without breaking existing workflows
- Reproducible Environments
  - Locked dependencies via pixi.lock
  - Cross-platform support through Conda-forge channels
  - Shared solve-groups ensure consistent dependency versions across environments
- Integrated Workflow Automation

    ```bash
    pixi run lint   # Run code quality checks
    pixi run docs   # Build documentation
    pixi run test   # Execute test suite
    pixi run build  # Create distribution packages
    ```

- Advanced Features
  - Environment-specific tasks (e.g., pixi run -e docs live-docs)
  - Feature-based dependency groups
  - Cross-environment dependency sharing through solve-groups
