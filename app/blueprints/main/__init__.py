from flask import Blueprint

bp = Blueprint("main", __name__, template_folder="../../templates")  # ← OBIEKT, nie funkcja

from . import  homepage,index