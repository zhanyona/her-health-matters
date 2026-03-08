import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# ============================================
# 1. СОЗДАНИЕ APP (ЭТО ВАЖНО!)
# ============================================
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app, origins='*')

# ============================================
# 2. МАРШРУТЫ (ROUTES)
# ============================================

# Главная страница - отдает chat.html
@app.route('/')
def serve_chat():
    return send_from_directory('.', 'chat.html')

# Проверка здоровья API
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'her health matters ai is running ✨'
    })

# ============================================
# 3. AI КЛАСС
# ============================================
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
• dark chocolate (70%+ cocoa)

🕊️ **see a doctor if:**
• pain stops you from daily activities
• pain between periods too"""
        
        elif 'tired' in message or 'fatigue' in message:
            return """⚡ **understanding fatigue**

🫧 **iron & periods:**
• heavy periods can cause low iron
• eat spinach, red meat, lentils

😴 **sleep tips:**
• same bedtime every night
• no phones 1 hour before bed
• no caffeine after 2pm

🧠 **stress:**
• try meditation, gentle movement"""
        
        elif 'irregular' in message or 'cycle' in message:
            return """🌊 **understanding your cycle**

🌸 **what's normal:**
• cycle length: 21 to 35 days
• period: 3 to 7 days

🦋 **common causes:**
• stress
• age (teens or approaching 40s)
• weight changes

🕊️ **see a doctor if:**
• no period for 3+ months
• bleeding between periods"""
        
        elif 'pms' in message or 'mood' in message:
            return """🌙 **understanding pms**

😢 **emotional symptoms:**
• irritability
• mood swings
• anxiety

🫧 **physical symptoms:**
• bloating
• breast tenderness
• food cravings

🌸 **what helps:**
• 30 min walking daily
• reduce salt and caffeine
• track your cycle"""
        
        else:
            return """🌸 **i'm here to help!**

ask me about:
• period pain and cramps
• irregular cycles
• fatigue and low energy
• pms and mood swings
• sleep problems
• skin issues

what's on your mind today? 💕"""

# Создаем экземпляр AI
ai = WomenHealthAI()

# ============================================
# 4. ЧАТ ENDPOINT
# ============================================
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