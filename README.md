# 🤖 Chatbot — Neural Network Chatbot using TensorFlow & Flask

A simple **Neural Network (NN)-based chatbot** built in **Python**, trained using **TensorFlow** and deployed locally using **Flask**.  
This chatbot responds to user messages based on trained conversational intents and can be easily run on your machine.

---

## 🧠 Features

- 🗨️ Conversational chatbot powered by a neural network  
- 📦 Trained using **TensorFlow**  
- 🚀 Served locally via a **Flask web app**  
- 🔌 Easy to extend with more intents  
- 🛠 Uses NLP preprocessing and intent classification  

---

## 🛠 Prerequisites

Make sure you have the following installed:
- Python 3.8+
- pip (Python package installer)

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/ShreedharG/Chatbot.git
cd Chatbot
```

Create and activate a virtual environment (recommended):

Linux / macOS
```bash
python -m venv venv
source venv/bin/activate
```

Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```
---

## ▶️ Running the Chatbot

Start the Flask application:
```bash
python app.py
```

The chatbot will be available at localhost.

Open this URL in your browser to interact with the chatbot.
---

## 🧪 Training the Model (Optional)

If you want to retrain the chatbot with updated intents:

Modify intents.json with new patterns and responses.

Run the training script:
```bash
python nlp_model.py
```
This will generate updated model and tokenizer files.

---

## 💡How It Works

- User input is tokenized and cleaned using NLP techniques
- Input is vectorized using a bag-of-words approach
- A neural network predicts the intent class
- A response is selected from the predicted intent
- Flask serves the chatbot through a web interface
---

## 📌Use Cases

- Learning NLP and neural networks
- Academic mini-project
- Base template for intent-based chatbots
- Backend chatbot logic for web applications
---

## 🙌Contributing

Contributions are welcome!
Open a Pull Request

---

## 📁 Repository Structure

```plaintext
.
├── static/
├── templates/
├── app.py              # Flask app
├── chatbot.py          # Chatbot logic & response generation
├── chatbot_model.h5    # Trained neural network model
├── classes.pkl         # Label encoder classes
├── db_helper.py        # Database helper (if used)
├── function.py         # Utility/helper functions
├── intents.json        # Intent definitions (training data)
├── nlp_model.py        # NLP preprocessing & model training
├── requirements.txt    # Python dependencies
├── welcome_msg.txt     # Startup / welcome message
├── words.pkl           # Tokenized vocabulary
└── README.md
```
