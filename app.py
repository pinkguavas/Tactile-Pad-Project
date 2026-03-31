from flask import Flask, render_template, request, jsonify
from braille import translate_text
from fake_board import send_to_board, reset_board, clear_board

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/display", methods=["POST"])
def display():
    data = request.get_json()
    text = data.get("text", "")

    patterns = translate_text(text)
    send_to_board(patterns)

    return jsonify({
        "status": "ok",
        "text": text,
        "patterns": patterns
    })

@app.route("/reset", methods=["POST"])
def reset():
    reset_board()
    return jsonify({"status": "reset"})

@app.route("/clear", methods=["POST"])
def clear():
    clear_board()
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(debug=True)