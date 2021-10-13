from flask_login import LoginManager, login_manager
from app_with_login.models import User


login_manager = LoginManager()

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

def init_app(app):
    login_manager.init_app(app)