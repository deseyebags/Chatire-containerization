FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8081

WORKDIR /app

# system deps for typical Python packages (adjust if you need postgres/mysql headers)
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# NOTE: this Dockerfile is intended to be built from the repository root so the build context
# includes manage.py and requirements.txt. Example:
#   docker build -f chat/Dockerfile -t chatire-chat-app .

# copy requirements from repo root (build context must include them)
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy whole project into container (requires repo root as build context)
COPY . /app

# copy entrypoint which runs migrations before starting the server
COPY chat/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8081

ENTRYPOINT ["docker-entrypoint.sh"]
# default: run Django development server (channels README used port 8081)
CMD ["runserver", "0.0.0.0:8081"]