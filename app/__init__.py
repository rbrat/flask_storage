from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, AllExcept, SCRIPTS, EXECUTABLES
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
upload_set = UploadSet(default_dest=lambda app:'app/'+app.config['UPLOAD_FOLDER'],
                       extensions=AllExcept(SCRIPTS+EXECUTABLES))
uploads = configure_uploads(app, upload_set)

from app import routes, models
