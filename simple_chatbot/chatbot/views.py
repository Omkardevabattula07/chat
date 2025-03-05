
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os

# Create chatbot instance
chatbot = ChatBot(
    "PersonalBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///chatbot.sqlite3"
)

# Train chatbot with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Train chatbot with custom data
training_data_path = os.path.join(os.path.dirname(__file__), "../chatbot_training/training_data.yml")

if os.path.exists(training_data_path):
    with open(training_data_path, "r") as file:
        training_data = file.readlines()
        trainer = ListTrainer(chatbot)
        trainer.train(training_data)

# Chatbot Response Function
def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("question", "")
        answer = chatbot.get_response(user_input).text
        return JsonResponse({"answer": answer})
    
    return render(request, "chatbot.html")
