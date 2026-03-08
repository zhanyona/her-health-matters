import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app, origins='*')

@app.route('/')
def serve_chat():
    return send_from_directory('.', 'chat.html')

@app.route('/chat.html')
def serve_chat_file():
    return send_from_directory('.', 'chat.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'her health matters ai is running ✨',
        'version': '3.0 - public server'
    })

class WomenHealthAI:
    def get_response(self, message):
        message = message.lower()
        
        if 'cramp' in message or 'pain' in message:
            return """🌸 **period pain relief**

🫧 **immediate relief:**
• heating pad on lower belly for 15-20 minutes
• warm bath with epsom salts
• gentle walking or stretching
• ibuprofen (take with food)

🌿 **natural remedies:**
• ginger tea
• raspberry leaf tea
• dark chocolate (70%+ cocoa)

🕊️ **see a doctor if:**
• pain stops you from daily activities
• pain suddenly gets worse
• pain between periods too"""
        
        elif 'tired' in message or 'fatigue' in message:
            return """⚡ **understanding fatigue**

🫧 **iron & periods:**
• heavy periods can cause low iron
• eat spinach, red meat, lentils
• add vitamin C (orange juice) to help absorption

😴 **sleep tips:**
• same bedtime every night
• no phones 1 hour before bed
• cool, dark room
• no caffeine after 2pm

🧠 **stress:**
• stress hormones exhaust your body
• try meditation, gentle movement, talking to someone"""
        
        elif 'irregular' in message or 'cycle' in message:
            return """🌊 **understanding your cycle**

🌸 **what's normal:**
• cycle length: 21 to 35 days
• period: 3 to 7 days
• variation up to 7-9 days is normal

🦋 **common causes:**
• stress
• age (teens or approaching 40s)
• weight changes
• intense exercise

🕊️ **see a doctor if:**
• no period for 3+ months
• cycles shorter than 21 or longer than 35 days
• bleeding between periods"""
        
        elif 'pms' in message or 'mood' in message:
            return """🌙 **understanding pms**

😢 **emotional symptoms:**
• irritability
• mood swings
• sadness or crying
• anxiety

🫧 **physical symptoms:**
• bloating
• breast tenderness
• food cravings
• fatigue

🌸 **what helps:**
• 30 min walking daily
• reduce salt and caffeine
• calcium supplements (ask doctor first)
• track your cycle to prepare"""
        
        else:
            return """🌸 **i'm here to help!**

ask me about:
• period pain and cramps
• irregular cycles
• fatigue and low energy
• pms and mood swings
• headaches
• sleep problems
• skin issues

what's on your mind today? 💕"""

ai = WomenHealthAI()

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        response = ai.get_response(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port,debug=False)