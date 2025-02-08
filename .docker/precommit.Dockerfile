# Use an official slim Python image
FROM python:3.11-slim

# Install system dependencies including Node.js (for Pyright)
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Install Pixi and pre-commit
RUN pip install --no-cache-dir pixi pre-commit

# (Optional) Install pyright globally if needed
RUN npm install -g pyright

# Install Pixi environments
RUN pixi install

# Default command runs all pre-commit hooks
CMD ["pre-commit", "run", "--all-files"]
