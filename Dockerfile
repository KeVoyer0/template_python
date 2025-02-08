# Builder stage
FROM ghcr.io/prefix-dev/pixi:0.41.1 AS builder

WORKDIR /app
COPY . .

RUN pixi install --frozen -e prod && \
    pixi shell-hook -e prod -s bash > /activate && \
    echo 'exec "$@"' >> /activate

# Runtime stage
FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    ca-certificates \
    && useradd -m appuser \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /activate /app/
COPY --from=builder /app/.pixi/envs/prod /app/.pixi/envs/prod
COPY --chown=appuser:appuser . /app

USER appuser
WORKDIR /app
ENTRYPOINT ["/bin/bash", "/app/activate"]
CMD ["start"]