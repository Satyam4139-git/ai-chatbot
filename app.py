from flask import (Flask,
                   render_template,
                   request,
                   jsonify)
from chatbot import (get_chatbot_response,
                     clear_history)
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({
                "error": "No message provided"
            }), 400

        bot_response = get_chatbot_response(
            user_message
        )

        return jsonify({
            "response": bot_response,
            "status": "success"
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

@app.route("/clear", methods=["POST"])
def clear():
    message = clear_history()
    return jsonify({"message": message})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=False,
            host="0.0.0.0",
            port=port)