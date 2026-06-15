FROM python:3.13-slim
WORKDIR /app

# 1. Copy dependencies first (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy source code
COPY . .

# 3. Syntax check
RUN python -m py_compile app.py

# 4. Expose container port (fixed at 8000)
EXPOSE 8000

# 5. Healthcheck (checks inside container, unaffected by host port)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

# 6. Default command
CMD ["python", "app.py"]