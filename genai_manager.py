import google.generativeai as genai
import logging
from config import GOOGLE_API_KEY, MODEL_NAME

logger = logging.getLogger(__name__)

class GenAIManager:
    def __init__(self):
        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            self.model = genai.GenerativeModel(MODEL_NAME)
            logger.info("GenAI Manager initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize GenAI Manager: {str(e)}")
            raise

    def generate_response_sync(self, message: str) -> str:
        """
        Generate a response using the Gemini model (synchronous version)
        
        Args:
            message (str): Input message from user
            
        Returns:
            str: Generated response
        """
        try:
            response = self.model.generate_content(message)
            return response.text
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error processing your request."