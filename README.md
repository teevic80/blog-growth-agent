# blog-growth-agent

An AI agent for automating blog content research and distribution workflows. Handles keyword research, content ideation, and publishing pipeline tasks.

## Tech Stack

- **TypeScript**
- **Claude / OpenAI** — LLM backbone for content generation and analysis
- **Node.js**

## Structure

```
├── functions/       # Core agent functions (keyword research, etc.)
├── scripts/         # Standalone test and utility scripts
├── types/           # Shared TypeScript types
```

## Getting Started

```bash
# Install dependencies
npm install

# Add environment variables
cp .env.example .env

# Run a script
npx ts-node scripts/test_keyword.ts
```

## Environment Variables

Create a `.env` file at the root — see `.env.example` for required keys.

## License

MIT
