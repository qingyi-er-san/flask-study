# 蓝图
from flask import Blueprint

blue = Blueprint('user',__name__)


@blue.route('/')
def index():
    return 'index'


