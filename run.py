from Server import app
from Server.config import HOST,PORT
import os


@app.route('/')
def index():
    return "started"

if __name__=='__main__':
    print(os.getenv('MY_TOKEN', 'Token Not found'))
    app.run(host=HOST, port=PORT, debug=True)
    