from Server import app
from Server.config import HOST,PORT
from Server.service.clientRoute import client_route

app.register_blueprint(client_route,url_prefix="/service")


@app.route('/')
def index():
    return "started"

if __name__=='__main__':
    app.run(host=HOST, port=PORT, debug=True,use_debugger=False)
    