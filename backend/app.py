from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status')
def get_status():
    return jsonify({
        "status": "Online",
        "message": "Hello from Python Backend on VM 2",
        "location": "Internal VPC"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
