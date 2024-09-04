from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.json  # Get JSON data from the request
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Process the data here
    print('Received data:', data)

    # Respond with a success message
    return jsonify({'message': 'Data received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
