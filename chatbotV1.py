"""
Simple LLM Chatbot - Version 1
A basic chatbot that uses Claude to have conversations
Author: Fernando Mirasol
Date: January 2026
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Claude
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def chat(user_message: str) -> str:
    """
    Send a message to Claude and get a response
    
    Args:
        user_message: The user's input message
        
    Returns:
        Claude's response as a string
    """
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    
    return response.content[0].text

def main():
    """Main conversation loop"""
    
    print("=" * 50)
    print("Simple LLM Chatbot (powered by Claude)")
    print("=" * 50)
    print("Type 'quit' to exit\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Exit condition
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        try:
            # Get response from Claude
            response = chat(user_input)
            print(f"\nClaude: {response}\n")
            
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Please check your API key and try again.\n")

if __name__ == "__main__":
    main()