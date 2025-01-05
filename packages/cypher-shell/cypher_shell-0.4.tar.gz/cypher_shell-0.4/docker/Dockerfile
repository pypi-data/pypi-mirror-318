FROM python:3.12-slim

WORKDIR /app
COPY . .

RUN python3 -m pip install -e .

CMD ["python3", "-m", "cypher_shell"]
