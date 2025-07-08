# functions/generate_competitor_report.py

from tools.search_tool import search_tool

def generate_competitor_report(agent, industry, region):
    query = f"{industry} blogs in {region}"
    search_results = search_tool(query)
    context = "\n".join(search_results)

    return {
        "client": agent.client_name,
        "industry": industry,
        "region": region,
        "competitor_report": agent.run(context)
    }
