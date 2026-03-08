import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import re

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app, origins='*')

@app.route('/')
def serve_chat():
    return send_from_directory('.', 'chat.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'her health matters ai is running ✨',
        'version': '4.0 - smart ai'
    })

class SmartWomenHealthAI:
    def __init__(self):
        self.conversation_history = []
    
    def get_response(self, message):
        """Main method to get AI response"""
        message_lower = message.lower()
        
        # Store in history
        self.conversation_history.append(message)
        
        # Check for different topics
        if any(word in message_lower for word in ['period', 'menstrual', 'cycle', 'monthly']):
            return self.answer_period_questions(message)
        
        elif any(word in message_lower for word in ['cramp', 'pain', 'hurt', 'ache']):
            return self.answer_pain_questions(message)
        
        elif any(word in message_lower for word in ['tired', 'fatigue', 'exhausted', 'energy']):
            return self.answer_fatigue_questions(message)
        
        elif any(word in message_lower for word in ['pms', 'mood', 'emotional', 'cry', 'sad', 'anxious']):
            return self.answer_mood_questions(message)
        
        elif any(word in message_lower for word in ['irregular', 'late', 'missed', 'early']):
            return self.answer_cycle_questions(message)
        
        elif any(word in message_lower for word in ['headache', 'migraine', 'head hurts']):
            return self.answer_headache_questions(message)
        
        elif any(word in message_lower for word in ['sleep', 'insomnia', 'can\'t sleep']):
            return self.answer_sleep_questions(message)
        
        elif any(word in message_lower for word in ['skin', 'acne', 'breakout', 'pimple']):
            return self.answer_skin_questions(message)
        
        elif any(word in message_lower for word in ['weight', 'gain', 'lose', 'appetite']):
            return self.answer_weight_questions(message)
        
        elif any(word in message_lower for word in ['doctor', 'gyno', 'specialist', 'should i see']):
            return self.answer_doctor_questions(message)
        
        else:
            return self.answer_general(message)
    
    def answer_period_questions(self, question):
        return """🌸 **understanding your period**

A period is when your body sheds the lining of your uterus. This happens about once a month if you're not pregnant.

**what's normal:**
• Cycle length: 21 to 35 days (28 days is average)
• Period length: 3 to 7 days
• Flow: light to heavy, possible small clots
• Color: bright red to dark brown is normal

**what happens in your body:**
Your hormones (estrogen and progesterone) rise and fall throughout the month. When they drop at the end of your cycle, your uterine lining sheds - that's your period!

**common symptoms (normal):**
• Mild cramping
• Bloating
• Breast tenderness
• Fatigue
• Mood changes
• Food cravings

**when to see a doctor:**
• Periods suddenly become very painful
• You're soaking through a pad/tampon every 1-2 hours
• Periods less than 21 days or more than 35 days apart
• Bleeding between periods
• No period for 3+ months (and not pregnant)

what specifically would you like to know about your period? 💕"""
    
    def answer_pain_questions(self, question):
        if 'cramp' in question.lower():
            return """🩹 **understanding period cramps**

period cramps (dysmenorrhea) happen because your uterus contracts to shed its lining. these contractions are triggered by chemicals called prostaglandins - more prostaglandins = more pain.

**why some women have worse cramps:**
• higher prostaglandin levels
• endometriosis (tissue grows outside uterus)
• fibroids (benign growths)
• pelvic inflammatory disease
• stress (makes pain feel worse)

**immediate relief:**
• 🔥 **heat therapy:** heating pad or hot water bottle on lower belly for 15-20 minutes (works as well as ibuprofen!)
• 💊 **medication:** ibuprofen or naproxen work best because they reduce prostaglandins. take with food!
• 🧘 **gentle movement:** light walking, stretching, child's pose in yoga
• 🛁 **warm bath:** add epsom salts for muscle relaxation
• ☕ **herbal tea:** ginger, chamomile, or raspberry leaf tea

**natural remedies (ask doctor first):**
• magnesium - helps muscles relax
• vitamin B1 - studies show it helps
• omega-3 fatty acids (fish oil) - anti-inflammatory
• acupressure or acupuncture

**foods that help:**
• anti-inflammatory foods: berries, nuts, leafy greens
• warm foods: soups, warm oatmeal
• dark chocolate (magnesium + mood boost!)
• bananas (potassium helps with cramping)
• ginger (add to tea or meals)

**foods to avoid before/during period:**
• salty foods (increase bloating)
• caffeine (can increase tension)
• sugary foods (cause energy crashes)
• processed foods

**when to see a doctor:**
• pain stops you from going to school/work
• over-the-counter meds don't help at all
• pain suddenly gets worse than usual
• you're over 25 and pain is new/getting worse
• pain between periods too
• heavy bleeding with clots

**possible conditions:**
• **endometriosis** - tissue similar to uterine lining grows outside the uterus
• **fibroids** - non-cancerous growths
• **adenomyosis** - tissue grows into uterine wall
• **pelvic inflammatory disease** - infection

what's your pain like? tell me more and i'll help you figure it out 💕"""
        
        else:
            return """🩹 **understanding pain**

pain is your body's way of telling you something needs attention.

**types of pain common in women:**

• **cramping pain** - usually period-related, in lower belly
• **headaches/migraines** - can be hormonal
• **breast pain** - often before period
• **back pain** - can be period-related or from posture
• **pelvic pain** - needs medical attention

**track your pain:**
write down:
• when it happens (before/during/after period?)
• where exactly it hurts
• what it feels like (sharp, dull, throbbing)
• what makes it better/worse
• how long it lasts

this information is SO helpful for doctors!

**red flags (see a doctor):**
• sudden severe pain
• pain with fever
• pain after injury
• pain that wakes you at night
• pain lasting more than a few days

what kind of pain are you experiencing? 🌸"""
    
    def answer_fatigue_questions(self, question):
        return """⚡ **understanding fatigue**

feeling tired all the time is SO common, but let's figure out why YOU might be exhausted:

**common causes in women:**

🩸 **iron deficiency / anemia**
• very common with heavy periods
• symptoms: pale skin, cold hands/feet, dizziness, brittle nails
• iron-rich foods: red meat, spinach, lentils, beans, fortified cereals
• tip: eat with vitamin C (orange juice) to help absorption

😴 **poor sleep quality**
• not just hours, but how well you sleep
• sleep hygiene tips:
  - same bedtime/wake time (even weekends!)
  - no phones 1 hour before bed (blue light disrupts melatonin)
  - cool, dark, quiet room
  - no caffeine after 2pm
  - limit alcohol (it ruins sleep quality)

🧠 **stress and mental health**
• stress hormones (cortisol) exhaust your body
• anxiety and depression both cause fatigue
• helpful: therapy, meditation, time in nature, talking to friends

⚡ **thyroid issues**
• very common in women!
• hypothyroidism causes fatigue, weight gain, feeling cold
• simple blood test can check this

🥗 **nutrition deficiencies**
• vitamin D deficiency (very common!)
• vitamin B12 deficiency (more common in vegetarians)
• magnesium deficiency

💧 **dehydration**
• even mild dehydration causes fatigue
• aim for 8 glasses of water daily

**energy-boosting tips:**
• gentle movement (walking actually BOOSTS energy)
• protein with every meal
• don't skip breakfast
• short power naps (10-20 min)
• sunlight exposure in morning

**when to see a doctor:**
• fatigue lasting more than 2 weeks
• fatigue with unexplained weight changes
• feeling cold all the time
• shortness of breath
• racing heart
• depression symptoms

what does YOUR fatigue feel like? when did it start? 💫"""
    
    def answer_mood_questions(self, question):
        return """😢 **understanding mood and emotions**

your feelings are valid, and they're often connected to what's happening in your body:

**hormones and mood:**

🌸 **estrogen:**
• boosts serotonin (your 'feel-good' chemical)
• higher in first half of cycle = usually better mood
• drops before period = can affect mood

🌙 **progesterone:**
• rises after ovulation
• can cause fatigue, mood changes
• drops sharply before period

**common patterns:**

**before period (pms):**
• irritability
• sadness
• anxiety
• feeling overwhelmed
• crying easily
• this is REAL and affects up to 75% of women!

**during period:**
• relief as hormones balance
• some feel low from physical discomfort

**pms vs pmdd:**

**pms (premenstrual syndrome):**
• mild to moderate symptoms
• doesn't severely impact daily life
• affects up to 75% of women

**pmdd (premenstrual dysphoric disorder):**
• severe symptoms
• affects daily life and relationships
• intense depression, anger, anxiety
• affects 3-8% of women
• treatable with medical help!

**what helps:**

🟢 **for cycle-related mood:**
• track your cycle - knowing "this is pms" helps
• be extra kind to yourself during luteal phase
• reduce commitments if possible
• exercise (even just walking helps!)
• avoid alcohol (it's a depressant)
• eat complex carbs (help stabilize mood)

🟢 **supplements (ask doctor first):**
• calcium - studies show it significantly reduces pms
• magnesium - helps with mood and bloating
• vitamin B6 - helps with mood symptoms

🟢 **lifestyle:**
• prioritize sleep
• time in nature
• creative expression
• talk to someone you trust

**when to see a doctor:**
• mood affecting daily life for 2+ weeks
• can't get out of bed
• loss of interest in things you loved
• changes in appetite or sleep
• thoughts of self-harm

**crisis support (if you're in the US):**
• call 988 (suicide & crisis lifeline)
• text HOME to 741741
• go to emergency room
• tell someone you trust

**remember:** mental health is health. you deserve support. 🤍

how have YOU been feeling? i'm here to listen."""
    
    def answer_cycle_questions(self, question):
        return """🌊 **understanding your menstrual cycle**

let's talk about what "irregular" actually means:

**normal cycle:**
• length: 21 to 35 days
• period: 3 to 7 days
• variation: up to 7-9 days difference is still normal

**what causes irregular periods:**

🟢 **common and usually not serious:**
• **age:** first 2-3 years after first period (teenagers)
• **age:** perimenopause (40s and 50s)
• **stress:** high stress affects hormones
• **travel:** jet lag can temporarily affect cycle
• **illness:** getting sick can delay period
• **weight changes:** significant loss or gain
• **exercise:** very intense training (common in athletes)

🟡 **may need medical attention:**

**pcos (polycystic ovary syndrome):**
• very common (affects 1 in 10 women)
• symptoms: irregular periods, acne, weight gain, excess hair
• manageable with lifestyle and medication

**thyroid issues:**
• both overactive and underactive thyroid affect periods
• symptoms: fatigue, weight changes, temperature sensitivity
• simple blood test can diagnose

**high prolactin:**
• can be caused by stress, medication, or small tumor
• symptoms: irregular periods, milky discharge

**birth control:**
• hormonal iud or progestin-only methods can make periods irregular or stop them

**when to see a doctor:**
• no period for 3+ months
• cycles consistently shorter than 21 days or longer than 35 days
• bleeding between periods
• severe pain with irregular cycles
• trying to get pregnant and cycles are irregular
• other symptoms like acne, weight changes, excess hair

**track your cycle!**
use an app or calendar to track:
• when period starts and ends
• how heavy the flow is
• any symptoms (pain, mood changes)
• this information is GOLD for your doctor

what's your specific situation? how old are you, and what does "irregular" mean for you? 🌸"""
    
    def answer_headache_questions(self, question):
        return """🤕 **understanding headaches**

headaches are super common, especially in women. let's figure out what kind you might have:

**types of headaches:**

🤕 **tension headaches:**
• feels like a tight band around your head
• dull, aching pain
• often from stress, poor posture, eye strain
• usually both sides of head
• **helps:** heat on neck/shoulders, gentle stretching, massage, check your posture

⚡ **migraines:**
• throbbing pain, often one side
• nausea, sensitivity to light/sound
• can last hours to days
• sometimes preceded by "aura" (visual disturbances)
• **helps:** rest in dark quiet room, cold compress on forehead, hydration, identify triggers

🔄 **hormonal headaches:**
• happen right before or during period
• from drop in estrogen
• can be migraine-like or tension-type
• **helps:** track with cycle, magnesium supplements might help prevent them

**common triggers:**
• stress
• lack of sleep
• dehydration
• caffeine (too much OR withdrawal)
• certain foods (aged cheese, processed meats, alcohol)
• bright lights
• strong smells
• weather changes

**what helps:**

**for immediate relief:**
• rest in dark, quiet room
• cold or warm compress on head/neck
• hydration (drink water!)
• over-the-counter pain relievers (use as directed)
• gentle neck stretches
• caffeine (can help some headaches, but be careful)

**for prevention:**
• regular sleep schedule
• stay hydrated
• regular meals (don't skip!)
• stress management
• exercise regularly
• identify and avoid triggers
• keep a headache diary

**when to see a doctor:**
• "worst headache of your life"
• with fever, stiff neck, confusion
• after head injury
• new type of headache after age 50
• headaches that keep getting worse
• daily or near-daily headaches

what do YOUR headaches feel like? when do they happen? 💫"""
    
    def answer_sleep_questions(self, question):
        return """🌙 **understanding sleep**

sleep problems affect women differently throughout the cycle:

**cycle and sleep:**

🌸 **week 1-2 (after period):**
• usually sleep well
• estrogen helps with sleep quality

🌙 **week 3-4 (before period):**
• may have trouble falling/staying asleep
• progesterone affects body temperature
• pms symptoms can disrupt sleep

**common sleep issues:**

😴 **can't fall asleep:**
• racing thoughts? write them down before bed
• create a wind-down routine (same thing every night)
• try 4-7-8 breathing: inhale 4, hold 7, exhale 8
• no phones in bed (they're sleep killers!)
• magnesium before bed might help (ask doctor)

😴 **wake up in the middle of the night:**
• don't look at the clock!
• if not back asleep in 20 min, get up and do something boring
• check if alcohol is disrupting sleep (it does!)
• keep room cool and dark

😴 **wake up tired:**
• could be sleep quality, not quantity
• possible sleep apnea (more common in women than thought)
• restless leg syndrome (common in pregnancy)
• not enough deep sleep

**sleep hygiene checklist:**
• same bedtime/wake time every day (even weekends!)
• cool room (65-68°f / 18-20°c)
• dark room (blackout curtains)
• quiet (white noise if helpful)
• comfy mattress/pillows
• no caffeine after 2pm
• no alcohol 3 hours before bed
• no big meals before bed
• exercise earlier in day (not right before bed)
• no screens 1 hour before bed

**natural sleep aids (ask doctor first):**
• magnesium glycinate
• chamomile tea
• lavender essential oil
• melatonin (short-term use only)

**when to see a doctor:**
• insomnia lasting more than a few weeks
• sleep problems affecting daily life
• you stop breathing during sleep (partner may notice)
• extreme daytime sleepiness

tell me about YOUR sleep - what's the hardest part? 💫"""
    
    def answer_skin_questions(self, question):
        return """🧴 **understanding your skin**

your skin is connected to your hormones! here's how:

**skin through your cycle:**

🌸 **week 1-2 (after period):**
• skin usually looks clearer
• estrogen helps skin stay plump and glowing

🌼 **week 3 (ovulation):**
• some women get an "ovulation glow"
• higher estrogen

🌙 **week 4 (before period):**
• progesterone increases oil production
• pores can clog = breakouts
• inflammation increases

**types of breakouts:**

🧴 **hormonal acne:**
• usually on jawline, chin, lower face
• happens around your period
• deep, cystic pimples that hurt
• **helps:** start using treatment a few days BEFORE your period

🧴 **stress acne:**
• anywhere on face
• from cortisol increasing oil
• often during exams, stressful times

🧴 **diet-related:**
• high sugar/dairy can trigger some people
• everyone's different - track what affects YOU

**what helps:**

🟢 **skincare routine:**
• gentle cleanser (harsh products make skin produce MORE oil)
• moisturizer even if oily (hydration is key!)
• spf every day (hormones can cause pigmentation)
• change pillowcases frequently
• don't pick! (causes scarring)

🟢 **ingredients that help:**
• **salicylic acid:** unclogs pores
• **benzoyl peroxide:** kills bacteria
• **niacinamide:** reduces inflammation
• **retinoids:** cell turnover (use at night, start slow)
• **azelaic acid:** great for hormonal acne and dark spots

🟢 **for period-related breakouts:**
• start using salicylic acid a few days BEFORE your period
• some women find spearmint tea helps (reduces androgens)
• be extra gentle with skin during pms

🟢 **lifestyle:**
• drink water (hydration helps skin)
• manage stress
• healthy diet with less sugar
• enough sleep (beauty sleep is real!)

**when to see a dermatologist:**
• severe cystic acne
• acne leaving scars
• not responding to otc treatments
• with irregular periods (could be pcos)

what's YOUR skin concern right now? 💕"""
    
    def answer_weight_questions(self, question):
        return """📊 **understanding weight and body**

weight fluctuations in women are NORMAL, especially with your cycle:

**cycle-related weight changes:**

🌸 **week before period (luteal phase):**
• water retention can add 2-5 pounds
• breast tissue changes
• bloating
• this is NOT fat gain - it's water!
• goes away after period starts

🌸 **during period:**
• usually "whoosh" effect as water leaves
• weight drops back to normal

**other factors affecting weight:**

⚖️ **stress:**
• cortisol causes water retention
• can affect where you store fat (more around middle)

😴 **sleep:**
• poor sleep affects hunger hormones (ghrelin and leptin)
• can increase cravings

💊 **medications:**
• some birth control can affect weight
• antidepressants
• steroids

🩺 **medical conditions:**
• pcos (weight gain, especially around middle)
• thyroid issues
• insulin resistance

**healthy approach to weight:**

🟢 **focus on how you FEEL, not just numbers:**
• energy levels
• strength
• mood
• sleep quality
• digestion
• how clothes fit

🟢 **sustainable habits:**
• eat enough protein and fiber
• stay hydrated
• move in ways you enjoy
• get enough sleep
• manage stress
• don't restrict (leads to bingeing)

🟢 **when weighing:**
• if you weigh yourself, do it at same time of day
• same day of cycle (e.g., day 5 of your period)
• remember the 2-5 pound cycle fluctuation is NORMAL

**intuitive eating principles:**
• eat when hungry, stop when full
• all foods fit (no "good" or "bad" foods)
• movement should feel good, not punishing
• health is about more than weight

**when to see a doctor:**
• unexplained weight loss or gain
• weight changes with other symptoms
• extreme measures to control weight
• disordered eating patterns
• preoccupation with weight affecting daily life

**you deserve to feel good in your body** regardless of the number on the scale. what's YOUR concern about weight? 💕"""
    
    def answer_doctor_questions(self, question):
        return """🩺 **when to see a doctor**

it's hard to know when something needs medical attention. here's a guide:

**for periods:**

🩸 **see a doctor if:**
• no period for 3+ months (and not pregnant)
• bleeding between periods
• soaking through pad/tampon every 1-2 hours
• periods less than 21 days or more than 35 days apart
• severe pain that otc meds don't help
• suddenly much heavier or more painful than usual

**for pain:**

🤕 **see a doctor if:**
• pain that stops daily activities
• new pain after age 25
• pain with fever, vomiting
• pain during sex
• pain that wakes you at night

**for breast health:**

🩺 **see a doctor if:**
• new lump or thickening
• nipple discharge (especially if bloody)
• skin changes (dimpling, redness, rash)
• persistent pain in one spot
• nipple turning inward

**for general health:**

❤️ **see a doctor if:**
• unexplained weight loss
• unexplained fever
• lump anywhere
• changes in moles
• persistent cough or hoarseness
• changes in bowel/bladder habits
• extreme fatigue

**for mental health:**

🧠 **see a doctor if:**
• feeling sad, anxious, or hopeless for 2+ weeks
• thoughts of self-harm
• can't do daily activities
• using substances to cope
• panic attacks

**for preventive care:**

🌸 **recommended:**
• annual well-woman visit
• pap smear: starting at 21, then every 3-5 years
• breast exams: clinical exams and self-exams
• std testing if sexually active
• vaccinations
• blood pressure check
• cholesterol screening (starting at 20)

**questions to ask your doctor:**
• "is this normal for someone my age?"
• "what tests do you recommend?"
• "how often should i come back?"
• "what symptoms should i watch for?"

**trust your gut!** if something feels wrong, get it checked. better to be safe.

what specific symptom are you worried about? 💕"""
    
    def answer_general(self, question):
        return """🌸 **i'm here to help!**

i can answer questions about:

**period & menstrual health:**
• period pain and cramps
• irregular cycles
• heavy bleeding
• pms and pmdd

**physical health:**
• fatigue and low energy
• headaches and migraines
• sleep problems
• skin issues (acne, breakouts)
• weight concerns

**reproductive health:**
• pregnancy and fertility
• birth control questions
• when to see a doctor

**mental wellness:**
• mood swings
• anxiety and stress
• emotional health

**what would you like to know more about?** 💕

just ask me anything - i'm here to listen and help!

*remember: i provide general information, not medical advice. always consult a healthcare provider for personal concerns.*"""

# Initialize AI
ai = SmartWomenHealthAI()

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
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🚀 Starting smart women's health AI on port {port}")
    app.run(host='0.0.0.0', port=port)