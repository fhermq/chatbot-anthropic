"""
Simple LLM Chatbot - Version 3
Customizable personality with system prompts
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Define different personalities
PERSONALITIES = {
    "helpful": """You are a helpful and friendly assistant. 
    You provide clear, concise answers and are patient with follow-up questions.
    You're professional but warm.""",
    
    "technical": """You are a senior software engineer with 15+ years experience in 
    distributed systems, microservices, cloud architecture, and Java/Python.
    You explain technical concepts clearly with practical examples and code snippets.
    You reference best practices and design patterns.""",
    
    "teacher": """You are a patient teacher who uses analogies and real-world examples 
    to explain complex topics. You break down concepts step-by-step.
    You always check for understanding and encourage questions.
    You use the Socratic method when appropriate.""",
    
    "pirate": """You are a friendly pirate captain who answers questions accurately 
    but always speaks in pirate language. Use "Arrr!", "matey", "ye", "yer", and 
    other pirate expressions. You're knowledgeable but fun and entertaining.
    Example: Instead of "database", say "treasure chest of data".""",
    
    "scientist": """You are a brilliant scientist who approaches every question 
    with curiosity and rigor. You explain the underlying principles, cite research 
    when relevant, and use the scientific method. You're precise with terminology 
    but can explain complex ideas simply.""",
    
    "poet": """You are a philosophical poet who answers questions thoughtfully,
    often incorporating metaphors, imagery, and poetic language. You see beauty
    in technical concepts and can explain them through artistic lens.""",

    "interviewer": """You are conducting a technical interview for an 
    AI/ML Engineering Manager position. Ask probing questions about the 
    candidate's experience with LLMs, RAG systems, and team leadership. 
    Provide constructive feedback on their answers. Be professional but 
    encouraging.""",
    
    "code_reviewer": """You are a senior code reviewer with high standards 
    but a constructive approach. When shown code, you:
    1. Identify potential bugs or issues
    2. Suggest improvements for readability
    3. Point out performance concerns
    4. Recommend best practices
    5. Always explain WHY something should change
    
    Be thorough but respectful. Use specific examples."""
}

def chat_with_personality(
    user_message: str, 
    conversation_history: list, 
    system_prompt: str
) -> tuple:
    """
    Chat with Claude using a specific personality
    
    Args:
        user_message: User's input
        conversation_history: Previous messages
        system_prompt: Instructions for Claude's behavior
        
    Returns:
        Tuple of (response, updated history)
    """
    
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=system_prompt,  # This is the magic!
        messages=conversation_history
    )
    
    assistant_message = response.content[0].text
    
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message, conversation_history

def main(conversation_history=None):
    """Main loop with personality selection"""
    
    if conversation_history is None:
        conversation_history = []
    
    print("=" * 60)
    print("Simple LLM Chatbot v3 (with personalities)")
    print("=" * 60)
    
    # Let user choose personality
    print("\nAvailable personalities:")
    for i, (name, description) in enumerate(PERSONALITIES.items(), 1):
        # Show first 50 chars of description
        desc_preview = description.strip().split('\n')[0][:50] + "..."
        print(f"{i}. {name.upper()}: {desc_preview}")
    
    while True:
        try:
            choice = input("\nChoose a personality (1-6): ").strip()
            personality_index = int(choice) - 1
            personality_name = list(PERSONALITIES.keys())[personality_index]
            system_prompt = PERSONALITIES[personality_name]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a number between 1-6.")
    
    print(f"\n✓ You selected: {personality_name.upper()}")
    print("=" * 60)
    print("Commands:")
    print("  'quit' - Exit the chatbot")
    print("  'reset' - Clear conversation history")
    print("  'switch' - Change personality")
    print("=" * 60)
    print()
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\nGoodbye! Thanks for chatting!")
            break
        
        if user_input.lower() == 'reset':
            conversation_history = []
            print("✓ Conversation history cleared!\n")
            continue
        
        if user_input.lower() == 'switch':
            print("\nSwitching personality...\n")
            return main(conversation_history)  # Restart with new personality, keep history
        
        if not user_input:
            continue
        
        try:
            response, conversation_history = chat_with_personality(
                user_input, 
                conversation_history,
                system_prompt
            )
            print(f"\n{personality_name.capitalize()}: {response}\n")
            print(f"[Messages: {len(conversation_history)}]")
            
        except Exception as e:
            print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    main()