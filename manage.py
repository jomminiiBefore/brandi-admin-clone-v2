from flask_script   import Server
from app            import create_app

if __name__ == "__main__":
    app = create_app()
    server = Server(host="0.0.0.0", port = 5000)

    app.run()