from Server import app
from Server.config import HOST,PORT
from Server.db import db

print(db)
@app.route('/')
def index():
    return "started"

if __name__=='__main__':
    app.run(host=HOST, port=PORT, debug=True)
    