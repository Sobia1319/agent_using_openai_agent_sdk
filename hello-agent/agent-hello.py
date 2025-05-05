import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

def my_first_agent():
    """
    A simple Hello World agent function using OpenAI Agent SDK with Gemini
    """
    # Get API key from environment variables
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        return
    
    # Configure the Gemini API
    genai.configure(api_key=api_key)
    
    # Use Gemini to create a simple response
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        "Say 'Hello, World!' and introduce yourself as my first agent."
    )
    
    # Print the response
    print("Agent Response:")
    print(response.text)

def main():
    """
    Main function to run the agent
    """
    print("Running Hello World Agent with Gemini...")
    my_first_agent()
    print("Agent execution completed.")

if __name__ == "__main__":
    main()