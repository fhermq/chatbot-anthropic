"""
Simple LLM Chatbot - Version 2
Now with conversation memory!
Author: Fernando Mirasol
Date: January 2026
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def chat_with_history(user_message: str, conversation_history: list) -> tuple:
    """
    Send a message to Claude with conversation history
    
    Args:
        user_message: The user's input message
        conversation_history: List of previous messages
        
    Returns:
        Tuple of (response text, updated conversation history)
    """
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Call Claude with full conversation history
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=conversation_history
    )
    
    # Extract response
    assistant_message = response.content[0].text
    
    # Add assistant response to history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message, conversation_history

def main():
    """Main conversation loop with memory"""
    
    print("=" * 50)
    print("Simple LLM Chatbot v2 (with memory)")
    print("=" * 50)
    print("Type 'quit' to exit")
    print("Type 'reset' to clear conversation history\n")
    
    # Initialize empty conversation history
    conversation_history = []
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        if user_input.lower() == 'reset':
            conversation_history = []
            print("Conversation history cleared!\n")
            continue
        
        if not user_input:
            continue
        
        try:
            response, conversation_history = chat_with_history(
                user_input, 
                conversation_history
            )
            print(f"\nClaude: {response}\n")
            
            # Show conversation length
            print(f"[Conversation: {len(conversation_history)//2} exchanges]")
            
        except Exception as e:
            print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    main()