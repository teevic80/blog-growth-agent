from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()  # Now this reads the API key from the environment

class KeywordResearchAgent(BaseModel):
    client: str
    industry: str
    region: str
    tone: str

    def run(self, prompt: str) -> str:
        """Executes the keyword generation prompt using OpenAI."""
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response.choices[0].message.content


def get_keyword_agent(client: str, industry: str, region: str, tone: str) -> KeywordResearchAgent:
    return KeywordResearchAgent(
        client=client,
        industry=industry,
        region=region,
        tone=tone
    )
