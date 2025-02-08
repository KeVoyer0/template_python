#!/bin/bash
set -eo pipefail

# Production environment validation
if [ -z "${PIXI_ENVIRONMENT}" ] || [ "${PIXI_ENVIRONMENT}" != "prod" ]; then
    echo "ERROR: Not running in production environment!" >&2
    exit 1
fi

# Main application execution
exec "$@"