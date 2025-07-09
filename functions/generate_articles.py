import os
from datetime import datetime

def generate_articles(writer_agent, keyword_data, competitor_data):
    article = writer_agent.run(keyword_data, competitor_data)
    save_article_to_file(article, keyword_data)
    return article

def save_article_to_file(article, keyword_data):
    # Ensure correct folder exists
    folder = "data/blog_articles"
    os.makedirs(folder, exist_ok=True)

    # Handle both cases for keyword_data
    keywords = keyword_data.get("keywords", keyword_data)
    try:
        main_keyword = keywords["search_intent_keywords"][0].replace(" ", "_").lower()
    except (KeyError, IndexError):
        main_keyword = "untitled"

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{folder}/article_{main_keyword}_{today}.md"

    if isinstance(article, dict):
        content = article.get("title", "# Untitled Article") + "\n\n" + article.get("content", "")
    else:
        content = article

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"📄 Article saved to {filename}")
