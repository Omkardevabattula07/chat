# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Initialize chatbot
chatbot = ChatBot(
    "SimpleBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///db.sqlite3",
)

# Train chatbot (only runs once)
trainer = ListTrainer(chatbot)

training_data = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm good. How can I help you?",
    "What is AI?",
    "AI stands for Artificial Intelligence, which simulates human intelligence in machines.",
    "Who created Django?",
    "Django was created by Adrian Holovaty and Simon Willison in 2003.",
    "What is Python?",
    "Python is a programming language known for its simplicity and readability.",
    "Tell me a joke",
    "Why don’t skeletons fight each other? They don’t have the guts!",
]

trainer.train(training_data)

# View for chatbot page
def chatbot_view(request):
    return render(request, "chatbot.html")

# API to get chatbot response
def get_response(request):
    user_message = request.GET.get("message")
    response = chatbot.get_response(user_message)
    return JsonResponse({"answer": str(response)})
