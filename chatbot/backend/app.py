from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

# Hypothesis context
HYPOTHESIS_CONTEXT = """
Our hypothesis is about the 2025 Himalayan glacier melt due to unusual El Niño events.
The research focuses on glacier acceleration, SAR imaging data analysis, and flood risk prediction.
Key findings involve log residuals, accumulated moisture, and glacier response to rainfall.
"""

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("question", "")

    prompt = f"""
You are an expert assistant. Answer questions ONLY based on the following hypothesis context:

{HYPOTHESIS_CONTEXT}

User question: {user_input}
Answer concisely and clearly:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.3
    )

    answer = response.choices[0].message["content"]
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
