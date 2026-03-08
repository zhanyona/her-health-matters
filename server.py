import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Создание приложения
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app, origins='*')

# Главная страница
@app.route('/')
def serve_chat():
    return send_from_directory('.', 'chat.html')

# Проверка здоровья
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'her health matters ai is running ✨'
    })

# AI класс
class WomenHealthAI:
    def get_response(self, message):
        message = message.lower()
        
        if 'cramp' in message or 'pain' in message:
            return """🌸 **period pain relief**

🫧 **immediate relief:**
• heating pad on lower belly
• warm bath with epsom salts
• ibuprofen (take with food)

🕊️ **see a doctor if:**
• pain stops daily activities"""
        
        elif 'tired' in message or 'fatigue' in message:
            return """⚡ **understanding fatigue**

🫧 **iron & periods:**
• eat spinach, red meat, lentils

😴 **sleep tips:**
• same bedtime every night
• no phones before bed"""
        
        elif 'irregular' in message or 'cycle' in message:
            return """🌊 **understanding your cycle**

🌸 **what's normal:**
• cycle: 21 to 35 days
• period: 3 to 7 days

🕊️ **see a doctor if:**
• no period for 3+ months"""
        
        else:
            return """🌸 **i'm here to help!**

ask me about:
• period pain
• irregular cycles
• fatigue
• mood swings

what's on your mind? 💕"""

ai = WomenHealthAI()

# Чат endpoint
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'No message'}), 400
        
        response = ai.get_response(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ВАЖНО: Этот блок ЗАПУСКАЕТ сервер через waitress
if __name__ == '__main__':
    from waitress import serve
    port = int(os.environ.get('PORT', 10000))
    print(f"Starting server on port {port}")
    serve(app, host='0.0.0.0', port=port)