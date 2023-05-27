from flask import Blueprint, jsonify, request
from . import transactions_blueprint

transactions = []

@transactions_blueprint.route('/merchant/transactions', methods=['GET'])
def query_transaction():
    custId = request.args.get('custId')
    record = request.args.get('record')

    if custId and custId.isdigit():
        if record == 'latest':

            return jsonify({
                    'message': 'Transaction found',
                    'mercTransId':'9999999',
                    'bankTxnId':'9999999',
                    'transDt': '2023/05/28',
                    'mercOrderId':'6060606',
                    'paymentAmt': 1000,
                    'paymentCur': 'MYR'
    }), 201
        else:

            return jsonify({'message': 'Invalid query.'}),400


@transactions_blueprint.route('/bank/transaction/verification', methods=['POST'])
def verify_transaction():
    verification_input = request.args.get['ic']
    
    if len(verification_input) == 12 and verification_input.isdigit():
        return jsonify({'message': 'Verification approved.',
                        'hash' : '8u7fc503953909637f78hg8c99b3b85ddde362418985afc11901bdefe8349102' }), 200
    else:
        return jsonify({'message': 'Invalid verification code. Expected 12-digit number.'}), 400


@transactions_blueprint.route('/bank/transactions/status', methods=['GET'])
def check_transaction():    
    bankTxnId = request.args.get('bankTxnId')
    hash = request.args.get('hash')

    if bankTxnId and hash:

        return jsonify({
                    'status': 'Transaction successful'
    }), 201
    else:

        return jsonify({'message': 'Invalid query.'}),400