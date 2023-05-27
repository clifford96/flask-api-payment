from flask import Blueprint

transactions_blueprint = Blueprint('transactions', __name__, url_prefix='/api')

from . import transactions
