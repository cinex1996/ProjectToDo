from flask import Blueprint

bp = Blueprint("reset", __name__, template_folder="../../templates")

from . import reset_password