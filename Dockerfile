FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml .

RUN uv sync

COPY . .

EXPOSE 8080

CMD ["uv", "run", "scripts/start.py"]