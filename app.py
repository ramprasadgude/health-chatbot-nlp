from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from translator import translate
from tts import speak_text

app = Flask(__name__)

# 🏠 Home route
@app.route("/")
def home():
    return render_template("index.html")

# 💬 Chat route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        user_input = data.get("message")
        lang = data.get("lang", "en")

        if not user_input:
            return jsonify({"response": "⚠️ No message received"})

        # 🌍 Step 1: Translate user input → English (SAFE)
        try:
            english_input = translate(user_input, "en")
        except:
            english_input = user_input

        # 🧠 Step 2: Get chatbot response
        response = get_response(english_input)

        # 🌍 Step 3: Translate back to selected language (SAFE)
        try:
            final_response = translate(response, lang)
        except Exception as e:
            print("Translation Error:", e)
            final_response = response

        # 🔊 Step 4: Convert response to voice (SAFE)
        try:
            audio = speak_text(final_response, lang)
        except Exception as e:
            print("TTS Error:", e)
            audio = None

        return jsonify({
            "response": final_response,
            "audio": audio
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "response": "⚠️ Server error. Check terminal."
        })

# 🗑️ Clear Chat Route
@app.route("/clear", methods=["POST"])
def clear_chat():
    from chatbot import clear_memory
    clear_memory()
    return jsonify({"status": "success"})

# 🚀 Run server
if __name__ == "__main__":
    app.run(debug=True)