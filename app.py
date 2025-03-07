from flask import Flask, jsonify, request, render_template
import cohere
import os

app = Flask(__name__)

# Initialize Cohere client with your API Key from environment variables
co = cohere.Client("CfySmSpGWd3Poq7HLi99BL5Mqf1qau40N5eahLSV")

# Serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to interact with the chatbot
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        response = co.generate(
            prompt=user_message,
            temperature=0,
            max_tokens=200
        )
        
        bot_response = response.generations[0].text if response.generations else "Sorry, I didn't understand that."
        return jsonify({'bot_response': bot_response})
    
    except Exception as e:
        print(f"Error in chatbot route: {e}")   
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
