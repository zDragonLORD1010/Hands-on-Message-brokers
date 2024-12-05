FROM python:3.12 AS base

WORKDIR /app/src

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./src /app/src

CMD ["python", "main.py"]

FROM base AS api_service

COPY ./src/services/api.py /app/src/main.py

FROM base AS filter_service

COPY ./src/services/filter.py /app/src/main.py

FROM base AS screaming_service

COPY ./src/services/screaming.py /app/src/main.py

FROM base AS sending_service

COPY ./src/services/sending.py /app/src/main.py

FROM base AS single_service

COPY ./src/services/single.py /app/src/main.py
