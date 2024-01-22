from flask import render_template, jsonify
from app.chat_gpt_service import ChatGPTService

def get_index():
    return render_template('index.html', title='Index')

def post_question(req):
    question = req.get('question')
    chat_gpt_service = ChatGPTService()
    response = chat_gpt_service.get_conversation(question)
    return jsonify({'response': response})