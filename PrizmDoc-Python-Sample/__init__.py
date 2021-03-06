from flask import Flask

from config import args as config
from views import index, viewer
from services import proxy, viewing_session

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(index.blueprint)
app.register_blueprint(viewer.blueprint)
app.register_blueprint(proxy.blueprint)
app.register_blueprint(viewing_session.blueprint)

if __name__ == "__main__":
    app.run(port=config.port, debug=True)
