# blog-growth-agent

A multi-agent AI system for automating blog content research and creation. Runs parallel agents for keyword research, competitor analysis, and content writing — orchestrated into a single publishing workflow.

## Tech Stack

- **Python**
- **Claude / OpenAI** — LLM backbone for content generation and analysis

## Structure

```
├── agents/
│   ├── keyword_agent.py      # Keyword research and opportunity analysis
│   ├── competitor_agent.py   # Competitor content analysis
│   └── writer_agent.py       # AI-powered content generation
├── tools/
│   └── search_tool.py        # Web search integration
├── workflows/
│   └── blog_workflow.py      # End-to-end orchestration
├── functions/                # Shared utilities
├── data/                     # Inputs and outputs
└── main.py                   # Entry point
```

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Add environment variables
cp .env.example .env

# Run the workflow
python main.py
```

## Environment Variables

Create a `.env` file at the root — see `.env.example` for required keys.

## License

MIT
