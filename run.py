from Server import app
from Server.config import HOST,PORT
from Server.service.clientRoute import client_route
from Server.owner.sellerRoute import seller_route

app.register_blueprint(client_route,url_prefix="/service")
app.register_blueprint(seller_route,url_prefix="/owner")


@app.route('/')
def index():
    return "started"

if __name__=='__main__':
    app.run(host=HOST, port=PORT, debug=True,use_debugger=False)
    