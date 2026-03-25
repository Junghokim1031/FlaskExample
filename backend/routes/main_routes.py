from flask import Blueprint
from backend.model.db import Database

# 중앙 DB 인스턴스 초기화
db_instance = Database()

# 부모 블루프린트 생성
main_routes = Blueprint('main', __name__)

# 자식 블루프린트 등록
from .index import index_bp
from .calculate import calculate_bp
from .history import history_bp

main_routes.register_blueprint(index_bp)
main_routes.register_blueprint(calculate_bp)
main_routes.register_blueprint(history_bp)
