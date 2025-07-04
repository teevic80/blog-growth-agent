# tools/search_tool.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def search_tool(query: str):
    """Use OpenAI to simulate a smart search tool"""
    prompt = f"Give a brief list of relevant search results or insights for: {query}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that returns search-style summaries for user queries."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )

        result = response.choices[0].message.content.strip()
        return [result]

    except Exception as e:
        print(f"❌ Error during OpenAI search: {e}")
        return [f"Search failed for query: {query}"]
