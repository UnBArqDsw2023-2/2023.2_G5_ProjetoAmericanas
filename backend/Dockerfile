FROM python:3.11-slim-bullseye

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /backend

# Install apt packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    # dependencies for building Python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev \
    # clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN python3 -m pip install --no-cache-dir pip==23.2.*
COPY requirements.txt /tmp/
COPY requirements_production.txt /tmp/
RUN pip install --default-timeout=15000 --no-cache-dir -r /tmp/requirements.txt -r /tmp/requirements_production.txt

# Django user
RUN addgroup --system django \
    && adduser --system --ingroup django django

COPY --chown=django:django core /backend/core
COPY --chown=django:django americanas /backend/americanas
COPY --chown=django:django manage.py /backend/manage.py
COPY --chown=django:django start.sh /backend/start.sh

RUN mkdir -p /backend/static
RUN chown django:django /backend/static

RUN chown django:django /backend

RUN chmod +x /backend/start.sh

USER django

CMD /backend/start.sh
