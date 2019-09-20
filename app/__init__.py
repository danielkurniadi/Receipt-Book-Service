from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
flask_app = Flask(__name__)

# Configurations
flask_app.config.from_object('config.flask_config')


def setup_db():
    # Import models here
    # db.create_all()
    pass


def setup_logging():
    print("Setting up logging")
    if not os.path.isdir("logs"):
        os.makedirs('logs')

    formatter = logging.Formatter("[%(asctime)s] %(message)s")

    handler_info = TimedRotatingFileHandler(
        './logs/info.log', when='midnight', interval=1, backupCount=5)
    handler_info.setLevel(logging.INFO)
    handler_info.setFormatter(formatter)

    handler_error = TimedRotatingFileHandler(
        './logs/error.log', when='midnight', interval=1, backupCount=5)
    handler_error.setLevel(logging.ERROR)
    handler_error.setFormatter(formatter)

    # access log
    logger = logging.getLogger('werkzeug')
    handler_access = logging.FileHandler('./logs/access.log')

    flask_app.logger.addHandler(handler_info)
    flask_app.logger.addHandler(handler_error)
    logger.addHandler(handler_access)


def get_register_blueprints():
    # Public API
    from app.receipt.views import mod_receipt

    # API Blueprints
    return [
        mod_receipt
    ]


"""
DEFINE DB
"""
setup_db()


"""
BLUEPRINT REGISTER
"""
[flask_app.register_blueprint(blueprint)
 for blueprint in get_register_blueprints()]

# production = os.environ.get('PRODUCTION', False)
# if production:
#     setup_logging()
