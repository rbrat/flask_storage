import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretniy-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or f"sqlite:///{os.path.join(basedir,'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'storage'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
