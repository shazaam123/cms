FROM python:3.8.18

WORKDIR /app

VOLUME ./app

COPY . . 

RUN python3 -m venv ./app/venv

ENV PATH="/app/.venv/bin:$PATH"

RUN python --version

RUN pip --version

RUN python -m ensurepip --upgrade

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

RUN chown -R root:root /app

RUN python main.py collectstatic --noinput

CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi