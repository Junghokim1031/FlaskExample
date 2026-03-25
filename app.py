import os
from flask import Flask
from backend.model.config import Config
from backend.routes.main_routes import main_routes, db_instance as db
import atexit


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # 부모 블루프린트
    app.register_blueprint(main_routes)

    # DB 종료 예약
    if hasattr(db, 'close'):
        atexit.register(db.close)
        
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)