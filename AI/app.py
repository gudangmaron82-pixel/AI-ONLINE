from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
memory_file = "data/memory.json"

# Pastikan folder data dan file memory ada
os.makedirs("data", exist_ok=True)
if not os.path.exists(memory_file):
    with open(memory_file, "w") as f:
        json.dump({}, f)

# Fungsi baca memory
def load_memory():
    with open(memory_file, "r") as f:
        return json.load(f)

# Fungsi tulis memory
def save_memory(memory):
    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=4)

@app.route("/")
def home():
    return "AI Multifungsi siap dijalankan!"

@app.route("/perintah", methods=["POST"])
def perintah():
    data = request.json
    if not data or "command" not in data:
        return jsonify({"error": "Tidak ada perintah"}), 400

    command = data["command"].lower()
    memory = load_memory()

    # Jika perintah sudah pernah ada, balas sesuai memory
    if command in memory:
        response = memory[command]
    else:
        # Jika baru, AI "belajar" dan balas default
        response = f"Perintah diterima: {command}"
        memory[command] = response
        save_memory(memory)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)