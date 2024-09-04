from flask import Flask, request, jsonify, render_template, send_from_directory
import openai, os, requests
from uuid import uuid4

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = "<REPLACE_WTIH_YOUR_API_KEY>"  # Replace with your actual API key

# Ensure the static directory exists
if not os.path.exists('static'):
    os.makedirs('static')

def generate_response(user_input):
    try:
        modified_input = "Based on—but not limited to—the following ingredients, give me a recipe that I can create and use emojis as best as you can" + user_input
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": modified_input}
            ],
            max_tokens=200,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return str(e)

# Fill in the prompt with the user input and generate an image
def generate_image(prompt):
    try:
        response = openai.Image.create(
         # Fill in details   
        )
        
    except Exception as e:
        print(f"Error generating image: {e}")  # Log the error for debugging
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return no content, 204 status

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    
    if user_input:
        ai_response = generate_response(user_input)
        image_filename = generate_image(user_input)
        # Fill in image_filename with the actual image filename
        if image_filename:
            
        else:
            
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
