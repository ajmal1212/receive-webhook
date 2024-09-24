from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def html():
    return render_template("index.html")

@app.route("/webhook", methods=['POST'])
def hook():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        
        # Print received webhook data
        print("Received webhook data:", data)
        
        # You should return a response to confirm receipt of the webhook
        return jsonify({"status": "success", "message": "Webhook received"}), 200
    else:
        error_message = "Content-Type not supported!"
        print(f"Unsupported Content-Type: {request.headers['Content-Type']}")
        return jsonify({"status": "error", "message": error_message}), 415  # Return an error for unsupported Content-Type

if __name__ == "__main__":
    app.run(debug=True)
