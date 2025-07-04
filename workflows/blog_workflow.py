from agents.keyword_agent import get_keyword_agent
from functions.generate_keywords import generate_keywords

def run_blog_workflow(config):
    print("🛠️ Inside run_blog_workflow with config:", config)

    client = config.get("client")
    industry = config.get("industry")
    region = config.get("region")
    tone = config.get("tone", "neutral")

    keyword_agent = get_keyword_agent(client, industry, region, tone)
    keywords = generate_keywords(keyword_agent, config, region)

    return {
        "client": client,
        "industry": industry,
        "region": region,
        "tone": tone,
        "keywords": keywords
    }
