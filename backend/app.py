from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'Welcome to the AI Waifu API!'}), 200

@app.route('/api/waifu', methods=['GET'])
def get_waifu():
    # This would normally fetch a waifu from a database or a list
    waifu = {'name': 'Rem', 'series': 'Re:Zero Starting Life in Another World'}
    return jsonify(waifu), 200

@app.route('/api/waifu', methods=['POST'])
def create_waifu():
    data = request.get_json()
    return jsonify({'message': 'Waifu created!', 'data': data}), 201

if __name__ == '__main__':
    app.run(debug=True)
