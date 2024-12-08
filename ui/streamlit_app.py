import streamlit as st
from src.data_loader import BlogDataLoader
from src.post_generator import PostGenerator


class StreamlitUI:
    def __init__(self):
        self.blog_loader = BlogDataLoader()
        self.post_generator = PostGenerator()

    def display_blog_content(self, content):
        """Display blog content in a structured format."""
        if isinstance(content, dict):
            for section, content in content.items():
                st.subheader(section.replace("_", " ").title())
                if isinstance(content, list):
                    for item in content:
                        st.write(f"• {item}")
                elif isinstance(content, dict):
                    for key, value in content.items():
                        st.write(f"**{key}**: {value}")
                else:
                    st.write(content)

    def show_existing_posts(self):
        """Display existing blog posts."""
        st.header("Existing LinkedIn Posts")
        blogs = self.blog_loader.load_blog_posts()

        for blog in blogs:
            with st.expander(blog["title"]):
                self.display_blog_content(blog["content"])
                st.write("\n**Hashtags:**")
                st.write(" ".join(blog["hashtags"]))

    def show_post_generator(self):
        """Show post generation interface."""
        st.header("Generate New LinkedIn Post")

        if st.button("Generate Post"):
            try:
                with st.spinner(
                    "Generating new post... This might take a few moments."
                ):
                    st.info("Connecting to Groq API...")
                    new_post = self.post_generator.generate_post()
                    st.success("New post generated!")

                    lines = new_post.split("\n")

                    st.header(lines[1])  # Display title

                    content_text = "\n".join(
                        [line for line in lines[3:] if not line.startswith("#")]
                    )
                    st.write(content_text)

                    hashtags = " ".join(
                        [line for line in lines if line.startswith("#")]
                    )
                    st.write(hashtags)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    def run(self):
        """Run the Streamlit application."""
        st.title("LinkedIn Post Generator 📝")
        st.write("Explore existing posts or generate new ones!")

        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", ["Existing Posts", "Generate New Post"])

        if page == "Existing Posts":
            self.show_existing_posts()
        else:
            self.show_post_generator()
