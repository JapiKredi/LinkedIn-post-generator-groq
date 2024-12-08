<<<<<<< HEAD
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from typing import Dict
from src.config import MODEL_ID, MODEL_CONFIG, HF_TOKEN


class LlamaModel:
=======
from groq import Groq
from src.config import GROQ_API_KEY, MODEL_NAME, MODEL_CONFIG


class GroqModel:
>>>>>>> 8ea3ce0 (Initial commit)
    _instance = None

    def __new__(cls):
        if cls._instance is None:
<<<<<<< HEAD
            cls._instance = super(LlamaModel, cls).__new__(cls)
            cls._instance._initialize_model()
        return cls._instance

    def _initialize_model(self):
        """Initialize the model and tokenizer."""
        try:
            print("Loading model and tokenizer...")
            self.tokenizer = AutoTokenizer.from_pretrained(
                MODEL_ID, token=HF_TOKEN, use_fast=True
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                MODEL_ID, token=HF_TOKEN, torch_dtype=torch.float16, device_map="auto"
            )
            print("Model and tokenizer loaded successfully!")
        except Exception as e:
            raise Exception(f"Error initializing model: {str(e)}")

    def generate_completion(self, prompt: str) -> str:
        """Generate completion using Llama model."""
        try:
            # Tokenize the input
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

            # Generate response
            outputs = self.model.generate(
                **inputs,
                max_length=MODEL_CONFIG["max_length"],
                temperature=MODEL_CONFIG["temperature"],
                top_p=MODEL_CONFIG["top_p"],
                top_k=MODEL_CONFIG["top_k"],
                repetition_penalty=MODEL_CONFIG["repetition_penalty"],
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
            )

            # Decode and return the response
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract the generated part (after the prompt)
            generated_text = response[len(prompt) :]

            return generated_text.strip()

        except Exception as e:
            raise Exception(f"Error generating completion: {str(e)}")

    def __del__(self):
        """Cleanup method to free GPU memory."""
        if hasattr(self, "model"):
            del self.model
        if hasattr(self, "tokenizer"):
            del self.tokenizer
        torch.cuda.empty_cache()
=======
            cls._instance = super(GroqModel, cls).__new__(cls)
            cls._instance._initialize_client()
        return cls._instance

    def _initialize_client(self):
        """Initialize the Groq client."""
        try:
            self.client = Groq(api_key=GROQ_API_KEY)
            print("Groq client initialized successfully!")
        except Exception as e:
            raise Exception(f"Error initializing Groq client: {str(e)}")

    def generate_completion(self, prompt: str) -> str:
        """Generate completion using Groq API."""
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=MODEL_NAME,
                temperature=MODEL_CONFIG["temperature"],
                max_tokens=MODEL_CONFIG["max_tokens"],
                top_p=MODEL_CONFIG["top_p"],
            )

            return completion.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"Error generating completion: {str(e)}")
>>>>>>> 8ea3ce0 (Initial commit)
