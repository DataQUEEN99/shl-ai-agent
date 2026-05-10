import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")


def generate_reply(user_query, recommendations):

    try:

        prompt = f"""
        User Query:
        {user_query}

        Recommendations:
        {recommendations}

        Explain professionally why these SHL assessments are suitable.
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Gemini Error: {str(e)}"