import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

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
        'version': '5.0 - ultra smart ai'
    })

class UltraSmartWomenHealthAI:
    def __init__(self):
        self.conversation_history = []
    
    def get_response(self, message):
        """Main method to get AI response"""
        message_lower = message.lower()
        
        # Store in history
        self.conversation_history.append(message)
        
        # PERIOD & MENSTRUAL
        if any(word in message_lower for word in ['period', 'menstrual', 'monthly', 'blood', 'bleeding']):
            return self.answer_period_questions(message)
        
        # PAIN & CRAMPS
        elif any(word in message_lower for word in ['cramp', 'pain', 'hurt', 'ache', 'sore', 'stabbing', 'sharp', 'throbbing']):
            return self.answer_pain_questions(message)
        
        # FATIGUE & ENERGY
        elif any(word in message_lower for word in ['tired', 'fatigue', 'exhausted', 'energy', 'sleepy', 'drained', 'weak', 'no energy']):
            return self.answer_fatigue_questions(message)
        
        # MOOD & EMOTIONS
        elif any(word in message_lower for word in ['mood', 'emotional', 'cry', 'sad', 'anxious', 'depressed', 'irritable', 'angry', 'upset', 'stress', 'overwhelmed', 'panic']):
            return self.answer_mood_questions(message)
        
        # CYCLE IRREGULARITIES
        elif any(word in message_lower for word in ['irregular', 'late', 'missed', 'early', 'cycle', 'when is my period', 'delayed']):
            return self.answer_cycle_questions(message)
        
        # HEADACHES & MIGRAINES
        elif any(word in message_lower for word in ['headache', 'migraine', 'head hurts', 'pressure in head', 'throbbing head', 'tension headache']):
            return self.answer_headache_questions(message)
        
        # SLEEP PROBLEMS
        elif any(word in message_lower for word in ['sleep', 'insomnia', "can't sleep", 'wake up', 'restless', 'nightmare', 'tired in morning', 'fall asleep']):
            return self.answer_sleep_questions(message)
        
        # SKIN ISSUES
        elif any(word in message_lower for word in ['skin', 'acne', 'breakout', 'pimple', 'rash', 'dry skin', 'oily skin', 'cyst', 'blackhead', 'whitehead', 'scar']):
            return self.answer_skin_questions(message)
        
        # WEIGHT & BODY
        elif any(word in message_lower for word in ['weight', 'gain', 'lose', 'appetite', 'hungry', 'full', 'bmi', 'diet', 'food', 'eating', 'craving']):
            return self.answer_weight_questions(message)
        
        # PREGNANCY & FERTILITY
        elif any(word in message_lower for word in ['pregnant', 'pregnancy', 'fertility', 'conceive', 'trying to get pregnant', 'ovulation', 'fertile', 'baby']):
            return self.answer_pregnancy_questions(message)
        
        # DIGESTIVE ISSUES
        elif any(word in message_lower for word in ['bloating', 'gas', 'stomach', 'nausea', 'vomit', 'diarrhea', 'constipated', 'digestion', 'gut', 'cramps stomach']):
            return self.answer_digestive_questions(message)
        
        # BREAST HEALTH
        elif any(word in message_lower for word in ['breast', 'chest', 'boob', 'tender breast', 'lump', 'nipple']):
            return self.answer_breast_questions(message)
        
        # HAIR ISSUES
        elif any(word in message_lower for word in ['hair', 'hair loss', 'thinning hair', 'bald', 'hair growth', 'facial hair', 'excess hair']):
            return self.answer_hair_questions(message)
        
        # SEXUAL HEALTH
        elif any(word in message_lower for word in ['sex', 'pain during sex', 'libido', 'sex drive', 'std', 'sti', 'infection', 'discharge', 'itch']):
            return self.answer_sexual_health_questions(message)
        
        # DOCTOR QUESTIONS
        elif any(word in message_lower for word in ['doctor', 'gyno', 'gynecologist', 'specialist', 'should i see', 'when to go', 'appointment', 'check up']):
            return self.answer_doctor_questions(message)
        
        # BIRTH CONTROL
        elif any(word in message_lower for word in ['birth control', 'contraception', 'pill', 'iud', 'implant', 'shot', 'patch', 'ring', 'condom']):
            return self.answer_birth_control_questions(message)
        
        # DEFAULT
        else:
            return self.answer_general(message)
    
    def answer_period_questions(self, question):
        return """🌸 understanding your period

A period happens when your body sheds the lining of your uterus. This is completely normal and healthy.

what's normal:
• Cycle length: 21 to 35 days (28 days is average but everyone is different)
• Period length: 3 to 7 days
• Flow: light to medium to heavy (can change day to day)
• Color: bright red, dark red, brown, or pink - all normal!
• Small clots: up to the size of a dime are normal

common period symptoms:
• Mild cramping in lower belly
• Bloating (your tummy might feel bigger)
• Breast tenderness
• Fatigue and low energy
• Mood changes (irritability, sadness)
• Food cravings (especially chocolate and carbs)
• Headaches
• Lower back pain
• Oily skin or breakouts

what helps with period symptoms:
• Heat therapy - heating pad or hot water bottle on your belly
• Gentle movement - walking, stretching, yoga
• Warm baths with epsom salts
• Over-the-counter pain relief (ibuprofen works best for cramps)
• Rest when you need to (your body is working hard!)
• Stay hydrated - drink extra water
• Iron-rich foods if bleeding is heavy (spinach, red meat, beans)

when to see a doctor:
• Periods suddenly become much more painful
• You're soaking through a pad or tampon every 1-2 hours
• Periods last longer than 7 days
• Cycles are shorter than 21 days or longer than 35 days
• Bleeding between periods
• No period for 3+ months (and not pregnant)
• Severe pain that medication doesn't help

what specifically would you like to know about your period? 💕"""
    
    def answer_pain_questions(self, question):
        if 'cramp' in question.lower():
            return """🩹 understanding period cramps

Period cramps happen because your uterus contracts to shed its lining. These contractions are triggered by chemicals called prostaglandins. More prostaglandins = more pain.

why some women have worse cramps:
• Higher prostaglandin levels
• Endometriosis (tissue grows outside uterus)
• Fibroids (benign growths)
• Adenomyosis (tissue grows into uterine wall)
• Pelvic inflammatory disease
• Stress (makes pain feel worse)
• Age (teens and 20s often have more cramps)

immediate relief:
• Heat therapy - heating pad or hot water bottle on lower belly for 15-20 minutes (works as well as ibuprofen!)
• Over-the-counter medication - ibuprofen or naproxen work best because they reduce prostaglandins. Take with food!
• Gentle movement - light walking, stretching, child's pose in yoga
• Warm bath - add epsom salts for muscle relaxation
• Herbal tea - ginger, chamomile, or raspberry leaf tea
• Massage - gently massage your lower belly
• orgasm - can help release tension and pain (seriously!)

natural remedies (ask doctor first):
• Magnesium - helps muscles relax
• Vitamin B1 - studies show it helps with cramps
• Omega-3 fatty acids (fish oil) - anti-inflammatory
• Acupressure or acupuncture
• Essential oils - lavender, clary sage diluted and massaged on belly

foods that help:
• Anti-inflammatory foods: berries, nuts, leafy greens, turmeric
• Warm foods: soups, warm oatmeal
• Dark chocolate (magnesium + mood boost)
• Bananas (potassium helps with cramping)
• Ginger (add to tea or meals)
• Pineapple (contains bromelain, anti-inflammatory)

foods to avoid before/during period:
• Salty foods (increase bloating)
• Caffeine (can increase tension and cramps)
• Sugary foods (cause energy crashes and inflammation)
• Processed foods
• Alcohol (can make cramps worse)

when to see a doctor:
• Pain stops you from going to school or work
• Over-the-counter meds don't help at all
• Pain suddenly gets worse than usual
• You're over 25 and pain is new or getting worse
• Pain between periods too
• Heavy bleeding with large clots
• Pain during sex
• Pain with fever or vomiting

possible conditions that need medical attention:
• Endometriosis - tissue similar to uterine lining grows outside the uterus
• Fibroids - non-cancerous growths in the uterus
• Adenomyosis - tissue grows into uterine wall
• Pelvic inflammatory disease - infection
• Ovarian cysts

what's your pain like? Where is it located? How long does it last? Tell me more and I'll help you figure it out 💕"""
        
        elif 'back' in question.lower():
            return """🩹 understanding back pain

Back pain is very common and can be related to your cycle or other factors.

period-related back pain:
• Lower back pain often happens with period cramps
• Caused by the same prostaglandins that cause cramps
• Can feel like a dull ache or sharp pain
• Usually starts a day or two before period
• Lasts through the first few days of bleeding

what helps for period back pain:
• Heating pad on lower back
• Gentle stretching (child's pose, cat-cow)
• Over-the-counter pain relief
• Warm bath
• Gentle massage
• Rest

other causes of back pain:
• Poor posture (especially from sitting at computer)
• Muscle strain from exercise
• Sleeping position
• Stress (makes muscles tense)
• Sciatica
• Kidney issues (if pain is higher up)

when to see a doctor for back pain:
• Pain after injury or fall
• Pain with fever
• Numbness or tingling in legs
• Loss of bladder or bowel control
• Pain that doesn't improve with rest
• Pain that wakes you at night

what does your back pain feel like? When did it start? 💫"""
        
        else:
            return """🩹 understanding pain

Pain is your body's way of telling you something needs attention.

types of pain common in women:
• Cramping pain - usually period-related, in lower belly
• Headaches and migraines - can be hormonal
• Breast pain - often before period
• Back pain - can be period-related or from posture
• Pelvic pain - needs medical attention
• Joint pain - can be related to hormones
• Muscle pain - from tension or exercise

track your pain:
Write down:
• When it happens (before/during/after period?)
• Where exactly it hurts
• What it feels like (sharp, dull, throbbing, stabbing, burning)
• How bad it is (1-10 scale)
• What makes it better or worse
• How long it lasts
• Any other symptoms with it

This information is super helpful for doctors!

red flags - see a doctor if:
• Sudden severe pain
• Pain with fever
• Pain after injury
• Pain that wakes you at night
• Pain lasting more than a few days
• Pain with unexplained weight loss
• Pain with bleeding (not period)

what kind of pain are you experiencing? Where is it? 🌸"""
    
    def answer_fatigue_questions(self, question):
        return """⚡ understanding fatigue

Feeling tired all the time is SO common, especially for women. Let's figure out why YOU might be exhausted:

🩸 iron deficiency / anemia
• Very common with heavy periods
• Your body needs iron to make red blood cells that carry oxygen
• Without enough iron, your cells don't get enough oxygen = you feel exhausted
• Other signs: pale skin, cold hands and feet, dizziness, brittle nails, shortness of breath
• Iron-rich foods: red meat, spinach, lentils, beans, fortified cereals, pumpkin seeds
• Tip: eat with vitamin C (orange juice, citrus, bell peppers) to help absorption

😴 poor sleep quality
• It's not just how many hours, but how well you sleep
• Signs of poor sleep: waking up multiple times, not feeling rested, needing caffeine to function
• Sleep hygiene tips:
  - Same bedtime and wake time (even on weekends!)
  - No phones 1 hour before bed (blue light disrupts melatonin)
  - Cool, dark, quiet room
  - No caffeine after 2pm
  - Limit alcohol (it ruins sleep quality)
  - No big meals before bed

🧠 stress and mental health
• Stress hormones (cortisol) can exhaust your body
• Anxiety and depression both cause fatigue
• Your brain working overtime = tired body
• Signs: can't turn your brain off, worrying, feeling overwhelmed
• Helpful: therapy, meditation, time in nature, talking to friends, deep breathing

⚡ thyroid issues
• Very common in women!
• Hypothyroidism (underactive) causes fatigue, weight gain, feeling cold, dry skin, hair thinning
• Hyperthyroidism (overactive) causes fatigue too, along with weight loss, racing heart, anxiety
• Simple blood test can check this

🥗 nutrition deficiencies
• Vitamin D deficiency - very common, especially in winter (fatigue, bone pain, low mood)
• Vitamin B12 deficiency - more common in vegetarians (fatigue, numbness, brain fog)
• Magnesium deficiency - fatigue, muscle cramps, trouble sleeping
• Eat a variety of whole foods and consider supplements after talking to doctor

💧 dehydration
• Even mild dehydration causes fatigue
• Aim for 8 glasses of water daily (more if you exercise or it's hot)
• Coffee and tea don't count (they're diuretics)
• Signs of dehydration: dark urine, dry mouth, headache

🩺 other medical causes
• Diabetes (fatigue, thirst, frequent urination)
• Chronic fatigue syndrome (extreme fatigue lasting months)
• Autoimmune diseases (like lupus, rheumatoid arthritis)
• Heart conditions
• Sleep apnea (pauses in breathing during sleep)

energy-boosting tips:
• Gentle movement (walking actually BOOSTS energy)
• Protein with every meal
• Don't skip breakfast
• Short power naps (10-20 minutes, no longer!)
• Sunlight exposure in morning
• Reduce sugar (causes energy crashes)
• Stay social (loneliness is draining)

when to see a doctor:
• Fatigue lasting more than 2 weeks
• Fatigue with unexplained weight changes
• Feeling cold all the time
• Shortness of breath
• Racing heart
• Depression or anxiety
• Not feeling better with rest

what does YOUR fatigue feel like? When did it start? Is it related to your cycle? Let's figure this out together 💕"""
    
    def answer_mood_questions(self, question):
        return """😢 understanding your feelings

Your emotions are valid, and they're often connected to what's happening in your body:

hormones and mood:

🌸 estrogen:
• Boosts serotonin (your 'feel-good' chemical)
• Higher in first half of cycle = usually better mood
• Drops before period = can affect mood
• Also drops after pregnancy (postpartum)

🌙 progesterone:
• Rises after ovulation
• Can cause fatigue, mood changes
• Has calming effect (like natural valium)
• Drops sharply before period

hormonal mood patterns:

🌱 week 1-2 (after period):
• Estrogen rising
• Usually feel more energetic, optimistic
• Good time for socializing, projects

🌼 week 3 (ovulation):
• Peak estrogen
• Often feel confident, sociable
• Some feel extra emotional

🍂 week 4 (before period):
• Progesterone drops
• Estrogen drops
• PMS symptoms start
• Can feel irritable, sad, anxious

common PMS mood symptoms:
• Irritability (snapping at people)
• Mood swings (happy then crying)
• Sadness or depression
• Anxiety or tension
• Feeling overwhelmed
• Difficulty concentrating (brain fog)
• Crying easily
• Anger
• Withdrawing from others

PMS vs PMDD:

🌸 PMS (premenstrual syndrome):
• Mild to moderate symptoms
• Doesn't severely impact daily life
• Affects up to 75% of women
• Manageable with lifestyle changes

🌪️ PMDD (premenstrual dysphoric disorder):
• Severe symptoms
• Affects daily life and relationships
• Intense depression, anger, anxiety
• Feel hopeless or out of control
• Affects 3-8% of women
• Needs medical treatment
• Can include physical symptoms too

what helps with mood:

🟢 lifestyle changes:
• Exercise - 30 minutes daily (walking, dancing, whatever you enjoy)
• Sunlight - get outside, especially in morning
• Sleep - prioritize 7-9 hours (crucial for mood!)
• Reduce stress - whatever works for you
• Avoid alcohol - it's a depressant
• Limit caffeine - can increase anxiety
• Eat regular meals - blood sugar swings affect mood

🟢 diet for mood:
• Complex carbs - whole grains, veggies (boost serotonin)
• Protein with each meal - helps stabilize blood sugar
• Omega-3s - salmon, walnuts, flax seeds (brain health)
• Magnesium - leafy greens, nuts, dark chocolate (calming)
• Limit sugar - causes energy crashes and mood swings
• Stay hydrated - dehydration affects mood

🟢 supplements (ask doctor first):
• Calcium - 1200mg daily (studies show it significantly reduces PMS)
• Magnesium - helps with mood and physical symptoms
• Vitamin B6 - helps with mood and brain function
• Vitamin D - low levels linked to depression
• Omega-3s - anti-inflammatory, brain health

🟢 tracking:
• Use an app to track your cycle and mood for 2-3 months
• You'll likely see a pattern
• This helps you PREPARE for tough days
• Also helpful for doctor if symptoms are severe

when to see a doctor:
• Mood affecting daily life for 2+ weeks
• Not just before period - any time of month
• Can't get out of bed
• Loss of interest in things you loved
• Changes in appetite or sleep
• Thoughts of self-harm
• Using substances to cope
• Panic attacks

crisis support:
If you're having thoughts of self-harm:
• Call 988 (Suicide & Crisis Lifeline in US)
• Text HOME to 741741
• Go to emergency room
• Tell someone you trust
• You are not alone. You deserve help.

remember: Mental health is health. You deserve support. 🤍

how have YOU been feeling? I'm here to listen without judgment."""
    
    def answer_cycle_questions(self, question):
        return """🌊 understanding your menstrual cycle

Let's talk about what's normal and what's not when it comes to your cycle:

what's normal:
• Cycle length: 21 to 35 days (count from first day of period to next first day)
• Period length: 3 to 7 days
• Flow: light to heavy (can vary day to day)
• Variation: up to 7-9 days difference from cycle to cycle is still normal
• Age matters: teens and women in 40s often have more variation

the menstrual cycle phases:

🌸 menstrual phase (days 1-5):
• You're on your period
• Hormones are at their lowest
• You might feel tired, introspective
• Good for rest and gentle movement

🌱 follicular phase (days 6-14):
• Estrogen rises
• Energy increases
• Mood improves
• Good for new projects, exercise

🌼 ovulation (around day 14):
• Egg is released
• Estrogen peaks
• You might feel your best
• Some feel mild pain (mittelschmerz)

🍂 luteal phase (days 15-28):
• Progesterone rises
• If no pregnancy, hormones drop
• PMS symptoms may appear
• Energy may decrease

reasons for irregular cycles:

🟢 common and usually not serious:
• Age - first 2-3 years after first period (teenagers)
• Age - perimenopause (40s and 50s)
• Stress - high stress affects hormones
• Travel - jet lag can temporarily affect cycle
• Illness - getting sick can delay period
• Weight changes - significant loss or gain
• Exercise - very intense training
• Medications - some antibiotics, antidepressants
• Breastfeeding - can stop periods

🟡 may need medical attention:

PCOS (polycystic ovary syndrome):
• Very common (affects 1 in 10 women)
• Symptoms: irregular periods, acne, weight gain (especially around middle), excess facial/body hair, thinning scalp hair
• Cause: hormone imbalance
• Manageable with lifestyle and medication

thyroid issues:
• Both overactive and underactive thyroid affect periods
• Symptoms: fatigue, weight changes, temperature sensitivity, hair changes
• Simple blood test can diagnose

high prolactin:
• Can be caused by stress, medication, or pituitary tumor
• Symptoms: irregular periods, milky discharge from nipples, headaches

birth control:
• Hormonal IUD or progestin-only methods can make periods irregular or stop them
• This is normal for these methods
• Periods usually return to normal when you stop

when to see a doctor:
• No period for 3+ months (and not pregnant)
• Cycles consistently shorter than 21 days or longer than 35 days
• Bleeding between periods
• Severe pain with irregular cycles
• Trying to get pregnant and cycles are irregular
• Other symptoms like acne, weight changes, excess hair
• Sudden change in your regular pattern

track your cycle!
Use an app or calendar to track:
• When period starts and ends
• How heavy the flow is
• Any pain or symptoms
• Mood changes
• This information is GOLD for your doctor

what's your specific situation? How old are you? What does irregular mean for you? Tell me more 🌸"""
    
    def answer_headache_questions(self, question):
        return """🤕 understanding headaches

Headaches are super common, especially in women. Let's figure out what kind you might have:

types of headaches:

🤕 tension headaches:
• Feels like a tight band around your head
• Dull, aching pain
• Often from stress, poor posture, eye strain
• Usually both sides of head
• Can last 30 minutes to several days
• Neck and shoulder muscles may be tight

⚡ migraines:
• Throbbing or pulsing pain, often one side
• Moderate to severe pain
• Nausea or vomiting
• Sensitivity to light, sound, smells
• Can last 4 to 72 hours
• Sometimes preceded by "aura" (visual disturbances like flashing lights, zigzag lines, blind spots)
• May have warning signs like food cravings, mood changes, yawning

🔄 hormonal headaches:
• Happen right before or during your period
• From drop in estrogen
• Can be migraine-like or tension-type
• Often improve during pregnancy
• May worsen with birth control pills

🌪️ sinus headaches:
• Pain in forehead, cheeks, behind nose
• Pressure that gets worse when bending over
• Usually with other sinus symptoms (congestion, runny nose)
• Often from allergies or infection

🤯 cluster headaches:
• Severe pain around one eye
• Happens in clusters (daily for weeks then stops)
• More common in men
• Eye may be red, watery, droopy

common triggers:
• Stress (most common trigger)
• Lack of sleep or too much sleep
• Dehydration
• Caffeine (too much OR withdrawal)
• Skipping meals
• Certain foods: aged cheese, processed meats, chocolate, MSG, artificial sweeteners
• Alcohol (especially red wine)
• Bright lights, loud sounds, strong smells
• Weather changes
• Hormonal changes
• Screen time / eye strain

what helps:

for immediate relief:
• Rest in dark, quiet room
• Cold or warm compress on head or neck
• Hydration (drink water!)
• Over-the-counter pain relievers (use as directed)
• Gentle neck stretches
• Caffeine (can help some headaches, but be careful - can also trigger)
• Sleep if possible
• Massage (temples, neck, shoulders)

for prevention:
• Regular sleep schedule
• Stay hydrated
• Regular meals (don't skip!)
• Stress management
• Exercise regularly
• Identify and avoid triggers
• Keep a headache diary
• Limit screen time, take breaks
• Check your posture

when to see a doctor:
• "Worst headache of your life"
• With fever, stiff neck, confusion
• After head injury
• New type of headache after age 50
• Headaches that keep getting worse
• Daily or near-daily headaches
• Headaches that wake you at night
• With vision changes
• With weakness or numbness

what do YOUR headaches feel like? When do they happen? Do they relate to your cycle? 💫"""
    
    def answer_sleep_questions(self, question):
        return """🌙 understanding sleep

Sleep problems affect so many women. Let's figure out what's going on with YOUR sleep:

cycle and sleep:

🌸 week 1-2 (follicular phase):
• Usually sleep well
• Estrogen helps with sleep quality
• Feel more rested

🌙 week 3-4 (luteal phase):
• May have trouble falling asleep
• May wake up during the night
• Progesterone increases body temperature (disrupts sleep)
• PMS symptoms (cramps, bloating) can wake you
• Dreams may be more vivid

common sleep issues:

😴 can't fall asleep:
• Racing thoughts? Write them down before bed
• Create a wind-down routine (same thing every night)
• Try 4-7-8 breathing: inhale 4 seconds, hold 7 seconds, exhale 8 seconds
• No phones in bed (they're sleep killers!)
• Get up if not asleep in 20 minutes (do something boring, then try again)
• Magnesium before bed might help (ask doctor)
• Melatonin (short-term use only, talk to doctor)

😴 wake up in the middle of the night:
• Don't look at the clock! (creates anxiety)
• If not back asleep in 20 min, get up and do something boring (read a book, not screens)
• Check if alcohol is disrupting sleep (it does!)
• Keep room cool and dark
• White noise might help

😴 wake up tired:
• Could be sleep quality, not quantity
• Sleep apnea (more common in women than thought) - pauses in breathing
• Restless leg syndrome (urge to move legs) - common in pregnancy
• Not enough deep sleep
• Anxiety or depression

😴 nightmares or vivid dreams:
• Can be worse before period
• Stress related
• Medication side effects
• Pregnancy (very common)

sleep hygiene checklist:
• Same bedtime and wake time every day (even weekends!)
• Cool room (65-68°F / 18-20°C)
• Dark room (blackout curtains or eye mask)
• Quiet (earplugs or white noise if needed)
• Comfy mattress and pillows
• No caffeine after 2pm
• No alcohol 3 hours before bed (ruins sleep quality)
• No big meals before bed
• Exercise earlier in day (not right before bed)
• No screens 1 hour before bed (blue light disrupts melatonin)
• Bed only for sleep and sex (train your brain)

natural sleep aids (ask doctor first):
• Magnesium glycinate - helps relaxation
• Chamomile tea - calming
• Lavender essential oil - on pillow or in diffuser
• Valerian root - herbal supplement
• Tart cherry juice - contains natural melatonin
• Passionflower tea

when to see a doctor:
• Insomnia lasting more than a few weeks
• Sleep problems affecting daily life
• You stop breathing during sleep (partner may notice)
• Loud snoring
• Extreme daytime sleepiness (falling asleep during day)
• Restless legs that keep you awake
• Depression or anxiety

tell me about YOUR sleep - what's the hardest part? How many hours do you usually get? 💫"""
    
    def answer_skin_questions(self, question):
        return """🧴 understanding your skin

Your skin is connected to what's happening inside your body, especially your hormones:

skin through your cycle:

🌸 week 1-2 (after period):
• Skin usually looks clearer
• Estrogen helps skin stay plump and glowing
• Good time for trying new products
• Wounds heal faster

🌼 week 3 (ovulation):
• Some women get an "ovulation glow"
• Higher estrogen = more collagen
• Skin may look its best

🌙 week 4 (before period):
• Progesterone increases oil production
• Pores can clog = breakouts
• Inflammation increases
• Skin may be more sensitive
• Breakouts typically on jawline, chin, lower face

types of breakouts:

🧴 hormonal acne:
• Usually on jawline, chin, lower face
• Happens around your period
• Deep, cystic pimples that hurt
• Come back same time each month
• Helps: start treatment a few days BEFORE your period

🧴 stress acne:
• Anywhere on face
• From cortisol increasing oil
• Often during exams, stressful times
• Can be inflamed and red

🧴 diet-related:
• High sugar foods can trigger some people
• Dairy affects some (everyone's different)
• Track what affects YOU
• Common triggers: dairy, sugar, white bread, whey protein

🧴 makeup-related:
• Pores clogged from makeup
• Not cleansing properly
• Dirty makeup brushes
• Products too heavy for your skin

what helps:

🟢 skincare routine basics:
• Gentle cleanser (harsh products make skin produce MORE oil)
• Moisturizer even if oily (hydration is key!)
• SPF every day (hormones can cause pigmentation)
• Change pillowcases frequently (at least weekly)
• Don't pick! (causes scarring and spreads bacteria)
• Clean your phone screen
• Wash face after sweating

🟢 ingredients that help:
• Salicylic acid - unclogs pores, great for blackheads and whiteheads
• Benzoyl peroxide - kills bacteria, good for inflamed acne
• Niacinamide - reduces inflammation, helps with redness
• Retinoids - cell turnover, prevents clogged pores (use at night, start slow)
• Azelaic acid - great for hormonal acne and dark spots
• Sulfur - absorbs oil, reduces inflammation
• Tea tree oil - natural antibacterial (dilute first!)

🟢 for period-related breakouts:
• Start using treatment a few days BEFORE your period
• Be extra gentle with skin during PMS
• Some women find spearmint tea helps (reduces androgens)
• Don't introduce new products right before period (skin is sensitive)

🟢 lifestyle:
• Drink water (hydration helps skin)
• Manage stress
• Healthy diet with less sugar
• Enough sleep (beauty sleep is real!)
• Exercise (increases blood flow to skin)
• Don't touch your face during the day

when to see a dermatologist:
• Severe cystic acne
• Acne leaving scars or dark spots
• Not responding to over-the-counter treatments
• With irregular periods (could be PCOS)
• Sudden severe acne in adult years
• Acne affecting your mental health

what's YOUR skin concern right now? Where are you breaking out? 💕"""
    
    def answer_weight_questions(self, question):
        return """📊 understanding your body and weight

Weight fluctuations in women are NORMAL, especially with your cycle. Let's talk about it:

cycle-related weight changes:

🌸 week before period (luteal phase):
• Water retention can add 2-5 pounds
• Breast tissue changes (swelling, tenderness)
• Bloating (your jeans feel tighter)
• Constipation can happen
• This is NOT fat gain - it's water and normal bodily changes
• It goes away after your period starts

🌸 during period:
• Usually "whoosh" effect as water leaves
• Weight drops back to normal
• You might feel lighter

🌸 week after period:
• Usually lowest weight of month
• Good time to weigh if you track

other factors affecting weight:

⚖️ stress:
• Cortisol (stress hormone) causes water retention
• Can increase belly fat storage
• Can cause cravings for sugar and fat
• Emotional eating

😴 sleep:
• Poor sleep affects hunger hormones (ghrelin and leptin)
• Ghrelin goes up = more hungry
• Leptin goes down = don't feel full
• Can increase cravings for carbs

💊 medications:
• Some birth control can cause water retention
• Antidepressants (some)
• Steroids
• Antihistamines (some people)
• Always check side effects

🩺 medical conditions:
• PCOS - weight gain especially around middle, insulin resistance
• Thyroid issues - hypothyroidism causes weight gain
• Insulin resistance - difficulty losing weight
• Depression - can affect appetite and activity

age:
• Metabolism naturally slows with age
• Muscle mass decreases if not maintained
• Hormonal changes in perimenopause

healthy approach to weight:

🟢 focus on how you FEEL, not just numbers:
• Energy levels throughout the day
• Strength and stamina
• Mood
• Sleep quality
• Digestion
• How clothes fit
• Confidence

🟢 sustainable habits:
• Eat enough protein (helps with fullness, muscle maintenance)
• Eat enough fiber (veggies, fruits, whole grains)
• Stay hydrated (thirst can feel like hunger)
• Move in ways you enjoy (not punishment)
• Get enough sleep (crucial!)
• Manage stress
• Don't restrict (leads to bingeing)
• Eat when hungry, stop when full

🟢 when weighing:
• If you weigh yourself, do it at same time of day (morning after bathroom)
• Same day of cycle (e.g., Day 5 of your period)
• Remember the 2-5 pound cycle fluctuation is NORMAL
• Consider weighing less often (weekly, not daily)
• Weight is just one data point, not your worth

intuitive eating principles:
• Eat when hungry, stop when full
• All foods fit (no "good" or "bad" foods)
• Movement should feel good, not punishing
• Health is about more than weight
• Your body knows what it needs

red flags - disordered eating:
• Obsessing over weight and food
• Severe restriction
• Binge eating
• Purging
• Exercise compulsion
• Extreme fear of weight gain
• Avoiding social situations with food

when to see a doctor:
• Unexplained weight loss
• Unexplained weight gain
• Weight changes with other symptoms
• Extreme measures to control weight
• Disordered eating patterns
• Preoccupation with weight affecting daily life
• Missed periods from weight changes

you deserve to feel good in your body regardless of the number on the scale. what's YOUR concern about weight? 💕"""
    
    def answer_pregnancy_questions(self, question):
        return """🤰 understanding pregnancy and fertility

Whether you're trying to conceive, worried about pregnancy, or just curious, here's helpful information:

early signs of pregnancy:
• Missed period (most common sign)
• Nausea (morning sickness - can happen any time of day)
• Breast tenderness (similar to period but often more intense)
• Fatigue (extreme tiredness)
• Frequent urination (hormone changes increase blood flow to kidneys)
• Food aversions or cravings
• Heightened sense of smell
• Mood swings
• Implantation bleeding (light spotting around when period would be due)
• Bloating
• Constipation

if you think you might be pregnant:
1. Take a home pregnancy test (most accurate after missed period)
2. First morning urine is best (most concentrated)
3. If positive, call a healthcare provider
4. Start prenatal vitamins with folic acid (400-800mcg)
5. Avoid alcohol, smoking, certain foods

if you're trying to conceive:

🌸 track your cycle:
• Ovulation happens about 14 days BEFORE your next period (not after)
• Most fertile window: 5 days before ovulation + day of ovulation
• Signs of ovulation: cervical mucus like egg white, mild cramping on one side, increased libido
• Ovulation predictor kits can help
• Tracking apps can help but aren't always accurate

🌸 optimize fertility:
• Start prenatal vitamins with folic acid (ideally 3 months before trying)
• Limit caffeine (under 200mg/day - about 1-2 cups coffee)
• No alcohol
• Healthy weight (both underweight and overweight can affect fertility)
• Manage stress
• Don't smoke
• Regular moderate exercise
• Track your cycle
• Have sex regularly (every 2-3 days throughout cycle)

🌸 when to see a fertility specialist:
• Under 35: after 1 year of trying
• 35-40: after 6 months
• Over 40: sooner rather than later
• If you have irregular periods or known issues
• If you've had multiple miscarriages

if you're worried about unplanned pregnancy:

🆘 emergency contraception:
• "Morning after pill" (Plan B, Take Action) - works up to 5 days, more effective sooner
• Available at pharmacies without prescription
• Ella (more effective, requires prescription in some places)
• Copper IUD - works as emergency contraception up to 5 days (most effective option)
• Not the same as abortion pill

🤰 abortion options (if applicable):
• Medication abortion (up to 10-11 weeks)
• In-clinic procedure (later in pregnancy)
• Laws vary by location
• Planned Parenthood and local clinics can help

resources:
• Planned Parenthood (if in US)
• Local health clinics
• Your regular gynecologist
• Crisis pregnancy centers (be aware they may have specific agendas)

what specifically do you want to know about? I'm here to help without judgment 💕"""
    
    def answer_digestive_questions(self, question):
        return """🫧 understanding digestive issues

Digestive problems are super common, especially around your period. Let's talk about it:

cycle-related digestive issues:

🌸 before period:
• Bloating is VERY common (water retention)
• Constipation (progesterone slows digestion)
• Gas
• Feeling full quickly
• Food cravings (especially carbs)

🌸 during period:
• Diarrhea or loose stools (prostaglandins affect bowels too)
• Cramping (can be digestive or uterine)
• Nausea (from pain or hormones)
• Loss of appetite

🌸 after period:
• Usually digestion returns to normal
• Less bloating

common digestive issues:

🫧 bloating:
• Can be from hormones, food, or both
• Reduce salt before period
• Avoid carbonated drinks
• Eat slowly, chew well
• Peppermint tea can help
• Gentle movement (walking)
• Over-the-counter simethicone (Gas-X)

💩 constipation:
• Drink more water (aim for 8 glasses)
• Increase fiber slowly (veggies, fruits, whole grains)
• Prunes or prune juice
• Warm lemon water in morning
• Gentle exercise
• Magnesium supplements (ask doctor first)
• Don't ignore the urge to go

💧 diarrhea:
• Stay hydrated (water, electrolyte drinks)
• BRAT diet: bananas, rice, applesauce, toast
• Avoid dairy, greasy foods, caffeine
• Probiotics may help
• Imodium for severe cases (short-term only)
• See doctor if bloody or persistent

😖 nausea:
• Ginger tea or candied ginger
• Small, frequent meals (empty stomach makes nausea worse)
• Avoid strong smells
• Peppermint
• Sea bands (acupressure)
• Eat crackers before getting up

🔥 heartburn / acid reflux:
• Avoid spicy, fatty, acidic foods
• Don't lie down after eating
• Eat smaller meals
• Elevate head of bed
• Antacids (Tums, Rolaids)
• See doctor if persistent

irritable bowel syndrome (IBS):
• Very common in women
• Symptoms: abdominal pain, bloating, diarrhea or constipation
• Often worse with stress and around period
• Low FODMAP diet helps many
• Stress management crucial
• See gastroenterologist

when to see a doctor:
• Blood in stool
• Unexplained weight loss
• Severe pain
• Persistent vomiting
• Fever with digestive symptoms
• Symptoms waking you at night
• Family history of colon cancer
• Symptoms lasting more than a few weeks

what digestive issues are you having? When do they happen? 💫"""
    
    def answer_breast_questions(self, question):
        return """🩺 understanding breast health

Breast changes are normal throughout your cycle and life. Here's what you should know:

cycle-related breast changes:

🌸 before period (luteal phase):
• Breast tenderness and sensitivity
• Swelling (breasts may feel fuller/heavier)
• Lumpy feeling (from hormonal changes)
• This is normal and goes away after period

🌸 during period:
• Symptoms usually improve
• Breasts return to normal size

🌸 after period:
• Breasts are usually least tender
• Good time for self-exam

types of breast pain:

🫧 cyclic breast pain:
• Related to your period
• Affects both breasts
• Feels dull, heavy, achy
• Gets better after period
• Very common and normal

🫧 non-cyclic breast pain:
• Not related to period
• May be one breast only
• Sharp or burning pain
• Could be from injury, cyst, or infection
• See doctor if persistent

breast lumps:

🌸 what's normal:
• Breasts naturally have lumpy tissue (like orange pulp)
• Lumps that change with your cycle are usually normal
• Cysts (fluid-filled sacs) are common
• Fibroadenomas (solid, rubbery lumps) are common in young women

🔴 when to see a doctor:
• New lump that doesn't go away after period
• Hard lump that feels different from surrounding tissue
• Lump that grows over time
• Skin changes: dimpling, puckering, redness, thickening
• Nipple changes: discharge (especially if bloody), turning inward, rash
• Swelling in armpit
• Persistent pain in one spot

breast self-exam:
• Do it at the same time each month (day 7-10 of cycle is ideal)
• Look in mirror with arms at sides, then raised
• Check for changes in size, shape, skin
• Feel while lying down (breast tissue spreads out)
• Use pads of fingers, not tips
• Cover entire breast and armpit
• Know what's normal for YOU

risk factors for breast cancer:
• Age (increases with age)
• Family history
• Genetic mutations (BRCA1, BRCA2)
• Early period (before 12) or late menopause (after 55)
• Never being pregnant or first pregnancy after 30
• Hormone therapy
• Dense breast tissue
• Alcohol consumption
• Obesity

reducing risk:
• Regular exercise
• Healthy weight
• Limit alcohol (1 drink/day max)
• Breastfeeding (reduces risk)
• Regular screenings
• Know your family history

when to see a doctor:
• Any new lump
• Skin changes
• Nipple discharge
• Persistent pain
• For routine screening (mammograms starting at 40-45, earlier if high risk)

do you have specific concerns about your breasts? 💕"""
    
    def answer_hair_questions(self, question):
        return """💇‍♀️ understanding hair changes

Hair changes can be frustrating. Let's talk about what might be happening:

normal hair cycle:
• Hair grows about 1/2 inch per month
• We lose 50-100 hairs daily (normal!)
• Hair goes through growth, resting, and shedding phases

cycle-related hair changes:

🌸 estrogen effect:
• Estrogen promotes hair growth and thickness
• Hair may look fuller and shinier when estrogen is high
• During pregnancy (high estrogen), many women have gorgeous hair
• After pregnancy (estrogen drops), many experience hair shedding (postpartum hair loss)

🌙 progesterone effect:
• Can affect oil production on scalp
• May make hair feel oilier before period

types of hair loss:

😔 telogen effluvium:
• Temporary hair shedding from stress, illness, childbirth, major weight loss
• Hair falls out 2-3 months after trigger
• Usually resolves on its own in 6 months

😔 female pattern hair loss:
• Gradual thinning, especially at crown and part line
• Genetic
• Can start any time after puberty
• Progressive but treatable

😔 alopecia areata:
• Patchy hair loss
• Autoimmune condition
• Round bald patches
• Can affect any hair-bearing area

😔 traction alopecia:
• From tight hairstyles (braids, ponytails, extensions)
• Preventable by loosening styles

😔 hormonal causes:

PCOS:
• Excess androgens can cause thinning on scalp
• AND excess hair on face/body (hirsutism)
• Other symptoms: irregular periods, acne, weight gain

thyroid issues:
• Both overactive and underactive thyroid affect hair
• Hair may be thin, brittle, or falling out
• Other symptoms: fatigue, weight changes, temperature sensitivity

menopause:
• Estrogen drops
• Hair may become thinner
• May also get facial hair growth

what helps:

🟢 for hair health:
• Gentle handling (don't brush when wet, avoid heat)
• Protein-rich diet (hair is made of protein)
• Iron-rich foods (low iron causes hair loss)
• Biotin (may help if deficient)
• Omega-3s (scalp health)
• Vitamins D and B12
• Scalp massage (increases blood flow)

🟢 medical treatments (doctor prescribed):
• Minoxidil (Rogaine) for female pattern hair loss
• Spironolactone (blocks androgens)
• Birth control pills (regulate hormones)
• Thyroid medication if needed

🟢 for excess facial/body hair:
• Shaving, waxing, threading
• Laser hair removal
• Electrolysis
• Prescription creams (eflornithine)
• Spironolactone (reduces androgens)

when to see a doctor:
• Sudden or patchy hair loss
• Hair loss with other symptoms (irregular periods, fatigue, weight changes)
• Bald spots
• Itching or pain on scalp
• You're worried about it

what hair concerns do you have? Thinning, shedding, or excess growth? 💫"""
    
    def answer_sexual_health_questions(self, question):
        return """💕 understanding sexual health

Sexual health is an important part of overall health. Let's talk about it without embarrassment:

cycle and libido:

🌸 during period:
• Libido varies (some higher, some lower)
• Sex is safe during period (though messier)
• Can help with cramps (orgasm releases feel-good hormones)

🌱 follicular phase (after period):
• Libido increases as estrogen rises
• Natural lubrication increases
• May feel more interested in sex

🌼 ovulation:
• Libido peaks (body's way of encouraging reproduction)
• Highest fertility
• May feel most attracted to partners

🍂 luteal phase (before period):
• Libido may decrease
• May feel less interested
• Physical discomfort (bloating, tenderness) can affect desire

common sexual health concerns:

😔 low libido:
• Can be hormonal (birth control, antidepressants)
• Stress and fatigue (major factors)
• Relationship issues
• Body image concerns
• Pain during sex
• Normal to fluctuate

🩹 pain during sex:
• Can be from lack of lubrication
• Vaginismus (muscles tighten involuntarily)
• Endometriosis
• Pelvic inflammatory disease
• Ovarian cysts
• Infections
• ALWAYS worth discussing with doctor

🩺 vaginal discharge:
• Normal discharge changes throughout cycle
• Clear and stretchy at ovulation (like egg white)
• Thicker and white before period
• Signs of infection: unusual color (green, gray), strong smell, itching, burning

common infections:

🦠 yeast infection:
• Thick, white, cottage-cheese discharge
• Itching and burning
• Redness and swelling
• Triggers: antibiotics, high sugar, hormones, tight clothing
• Treatment: over-the-counter antifungal creams or suppositories

🦠 bacterial vaginosis (BV):
• Thin, gray or white discharge
• Fishy odor (worse after sex)
• Usually no itching
• Treatment: prescription antibiotics

🦠 UTIs (urinary tract infections):
• Burning when peeing
• Urgent need to pee
• Pees small amounts frequently
• Cloudy or bloody urine
• Treatment: antibiotics, drink water

🦠 STIs (sexually transmitted infections):
• Can have no symptoms!
• Unusual discharge, sores, bumps, pain
• Get tested regularly if sexually active

protection and prevention:
• Condoms (protect against STIs and pregnancy)
• Dental dams for oral sex
• Regular testing
• Communicate with partners
• HPV vaccine (prevents cervical cancer)

when to see a doctor:
• Pain during sex
• Unusual discharge or odor
• Sores, bumps, or blisters
• Burning with urination
• Missed period
• Concern about STI exposure
• For regular check-ups (annual exam, Pap smear)

any specific questions? I'm here to help without judgment 💕"""
    
    def answer_birth_control_questions(self, question):
        return """💊 understanding birth control

There are many options. Here's what you should know:

hormonal methods:

💊 combination pill:
• Contains estrogen and progestin
• Take daily at same time
• 91-99% effective with perfect use
• Can regulate periods, reduce cramps, improve acne
• Side effects: nausea, breast tenderness, mood changes
• Not for smokers over 35 or those with migraine with aura

💊 progestin-only pill (mini-pill):
• Take daily at same time (3 hour window)
• Good for those who can't take estrogen
• May have irregular bleeding
• 91-99% effective

💉 Depo-Provera shot:
• Shot every 3 months
• 94-99% effective
• May cause weight gain
• Can take months to get pregnant after stopping

💍 vaginal ring (NuvaRing):
• Insert for 3 weeks, remove for 1 week
• 91-99% effective
• Changed monthly
• Similar to pill hormones

💊 implant (Nexplanon):
• Small rod in arm
• Lasts up to 5 years
• 99% effective
• May have irregular bleeding

🛡️ hormonal IUD (Mirena, Kyleena, Liletta, Skyla):
• T-shaped device in uterus
• Lasts 3-7 years depending on brand
• 99% effective
• Periods often become lighter or stop

non-hormonal methods:

🛡️ copper IUD (Paragard):
• No hormones
• Lasts up to 10-12 years
• 99% effective
• Can make periods heavier and more crampy
• Can be used as emergency contraception

🛡️ barrier methods:
• Condoms (male and female) - 82-98% effective, protect against STIs
• Diaphragm - needs fitting, used with spermicide
• Cervical cap
• Sponge

🛡️ fertility awareness:
• Tracking cycle to avoid sex on fertile days
• Requires strict tracking (temperature, cervical mucus)
• 76-88% effective with typical use
• Good for those who can't use hormones

🛡️ withdrawal (pulling out):
• 78-96% effective
• Risky (pre-cum can contain sperm)

🛡️ sterilization:
• Tubal ligation (tubes tied)
• Essure (coils in tubes, not available in all countries)
• Vasectomy for men
• Permanent

emergency contraception:

🆘 Plan B (levonorgestrel):
• Take within 72 hours (sooner = better)
• Available over-the-counter
• Works by delaying ovulation
• Less effective if over 165 lbs

🆘 Ella (ulipristal acetate):
• Prescription only
• Works up to 5 days
• More effective than Plan B
• Works closer to ovulation

🆘 Copper IUD:
• Inserted within 5 days
• Most effective option (99.9%)
• Provides ongoing contraception

choosing a method:
• Consider effectiveness, side effects, convenience, cost
• Think about future pregnancy plans
• Discuss with healthcare provider
• It's okay to try and switch!

questions to ask yourself:
• Do I want hormones?
• How long do I want protection?
• Am I good at taking daily pills?
• Do I need STI protection (condoms)?
• What are the side effects?
• What's my budget?

always discuss with your healthcare provider to find what's right for YOU 💕"""
    
    def answer_doctor_questions(self, question):
        return """🩺 when to see a doctor

It's hard to know when something needs medical attention. Here's a guide:

for periods:

🩸 see a doctor if:
• No period for 3+ months (and not pregnant)
• Bleeding between periods
• Soaking through pad/tampon every 1-2 hours
• Periods less than 21 days or more than 35 days apart
• Severe pain that OTC meds don't help
• Suddenly much heavier or more painful than usual
• Periods lasting more than 7 days
• Large clots (bigger than a quarter)

for pain:

🤕 see a doctor if:
• Pain that stops daily activities
• New pain after age 25
• Pain with fever or vomiting
• Pain during sex
• Pain that wakes you at night
• Pain with unexplained weight loss
• Pain after injury

for breast health:

🩺 see a doctor if:
• New lump (especially if hard, doesn't move)
• Lump that doesn't go away after period
• Skin changes: dimpling, puckering, redness
• Nipple discharge (especially if bloody)
• Nipple turning inward
• Rash on breast
• Swelling in armpit
• Persistent pain in one spot

for general health:

❤️ see a doctor if:
• Unexplained weight loss or gain
• Unexplained fever
• Lump anywhere
• Changes in moles (ABCDE: asymmetry, border, color, diameter, evolving)
• Persistent cough or hoarseness
• Changes in bowel or bladder habits
• Extreme fatigue lasting weeks
• Shortness of breath
• Chest pain
• Severe headache

for mental health:

🧠 see a doctor if:
• Feeling sad, anxious, or hopeless for 2+ weeks
• Loss of interest in things you loved
• Changes in appetite or sleep
• Thoughts of self-harm
• Can't do daily activities
• Using substances to cope
• Panic attacks
• Hearing voices or seeing things

for sexual health:

💕 see a doctor if:
• Pain during sex
• Unusual discharge (color, smell, amount)
• Sores, bumps, or blisters
• Burning with urination
• Missed period
• Concern about STI exposure
• Irregular bleeding

for preventive care:

🌸 recommended schedule:
• Annual well-woman visit (yearly)
• Pap smear: starting at 21, then every 3-5 years
• HPV test: starting at 30, every 5 years with Pap
• Breast exams: clinical exam yearly, self-exams monthly
• STD testing: if sexually active (yearly or with new partners)
• Blood pressure check (yearly)
• Cholesterol screening: starting at 20, then every 4-6 years
• Diabetes screening: based on risk factors
• Vaccinations: HPV, flu, Tdap, etc.

questions to ask your doctor:
• "Is this normal for someone my age?"
• "What tests do you recommend?"
• "How often should I come back?"
• "What symptoms should I watch for?"
• "Are there lifestyle changes I should make?"
• "What are the side effects of this medication?"

trust your gut! If something feels wrong, get it checked. Better to be safe.

what specific symptom are you worried about? 💕"""
    
    def answer_general(self, question):
        return """🌸 i'm here to help!

I can answer questions about all aspects of women's health:

period & menstrual health:
• Period pain and cramps
• Irregular cycles
• Heavy bleeding
• PMS and PMDD
• Missed or late periods
• Spotting between periods

physical health:
• Fatigue and low energy
• Headaches and migraines
• Sleep problems
• Skin issues (acne, breakouts)
• Weight concerns
• Digestive issues (bloating, nausea)
• Breast health
• Hair changes

reproductive health:
• Pregnancy and fertility
• Birth control options
• Sexual health
• STIs and infections
• When to see a doctor

mental wellness:
• Mood swings
• Anxiety and stress
• Depression
• Emotional health

just ask me anything - i'm here to listen and help!

what's on your mind today? 💕

remember: i provide general information, not medical advice. always consult a healthcare provider for personal concerns."""

# Initialize AI
ai = UltraSmartWomenHealthAI()

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
    print(f"🚀 Starting ultra smart women's health AI on port {port}")
    app.run(host='0.0.0.0', port=port)