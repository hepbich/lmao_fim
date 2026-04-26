FROM python:3.11.2-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ~/ZirkaBot

COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY zirka_bot ./zirka_bot

CMD ["python", "-m", "zirka_bot"]

# -------------------------------
# Build an image from a Dockerfile:
# $ docker build -t Zirka_bot .
# -------------------------------
# Create and run a new container from an image:
# $ docker run -d --name ZirkaBot \
#    --env "BOT_TOKEN=<BOT_TOKEN>" \
#    --env "AI_KEY=<AI_KEY>" \
#    --env "VCHAT_ID=<VCHAT_ID>" \
#    --env "DCHAT_ID=<DCHAT_ID>" \
#    --env "SCHAT_ID=<SCHAT_ID>" \
#    Zirka_bot
# -------------------------------
# Stop running container:
# $ docker stop ZirkaBot
# -------------------------------
# Start stopped container:
# $ docker start ZirkaBot
# -------------------------------
# Remove container:
# $ docker rm ZirkaBot
# -------------------------------
# Remove image:
# $ docker rmi Zirka_bot
# -------------------------------
# Execute a command in a running container:
# $ docker exec -it ZirkaBot bash