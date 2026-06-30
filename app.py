from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Server ka naam aur deployment details
SERVER_NAME = "Satyam Pandey"
DEPLOYED_BY = "Satyam Pandey"

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "server_name": SERVER_NAME,
        "status": "Running successfully",
        "deployed_by": DEPLOYED_BY,
        "message": "Welcome to the Name-Hiding Messenger Server!"
    })

@app.route('/webhook', methods=['POST'])
def hide_name_webhook():
    """
    Ye endpoint messenger group ke messages receive karega 
    aur sender ka naam hide karke group me forward karne ke liye data process karega.
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data received"}), 400

    # Example: Agar message me 'sender_name' aur 'text' aa raha hai
    original_sender = data.get('sender_name', 'Unknown')
    message_text = data.get('text', '')

    # Naam hide karne ka logic (Sabko 'Anonymous' ya 'Group Member' dikhega)
    hidden_sender = "Anonymous Member"
    
    # Aapka processed data jo aage forward hoga
    processed_message = {
        "sender_name": hidden_sender,
        "text": message_text,
        "info": f"Processed secure by Server: {SERVER_NAME}"
    }

    # Yahan aap apna bot/messenger forward logic add kar sakte hain
    
    return jsonify({
        "status": "Success",
        "data": processed_message,
        "deployed_by": DEPLOYED_BY
    }), 200

if __name__ == '__main__':
    # Render port automatically assign karta hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
