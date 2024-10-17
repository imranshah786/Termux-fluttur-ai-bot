from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Yahan pe data ko process karen
    print("Received data:", data)
    response = {
        "status": "success",
        "message": "Data received successfully!"
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5000)  # Server ko 5000 port par run karna
