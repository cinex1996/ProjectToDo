from flask import Blueprint

bp = Blueprint("posts",__name__,template_folder="../../templates")
from . import create_post
from . import delete_post
from .edit import edit_post