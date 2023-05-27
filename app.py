from flask import Flask
from app.transactions import transactions_blueprint

app = Flask(__name__)
app.register_blueprint(transactions_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
