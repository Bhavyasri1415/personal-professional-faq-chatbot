import re

from intents import faq_patterns
from utils import preprocess_text


def chatbot_response(user_input):
    """
    Process the user's question and find
    the matching FAQ response.
    """

    processed_input = preprocess_text(user_input)

    for pattern, response in faq_patterns.items():

        if re.search(pattern, processed_input):
            return response

    return (
        "I'm sorry, I don't have an answer for that yet. "
        "You can ask me about Bhavya's education, skills, projects, "
        " DSA, AI/ML, Java or career interests."
    )


def start_chat():

    print("=" * 50)
    print("BHAVYA'S PROFESSIONAL ASSISTANT")
    print("=" * 50)

    print("\nYou can ask questions about:")
    print("- Education")
    print("- Technical skills")
    print("- Java")
    print("- DSA")
    print("- Projects")
    print("- AI/ML")
    print("- Career interests")

    print("\nType 'bye' to exit.\n")

    while True:

        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        if re.search(
            r"(bye|goodbye|exit|quit)",
            user_input.lower()
        ):
            break


if __name__ == "__main__":
    start_chat()