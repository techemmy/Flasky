from flask import Blueprint
from flask_login import current_user

from ..models import Permission

main = Blueprint('main', __name__)


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

@main.app_context_processor
def inject_user_objetct():
    return dict(user=current_user)


from . import views, errors
