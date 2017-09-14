FROM python:3.5-alpine

ADD requirements.txt /requirements.txt

# Install build deps, then run `pip install`
# Then, remove unneeded build deps all in a single step
RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
            gcc \
            make \
            libc-dev \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev \
            musl-dev \
            postgresql-dev \
            bash \
    && pyvenv /venv \
    && /venv/bin/pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /requirements.txt" \
    && runDeps="$( \
            scanelf --needed --nobanner --recursive /venv \
                    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                    | sort -u \
                    | xargs -r apk info --installed \
                    | sort -u \
    )" \
    && apk add --virtual .python-rundeps $runDeps \
    && apk del .build-deps

# Install npm for apidoc
RUN apk update && apk add nodejs
RUN npm install apidoc -g

# Update API docs
RUN apidoc -i api/routes -o docs/

# Make DB Migrations
# RUN /venv/bin/python manage.py makemigrations api
# RUN /venv/bin/python manage.py migrate

# uWSGI will listen on this port
EXPOSE 8000

# uWSGI configuration:
ENV UWSGI_VIRTUALENV=/venv UWSGI_WSGI_FILE=wolfbeacon/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Start uWSGI
CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]
