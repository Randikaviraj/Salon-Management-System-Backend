# Bcrypt for hash the function
from flask_bcrypt import Bcrypt
from Server import app


bcrypt = Bcrypt(app)