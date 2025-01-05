def backendCode():
    return"""
from flask import Flask, request, jsonify, render_template
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI_Service')))
from AIResponse import  get_gemini_response

app = Flask(__name__, template_folder="../Frontend/templates", static_folder="../Frontend/static")


@app.route('/')
def home():
    return render_template('index.html')

    
@app.route('/api/aiResponse',methods=['POST'])
def text_response():
    data = request.get_json()
    input = data['Userinput']
    print("User Input",input)
    
    response = get_gemini_response(input)
    print(response)
    return jsonify({'botResponse':response})
    
if __name__ == "__main__":
    app.run(debug=True)
"""
