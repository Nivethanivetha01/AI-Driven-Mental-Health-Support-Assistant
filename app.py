from flask import Flask, render_template, request, redirect, url_for, jsonify

import google.generativeai as genai
import os
#P9hDW6wx14vOafyf5zU4h1sGklIxOZg8tT4Ut1q3
# Hugging Face API setup


# Configure the API key for Google Generative AI
os.environ["GOOGLE_API_KEY"] = "AIzaSyC2MZ3x43QiAAyIfrjvK3t5aSj07lXfBrM"  # Replace with your Google API key
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Initialize Flask app
app = Flask(__name__,template_folder='templates')

# Load the model for Gemini API
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

@app.route('/')
def login():
    return render_template('login.html')    

@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

@app.route('/submit_questions', methods=['POST'])
def submit_questions():
    # Collect responses from the form
    responses = {
        'question1': request.form['question1'],
        'question2': request.form['question2'],
        'question3': request.form['question3'],
        'question4': request.form['question4'],
        'question5': request.form['question5'],
        'question6': request.form['question6'],
        'question7': request.form['question7'],
        'question8': request.form['question8'],
        'question9': request.form['question9'],
        'question10': request.form['question10'],
        'question11': request.form['question11'],
        'question12': request.form['question12'],
        'question13': request.form['question13'],
        'question14': request.form['question14'],
        'question15': request.form['question15'],
        'question16': request.form['question16'],
        'question17': request.form['question17'],
        'question18': request.form['question18'],
        'question19': request.form['question19'],
        'question20': request.form['question20'],
    }

    # Initialize score
    score = 0

    # Analyze responses to assess mental health
    for response in responses.values():
        if response == 'Never':
            score += 1
        elif response == 'Rarely':
            score += 2
        elif response == 'Sometimes':
            score += 3
        elif response == 'Often':
            score += 4
        elif response == 'Always':
            score += 5

    # Determine mental health status based on the total score
    if score <= 40:
        result = "Your mental health appears to be in good condition. Keep up your self-care habits and continue monitoring your mental well-being."
    elif score <= 80:
        result = "You may be facing some challenges with your mental health. Consider incorporating more relaxation techniques and speaking with someone you trust."
    else:
        result = "It seems you are experiencing significant mental health challenges. It's important to seek professional support to help navigate these feelings."

    # Render the result page with the calculated result
    return render_template('result.html', result=result)



@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    prompt = (
        f"As a mental health support assistant, how would you respond to the following statement:\n"
        f"User: {user_input}\n"
        #f"Please provide a supportive, empathetic response."
    )
    
    try:
        response = model.generate_content([prompt])
        chat_response = response.text.strip()
    except Exception as e:
        chat_response = f"An error occurred: {str(e)}"

    return jsonify({"response": chat_response})

if __name__ == '__main__':
    app.run(debug=True)
