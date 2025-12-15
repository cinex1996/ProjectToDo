from flask import Blueprint

bp = Blueprint("posts",__name__,"../../templates")
from . import create_post