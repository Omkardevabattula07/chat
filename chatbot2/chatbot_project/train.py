# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# chatbot = ChatBot("SimpleBot", storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri="sqlite:///db.sqlite3")

# trainer = ListTrainer(chatbot)

# training_data = [
#     "Hello",
#     "Hi there!",
#     "Who created Django?",
#     "Django was created by Adrian Holovaty and Simon Willison in 2003.",
#     "What is Python?",
#     "Python is a programming language known for its simplicity and readability.",
#     "Tell me a joke",
#     "Why don’t skeletons fight each other? They don’t have the guts!",
# ]

# trainer.train(training_data)

# print("Training complete!")
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "SimpleBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///db.sqlite3",
)

trainer = ListTrainer(chatbot)

training_data = [
    "Hello", "Hi there!",
    "How are you?", "I'm good. How can I help you?",
    "Who are you?", "I'm a chatbot created to assist you.",
    "What is AI?", "AI stands for Artificial Intelligence, which simulates human intelligence in machines.",
    "What is Python?", "Python is a high-level programming language known for its simplicity.",
    "Tell me a joke", "Why don’t skeletons fight each other? They don’t have the guts!",
    "What is Django?", "Django is a Python-based web framework used for building web applications.",
    "Who created Django?", "Django was created by Adrian Holovaty and Simon Willison in 2003.",
    "What is Machine Learning?", "Machine Learning is a subset of AI that allows computers to learn from data.",
    "What is Deep Learning?", "Deep Learning is a type of Machine Learning using neural networks.",
    "What is an API?", "API stands for Application Programming Interface, which allows different software to communicate.",
    "What is the capital of France?", "The capital of France is Paris.",
    "Who is the President of the USA?", "It depends on the current date. You can check the latest news!",
    "What is the largest planet?", "Jupiter is the largest planet in our solar system.",
    "What is 2 + 2?", "2 + 2 equals 4.",
    "What is the speed of light?", "The speed of light is approximately 299,792,458 meters per second.",
    "Who discovered gravity?", "Gravity was discovered by Sir Isaac Newton.",
    "What is photosynthesis?", "Photosynthesis is the process by which plants make food using sunlight.",
    "What is your name?", "My name is SimpleBot!",
    "Who invented the telephone?", "The telephone was invented by Alexander Graham Bell.",
    "What is the boiling point of water?", "Water boils at 100 degrees Celsius or 212 degrees Fahrenheit.",
    "What is the capital of India?", "The capital of India is New Delhi.",
    "Who wrote 'Romeo and Juliet'?", "Romeo and Juliet was written by William Shakespeare.",
    "What is the currency of Japan?", "The currency of Japan is the Japanese Yen.",
    "What is the tallest mountain in the world?", "Mount Everest is the tallest mountain in the world.",
    "Who is Elon Musk?", "Elon Musk is the CEO of Tesla and SpaceX.",
    "What is the periodic table?", "The periodic table is a chart of elements arranged by atomic number.",
    "What is an atom?", "An atom is the smallest unit of matter that retains the properties of an element.",
    "What is quantum physics?", "Quantum physics is the study of matter and energy at the smallest scales.",
    "What is the human brain?", "The human brain is the central organ of the nervous system responsible for thought and memory.",
    "What is the meaning of life?", "The meaning of life is subjective and varies from person to person.",
    "Who is the richest person in the world?", "The richest person changes over time. Check the latest Forbes list!",
    "What is the Big Bang Theory?", "The Big Bang Theory explains the origin of the universe from a singularity.",
    "How far is the Moon?", "The Moon is about 384,400 km away from Earth.",
    "What is cybersecurity?", "Cybersecurity is the practice of protecting systems and data from digital attacks.",
    "What is a blockchain?", "A blockchain is a decentralized digital ledger used for recording transactions securely.",
    "Who is the CEO of Apple?", "Apple's CEO changes over time. The current CEO is Tim Cook (as of 2024).",
    "What is HTML?", "HTML stands for HyperText Markup Language, used for creating web pages.",
    "What is CSS?", "CSS stands for Cascading Style Sheets, used for styling web pages.",
    "What is JavaScript?", "JavaScript is a programming language used for web development.",
    "What is a database?", "A database is an organized collection of data that can be accessed electronically.",
    "What is a computer?", "A computer is an electronic device that processes data.",
    "What is an operating system?", "An operating system is system software that manages hardware and software resources.",
    "What is a programming language?", "A programming language is a set of instructions used to communicate with computers.",
    "Who created Linux?", "Linux was created by Linus Torvalds in 1991.",
    "What is hacking?", "Hacking refers to gaining unauthorized access to computer systems.",
    "What is cloud computing?", "Cloud computing is the delivery of computing services over the internet.",
    "What is a URL?", "A URL (Uniform Resource Locator) is the address of a web page.",
    "What is IoT?", "IoT (Internet of Things) refers to the network of interconnected devices.",
    "What is a firewall?", "A firewall is a security system that monitors and controls incoming and outgoing network traffic.",
    "What is an IP address?", "An IP address is a unique identifier for a device on a network.",
    "What is a VPN?", "A VPN (Virtual Private Network) encrypts your internet connection for privacy and security.",
    "What is phishing?", "Phishing is a cyber attack where scammers trick people into revealing sensitive information.",
    "What is cryptocurrency?", "Cryptocurrency is a digital currency secured by cryptography.",
]

trainer.train(training_data)

print("Training complete!")
