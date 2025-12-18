from flask import Blueprint
bp = Blueprint("search",__name__,template_folder="../../templates")
from . import search_user