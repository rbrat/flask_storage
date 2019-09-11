FROM python:3

RUN adduser storage

WORKDIR /home/storage

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
RUN mkdir app/storage
COPY migrations migrations
COPY storage.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP storage.py
ENV SECRET_KEY E7CA80D9-41DF-4FB5-B62F-582B5BF3012E
ENV UPLOAD_FOLDER storage

RUN chown -R storage:storage ./
USER storage

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]