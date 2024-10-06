# ------------------------------------------------------------------------------------------------------------

from flask import Blueprint, request, jsonify
from flask_cors import CORS  # Import CORS
from models.extendible_hashing import extendible_hasher  # Import your extendible hash instance
from models.linear_hashing import linear_hasher  # Import your linear hash instance
import logging

# Create a Blueprint for the routes
routes_app = Blueprint('routes', __name__)
CORS(routes_app)  # Enable CORS for this Blueprint

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Extendible Hashing Routes
@routes_app.route('/extendible/insert', methods=['POST'])
def extendible_insert():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')

    if key is None or value is None:
        return jsonify({'error': 'Key and Value must be provided for insertion.'}), 400

    extendible_hasher.insert(key, value)

    return jsonify({
        'message': f'Inserted ({key}, {value}) successfully.',
        'state': extendible_hasher.statistics()
    }), 201

@routes_app.route('/extendible/delete', methods=['DELETE'])
def extendible_delete():
    data = request.get_json()
    key = data.get('key')

    if key is None:
        return jsonify({'error': 'Key must be provided for deletion.'}), 400

    extendible_hasher.delete(key)

    return jsonify({
        'message': f'Deleted key {key} successfully.',
        'state': extendible_hasher.statistics()
    }), 200

@routes_app.route('/extendible/search', methods=['GET'])
def extendible_search():
    key = request.args.get('key')

    if key is None:
        return jsonify({'error': 'Key must be provided for search.'}), 400

    result = extendible_hasher.search(int(key))
    if result is None:
        return jsonify({
            'message': f'Key {key} not found.'
        }), 404
    return jsonify({
        'message': f'Found key {key}: {result}',
        'state': extendible_hasher.statistics()
    }), 200

@routes_app.route('/extendible/statistics', methods=['GET'])
def extendible_statistics():
    stats = extendible_hasher.statistics()
    logging.info("Statistics retrieved for extendible hash.")
    return jsonify(stats), 200  # Respond with statistics

# Linear Hashing Routes
@routes_app.route('/linear/insert', methods=['POST'])
# def linear_insert():
#     data = request.get_json()
#     key = data.get('key')
#     value = data.get('value')
    
#     if key is None or value is None:
#         return jsonify({'error': 'Key and Value must be provided for insertion.'}), 400

#     linear_hasher.insert(key, value)
    
#     return jsonify({
#         'message': f'Inserted ({key}, {value}) successfully.',
#         'state': linear_hasher.statistics()
#     }), 201
def insert():
    data = request.get_json()  # Get the JSON data from the request
    key = data.get('key')       # Extract the key
    value = data.get('value')   # Extract the value

    if key is None or value is None:
        return jsonify({'error': 'Key and Value must be provided'}), 400

    print("Insert function called")  # Debug print statement
    logging.info(f'Attempting to insert key: {key}, value: {value}')  # Log attempt

    linear_hasher.insert(key, value)  # Insert the key-value pair

    # Log the successful insertion
    logging.info(f'Inserted key: {key}, value: {value}')
    print(f'Inserted key: {key}, value: {value}')  # Debug print for confirmation

    return jsonify({
        'message': 'Inserted successfully',
        'inserted': {
            'key': key,
            'value': value
        },
        'state': linear_hasher.statistics()  # Include the current state
    }), 201


@routes_app.route('/linear/delete', methods=['DELETE'])
def linear_delete():
    data = request.get_json()
    key = data.get('key')
    
    if key is None:
        return jsonify({'error': 'Key must be provided for deletion.'}), 400

    linear_hasher.delete(key)

    return jsonify({
        'message': f'Deleted key {key} successfully.',
        'state': linear_hasher.statistics()
    }), 200

@routes_app.route('/linear/search', methods=['GET'])
def linear_search():
    key = request.args.get('key')
    
    if key is None:
        return jsonify({'error': 'Key must be provided for search.'}), 400

    result = linear_hasher.search(int(key))
    if result is None:
        return jsonify({
            'message': f'Key {key} not found.'
        }), 404
    return jsonify({
        'message': f'Found key {key}: {result}',
        'state': linear_hasher.statistics()
    }), 200

@routes_app.route('/linear/statistics', methods=['GET'])
def linear_statistics():
    stats = linear_hasher.statistics()
    logging.info("Statistics retrieved for linear hash.")
    return jsonify(stats), 200  # Respond with statistics
