import os
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Groq settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "mixtral-8x7b-32768"

# Generation settings
MODEL_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 0.95,
}

# Prompt template
BLOG_GENERATION_PROMPT = """Based on the following LinkedIn tech blog topics, generate a new, unique LinkedIn blog post about AI or technology:

Topics:
- Model Context Protocol
- AWS and hallucinations in LLMs
- Claude model updates
- AI reasoning and development

Generate a professional LinkedIn post with:
1. An engaging title
2. Main content
3. Relevant hashtags

Your response should be well-structured and professional."""
