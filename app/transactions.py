from flask import Blueprint, jsonify, request
from . import transactions_blueprint

transactions = []

@transactions_blueprint.route('/merchant/transactions/id', methods=['GET'])
def get_transactions():
    return jsonify(transactions)

@transactions_blueprint.route('/merchant/transactions/id', methods=['POST'])
def create_transaction():
    data = request.get_json()
    # Process the transaction data and save it
    transaction = {
        'amount': data['amount'],
        'currency': data['currency'],
        'description': data['description']
    }
    transactions.append(transaction)
    # Return the response
    return jsonify({
        'message': 'Transaction created',
        'transaction_id': len(transactions),
        'amount': transaction['amount'],
        'currency': transaction['currency'],
        'description': transaction['description']
    }), 201

@transactions_blueprint.route('/merchant/transactions', methods=['POST'])
def query_transaction():
    data = request.get_json()
    query = data['query']
    
    if query == 'I would like to request for the most recent transaction':
        if len(transactions) > 0:
            recent_transaction = transactions[-1]
            return jsonify(recent_transaction)
        else:
            return jsonify({'message': 'No transactions found.'}), 404
    
    # Handle other types of queries if needed
    
    return jsonify({'message': 'Invalid query.'}), 400

@transactions_blueprint.route('/bank/request', methods=['GET'])
def bank_request():
    data = request.get_json()
    query = data['query']

    if 'check' in query.lower() and ('transaction' in query.lower() or 'payment' in query.lower()):
        return jsonify({
            'message': 'Please provide IC for verification'
        })
    else:
        return jsonify({
            'message': 'Invalid query'
        }), 400

@transactions_blueprint.route('/bank/verification', methods=['POST'])
def verify_transaction():
    data = request.get_json()
    verification_input = data['identity']
    
    if len(verification_input) == 12 and verification_input.isdigit():
        return jsonify({'message': 'Verification approved. Please provide the Transaction ID'}), 200
    else:
        return jsonify({'message': 'Invalid verification code. Expected 12-digit number.'}), 400


@transactions_blueprint.route('/bank/transactions', methods=['POST'])
def check_transaction():
    transaction_id = request.json.get('transaction_id')

    if transaction_id and transaction_id.isdigit():
        return jsonify({'message': 'Transaction was successful'})
    else:
        return jsonify({'message': 'Invalid transaction ID.'}), 404
