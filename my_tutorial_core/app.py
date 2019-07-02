from flask import Flask, Blueprint

from my_tutorial_core.restplus import api
from my_tutorial_core.controller.tutorial import ns_tutorial
from my_tutorial_core.db import config_db
from my_tutorial_core.log import log

app = Flask(__name__)


def initialize_app(app):
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['ERROR_404_HELP'] = False

    config_db(app)
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    api.add_namespace(ns_tutorial)


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=True)


if __name__ == '__main__':
    main()
