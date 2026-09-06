FROM python:3.12-bookworm

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.12.7 /uv /uvx /bin/

ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

# RTxReadBin
COPY RTxReadBin-1.0-py3-none-any.whl /tmp/

RUN uv pip install \
    --python /opt/venv/bin/python \
    /tmp/RTxReadBin-1.0-py3-none-any.whl

RUN /opt/venv/bin/python -c \
    "from RSRTxReadBin import RTxReadBin; print('RTxReadBin OK')"

CMD ["bash"]
