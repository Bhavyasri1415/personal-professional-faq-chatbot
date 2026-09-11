# Personal Professional FAQ Chatbot

A  personal chatbot that answers questions about my education, technical skills, projects, DSA practice, and career interests.

I built this project as a small portfolio application to make my professional profile more interactive and easier to explore.

## Features

* Answers questions about my education and technical background
* Provides information about programming skills and Java experience
* Describes my projects and technical work
* Shares information about my DSA practice
* Provides information about my career interests
* Includes suggested questions for quick interaction
* Maintains chat history during the session
* Simple web interface built with Streamlit

## How It Works

The chatbot uses a rule-based NLP approach.

```text
User Question
     ↓
Streamlit Interface
     ↓
Text Preprocessing
     ↓
Pattern Matching
     ↓
FAQ Response
     ↓
Chatbot Reply
```

The user's question is first processed using NLTK. Regular expressions are then used to match the question against predefined FAQ patterns. When a matching pattern is found, the chatbot returns the corresponding response.

If no pattern matches the question, a default response is provided.

## Technologies Used

* Python
* NLTK
* Regular Expressions (Regex)
* Streamlit

## Project Structure

```text
personal-faq-chatbot/
│
├── app.py
├── chatbot.py
├── intents.py
├── utils.py
├── requirements.txt
└── README.md
```

### File Description

**app.py**
Contains the Streamlit user interface and manages the chat interaction.

**chatbot.py**
Contains the main chatbot logic and pattern matching.

**intents.py**
Contains the FAQ patterns and their corresponding responses.

**utils.py**
Handles NLTK setup and basic text preprocessing.

**requirements.txt**
Contains the Python dependencies required to run the project.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/personal-professional-faq-chatbot.git
```

### 2. Open the project directory

```bash
cd personal-professional-faq-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the application

```bash
streamlit run app.py
```

The application will open in the browser.

## Example Questions

Some questions the chatbot can answer:

* Who is Bhavya?
* What are her technical skills?
* How many DSA problems has she solved?
* Tell me about her projects.
* Tell me about her API Rate Limiter.
* What are her career interests?
* What technologies does she use?

## Why I Built This

I wanted to build a project that was simple enough to understand completely but also had a practical use case.

Instead of creating a generic FAQ chatbot, I used my own professional profile as the knowledge source. This helped me practice Python, NLP preprocessing, regular expressions, and Streamlit while building something that can also be used as a personal portfolio project.

## Future Improvements

I plan to improve the chatbot by exploring:

* TF-IDF and cosine similarity for better question matching
* Semantic search using embeddings
* Vector database integration
* RAG-based responses
* Resume and project document integration
* Better handling of differently worded questions
* Online deployment

## Author

**Bhavya Sri**

Final-year B.Tech CSE student specializing in AI/ML, interested in Java development, backend engineering, software development, and AI/ML applications.

---

This project is part of my personal portfolio and is intended to demonstrate practical programming, NLP, and application development skills.
