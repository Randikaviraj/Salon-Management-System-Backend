# Bcrypt for hash the function
from flask.ext.bcrypt import Bcrypt
from Server import app


bcrypt = Bcrypt(app)