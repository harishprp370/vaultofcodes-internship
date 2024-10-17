import os
import openai
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
import json
import time



# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Features page route
@app.route('/features')
def features():
    return render_template('features.html')

# Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')
# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize feedback storage
feedback_data = []

def get_openai_response(prompt):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",  # You can change this to a different engine if needed
                prompt=prompt,
                max_tokens=150,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            if "Rate limit" in str(e):
                if attempt < max_retries - 1:
                    time.sleep(20)  # Wait for 20 seconds before retrying
                else:
                    return "I apologize, but I'm currently experiencing high demand. Please try again later."
            else:
                return f"An error occurred: {str(e)}"

def answer_question(question):
    prompt = f"Answer the following question: {question}"
    return get_openai_response(prompt)

def summarize_text(text):
    prompt = f"Summarize the following text:\n\n{text}"
    return get_openai_response(prompt)

def generate_creative_content(prompt_text):
    prompt = f"Generate creative content based on this prompt: {prompt_text}"
    return get_openai_response(prompt)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    user_input = ""
    selected_function = ""

    if request.method == 'POST':
        selected_function = request.form.get('function')
        user_input = request.form.get('user_input')

        if selected_function == 'answer':
            response = answer_question(user_input)
        elif selected_function == 'summarize':
            response = summarize_text(user_input)
        elif selected_function == 'creative':
            response = generate_creative_content(user_input)
        else:
            response = "Invalid function selected."

    return render_template('index.html', response=response, user_input=user_input, function=selected_function)

@app.route('/feedback', methods=['POST'])
def feedback():
    helpful = request.form.get('helpful')
    user_input = request.form.get('user_input')
    response = request.form.get('response')
    function = request.form.get('function')

    feedback_entry = {
        'helpful': helpful,
        'user_input': user_input,
        'response': response,
        'function': function
    }
    feedback_data.append(feedback_entry)

    # Save feedback to a JSON file
    with open('feedback.json', 'w') as f:
        json.dump(feedback_data, f, indent=4)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)