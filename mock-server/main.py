from flask import Flask

from app.routes import customer_bp

def main():
    app = Flask(__name__)

    app.register_blueprint(customer_bp)
    return app

app = main()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
