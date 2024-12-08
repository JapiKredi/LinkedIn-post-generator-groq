import json
import os
from typing import List, Dict
from src.config import DATA_DIR


class BlogDataLoader:
    @staticmethod
    def load_blog_posts() -> List[Dict]:
        """Load blog posts from JSON file."""
        try:
            with open(os.path.join(DATA_DIR, "blog_posts.json"), "r") as f:
                data = json.load(f)
                return data["posts"]
        except Exception as e:
            raise Exception(f"Error loading blog posts: {str(e)}")
