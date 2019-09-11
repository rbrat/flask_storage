from flask import request, send_from_directory, redirect, jsonify, abort, render_template
from app import app, db, upload_set
from app.models import StoredFile, get_available_file_name, get_uuid
from werkzeug import secure_filename
from datetime import datetime
import os


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/v1/download/<file_uuid>')
def get_file(file_uuid):
    file = StoredFile.query.filter_by(uuid=file_uuid).first()
    print(file)
    print(os.path.join(app.root_path, app.config['UPLOAD_FOLDER']))
    if file:
        return send_from_directory(directory=os.path.join(app.root_path, app.config['UPLOAD_FOLDER']), filename=file.filename, as_attachment=True)
    else:
        abort(404, description=f'No file found with uuid {file_uuid}')


@app.route('/v1/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        abort(400, description='No file part')
    file = request.files['file']
    if file:
        try:
            filename=get_available_file_name(secure_filename(file.filename))
            upload_set.save(file, name=filename)
            stored_file = StoredFile(filename=filename, uuid=get_uuid())
            db.session.add(stored_file)
            db.session.commit()
            return jsonify({'file': stored_file.uuid}), 201
        except Exception as e:
            abort(400, description=e)

