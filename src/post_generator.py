<<<<<<< HEAD
from src.model import LlamaModel
=======
from src.model import GroqModel
>>>>>>> 8ea3ce0 (Initial commit)
from src.config import BLOG_GENERATION_PROMPT


class PostGenerator:
    def __init__(self):
<<<<<<< HEAD
        self.model = LlamaModel()
=======
        self.model = GroqModel()
>>>>>>> 8ea3ce0 (Initial commit)

    def generate_post(self) -> str:
        """Generate a new blog post."""
        try:
            generated_text = self.model.generate_completion(BLOG_GENERATION_PROMPT)

<<<<<<< HEAD
            # Process the generated text to ensure it's properly formatted
            lines = generated_text.split("\n")

            # Extract title, content, and hashtags
            title = None
            content = []
            hashtags = []

            current_section = "content"
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                if not title:
                    title = line
                    continue

                if line.startswith("#"):
                    current_section = "hashtags"
                    hashtags.append(line)
                else:
                    if current_section == "content":
                        content.append(line)

            # Format the post
            formatted_post = f"""Title: {title}

{''.join(content)}

{''.join(hashtags)}"""
=======
            # Process the generated text
            lines = generated_text.split("\n")

            # Format the post
            formatted_post = self._format_post(lines)
>>>>>>> 8ea3ce0 (Initial commit)

            return formatted_post

        except Exception as e:
            raise Exception(f"Error generating post: {str(e)}")
<<<<<<< HEAD
=======

    def _format_post(self, lines: list) -> str:
        """Format the generated post."""
        title = None
        content = []
        hashtags = []

        current_section = "content"
        for line in lines:
            line = line.strip()
            if not line:
                continue

            if not title:
                title = line
                continue

            if line.startswith("#"):
                current_section = "hashtags"
                hashtags.append(line)
            else:
                if current_section == "content":
                    content.append(line)

        formatted_post = f"""Title: {title}

{''.join(content)}

{''.join(hashtags)}"""

        return formatted_post
>>>>>>> 8ea3ce0 (Initial commit)
