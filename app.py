from flask import Flask, send_from_directory, request, jsonify
import json
import os

app = Flask(__name__)

# Serve static files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# API endpoints for attendance data
@app.route('/api/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        data = request.get_json()
        # Save to a file or database
        with open('attendance.json', 'w') as f:
            json.dump(data, f)
        return jsonify({'status': 'saved'})
    else:
        if os.path.exists('attendance.json'):
            with open('attendance.json', 'r') as f:
                data = json.load(f)
            return jsonify(data)
        return jsonify({})

from flask import Flask, send_from_directory, request, jsonify
import json
import os

app = Flask(__name__)

# Serve static files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# API endpoints for attendance data
@app.route('/api/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        data = request.get_json()
        # Save to a file or database
        with open('attendance.json', 'w') as f:
            json.dump(data, f)
        return jsonify({'status': 'saved'})
    else:
        if os.path.exists('attendance.json'):
            with open('attendance.json', 'r') as f:
                data = json.load(f)
            return jsonify(data)
        return jsonify({})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)