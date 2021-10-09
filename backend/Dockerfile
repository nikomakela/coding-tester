FROM python:3 as appbase


ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN mkdir /entrypoint

COPY requirements*.txt /app/

RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /entrypoint/
ENTRYPOINT ["/entrypoint/docker-entrypoint.sh"]

# ==============================
FROM appbase as staticbuilder
# ==============================

ENV VAR_ROOT /app
COPY . /app
RUN python manage.py collectstatic --noinput

# ==============================
FROM appbase as production
# ==============================

ENV VAR_ROOT /app
COPY --from=staticbuilder /app/static /app/static
COPY . /app/

EXPOSE 8000/tcp
