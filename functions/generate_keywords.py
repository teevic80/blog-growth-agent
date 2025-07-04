from tools.search_tool import search_tool
import json

def generate_keywords(agent, config, region):
    query = f"{config['industry']} services in {region}"
    search_results = search_tool(query)
    search_snippets = "\n".join(search_results)

    prompt = f"""
    Based on the following search results, generate SEO keyword suggestions for a {config['industry']} business in {region}:

    Search Results:
    {search_snippets}

    Return keywords in the following JSON format:
    {{
        "search_intent_keywords": [...],
        "short_tail_keywords": [...],
        "long_tail_keywords": [...],
        "related_keywords": [...],
        "region_specific_keywords": [...]
    }}
    """

    raw_output = agent.run(prompt)

    try:
        keywords = json.loads(raw_output)
    except Exception:
        keywords = {"error": "Failed to parse OpenAI output", "raw": raw_output}

    return {
        "client": config["client"],
        "industry": config["industry"],
        "region": region,
        "keywords": keywords,
        "source": search_results
    }
