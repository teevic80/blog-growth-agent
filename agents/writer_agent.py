# agents/writer_agent.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

class BlogWriterAgent:
    def __init__(self, client_name: str, industry: str, region: str, tone: str):
        self.client_name = client_name
        self.industry = industry
        self.region = region
        self.tone = tone

    def run(self, keyword_data: dict, competitor_data: dict) -> dict:
        prompt = f"""
        You are a professional SEO blog writer for a {self.industry} business in {self.region} called {self.client_name}. Write in a {self.tone} tone.

        Based on the following keyword research and competitor analysis, write 3 engaging, SEO-optimized blog article drafts:

        - 2x high-conversion articles: Use short-tail + search intent keywords. Focus on helping users actively seeking help in this industry.
        - 1x competitor article: Use competitor article topics, gaps, and backlink opportunities. Improve on what competitors are doing.

        Keyword Research:
        {keyword_data}

        Competitor Research:
        {competitor_data}

        Return a JSON response like:
        {{
            "high_conversion_articles": [
                {{"title": "...", "content": "..."}},
                {{"title": "...", "content": "..."}}
            ],
            "competitor_article": {{
                "title": "...",
                "content": "..."
            }}
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        import json
        try:
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            return {
                "error": "Failed to parse OpenAI response",
                "raw_output": response.choices[0].message.content,
                "exception": str(e)
            }

def get_writer_agent(client_name: str, industry: str, region: str, tone: str):
    return BlogWriterAgent(client_name, industry, region, tone)
