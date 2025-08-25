from flask import Blueprint

api_bp = Blueprint('api', __name__)

from . import login
from . import user
from . import like
from . import cart
from . import review
from . import buy
from . import comment