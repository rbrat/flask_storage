from app import db
from datetime import datetime
from uuid import uuid4 as uuid
import os


def get_available_file_name(filename):
    ident = ''
    file = StoredFile.query.filter_by(filename=filename).first()
    if file is None:
        return filename
    filename, ext = os.path.splitext(filename)
    while file is not None:
        ident = str(uuid())[:8]
        file = StoredFile.query.filter_by(
            filename=f'{filename}_{ident}{ext}').first()
    return f'{filename}_{ident}{ext}'


def check_available_uuid(uuid):
    file = StoredFile.query.filter_by(uuid=uuid).first()
    return file is None


def get_available_uuid():
    file_uuid = str(uuid())
    while(not check_available_uuid(file_uuid)):
        file_uuid = str(uuid())
    return file_uuid


class StoredFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String, nullable=False, unique=True)
    filename = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<File {self.filename}>'
