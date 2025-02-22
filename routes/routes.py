import sqlite3
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request

from models import *
from repositories import *
from services.ChatBotService import ChatBotService

opel_routes = Blueprint('opel_routes', __name__)

@opel_routes.route('/srekja', methods=['GET'])
def srekja():
    prompt = ChatBotService.AskTheChatBot("Наброј ми 10 македонски кошаркари")
    print(prompt)
    return prompt

@opel_routes.route('/chat', methods=['POST', 'GET'])
def chat():
    data = request.get_json()

    # Extract user message from the request
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Get a response from the AI bot
    bot_response = ChatBotService.AskTheChatBot(user_message)

    # Return the response as JSON
    return jsonify({'response': bot_response}), 200