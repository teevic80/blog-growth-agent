# main.py
import json
from workflows.blog_workflow import run_blog_workflow
from dotenv import load_dotenv

load_dotenv()

def load_input(file_path="data/sample_input.json"):
    with open(file_path, "r") as f:
        return json.load(f)

def main():
    config = load_input()
    result = run_blog_workflow(config)
    print("Running blog workflow...")
    print("✅ Final Result:\n", result)

if __name__ == "__main__":
    main()
