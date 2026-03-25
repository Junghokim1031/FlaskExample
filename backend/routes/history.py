from flask import Blueprint, render_template
from .main_routes import db_instance as db

history_bp = Blueprint('history', __name__)

@history_bp.route('/history')
def history():
    # 최근 BMI 기록 10개 가져오기
    records = db.get_bmi_records(10)
    return render_template('history.html', records=records)
