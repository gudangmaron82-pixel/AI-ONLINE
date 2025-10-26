from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

def ai_reply(user_input):
    user_input = user_input.lower()
    if "halo" in user_input:
        return "Halo juga! Saya AI online buatan Fahlevi & PG."
    elif "nama" in user_input:
        return "Saya AI sederhana, bisa belajar dari perintah kamu."
    elif "waktu" in user_input:
        return "Sekarang jam " + datetime.datetime.now().strftime("%H:%M")
    else:
        with open("model.txt", "a", encoding="utf-8") as f:
            f.write(user_input + "\n")
        return "Saya belum tahu tentang itu, tapi sudah saya catat."

@app.route("/", methods=["GET"])
def home():
    return "AI Fahlevi & PG aktif online ✅"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("msg", "")
    return jsonify({"reply": ai_reply(user_input)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)