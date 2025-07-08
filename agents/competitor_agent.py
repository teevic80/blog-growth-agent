# agents/competitor_agent.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

class CompetitorResearchAgent:
    def __init__(self, client_name: str, industry: str, region: str, tone: str):
        self.client_name = client_name
        self.industry = industry
        self.region = region
        self.tone = tone

    def run(self, context_snippets: list):
        prompt = f"""
        You are a content marketing analyst for a {self.industry} business in {self.region} called {self.client_name}.
        Your tone should be {self.tone}.

        Based on the following content samples and assumed competitor blogs in this space, generate a report in JSON format that includes:

        1. "top_competitors": [List 3 key competitors by name]
        2. "top_articles": For each competitor, list 1-2 of their top articles with title + URL.
        3. "high_performing_keywords": Top 5 keywords across all competitors (with volume and search intent if known)
        4. "hashtag_opportunities": Suggested hashtags based on trends and content
        5. "content_gaps": Topics that competitors cover poorly or miss completely
        6. "backlink_opportunities": List 3 potential blogs or websites that link to your competitors and could be reached out to

        Context:
        {context_snippets}
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        import json
        try:
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            return {
                "error": "Failed to parse JSON",
                "raw_output": response.choices[0].message.content,
                "exception": str(e)
            }

def get_competitor_agent(client_name: str, industry: str, region: str, tone: str):
    return CompetitorResearchAgent(client_name, industry, region, tone)
