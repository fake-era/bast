# Build stage
FROM python:slim-buster AS builder

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake

WORKDIR /src

COPY ./src/requirements.txt .

RUN pip install --upgrade pip \
    && pip wheel --no-cache-dir --no-deps --wheel-dir /src/wheels -r requirements.txt

# Final stage
FROM python:slim-buster

WORKDIR /src

COPY --from=builder /src/wheels /wheels
COPY --from=builder /src/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY . .

ADD ./src/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

CMD ["./entrypoint.sh"]
