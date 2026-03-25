from flask import Flask
import logging
from app.routes import customer_bp
from config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def main():
    app = Flask(__name__)

    app.register_blueprint(customer_bp)
    logger.info("Mock Server initialized with customer routes")
    return app

app = main()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
