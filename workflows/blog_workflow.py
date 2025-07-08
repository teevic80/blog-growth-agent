# workflows/blog_workflow.py

from agents.keyword_agent import get_keyword_agent
from agents.competitor_agent import get_competitor_agent
from functions.generate_keywords import generate_keywords
from functions.generate_competitor_report import generate_competitor_report

def run_blog_workflow(config: dict):
    print("🛠️ Inside run_blog_workflow with config:", config)

    client = config["client"]
    industry = config["industry"]
    region = config["region"]
    tone = config.get("tone", "Neutral")

    print("Running blog workflow...")

    keyword_agent = get_keyword_agent(client, industry, region, tone)
    keywords = generate_keywords(keyword_agent, config, region)

    competitor_agent = get_competitor_agent(client, industry, region, tone)
    competitor_report = generate_competitor_report(competitor_agent, industry, region)

    return {
        "client": client,
        "industry": industry,
        "region": region,
        "tone": tone,
        "keywords": keywords,
        "competitor_analysis": competitor_report
    }
