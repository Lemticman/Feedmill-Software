from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')

# In-memory storage for testing
inventory_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory_data)

@app.route('/api/inventory', methods=['POST'])
def add_inventory():
    data = request.json
    data['timestamp'] = datetime.now().isoformat()
    inventory_data.append(data)
    return jsonify({'status': 'success'}), 201

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT"])
    app.run(host="0.0.0.0", port=port)

