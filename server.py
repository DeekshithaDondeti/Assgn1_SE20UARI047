from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/api/messages', methods=['POST'])
def receive_message():
    data = request.json
    message = data.get('message', '')
    print(f"Received message: {message}")
    return jsonify({"status": "Message received!"})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
