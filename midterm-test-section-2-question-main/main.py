"""Main application entry point for LangChain router demo."""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from mock_tools import FakeWeatherSearchTool, FakeCalculatorTool, FakeNewsSearchTool
from router import ConversationRouter


def main():
    print("🚀 LangChain Application Main")
    print("=" * 40)
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    # Check if API key is available
    if not os.getenv("GOOGLE_API_KEY"):
        print("⚠️  No Google API key found. Using mock responses only.")
    
    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    # Initialize tools
    tools = [
        FakeWeatherSearchTool(),
        FakeCalculatorTool(),
        FakeNewsSearchTool()
    ]
    
    # Initialize router
    router = ConversationRouter(llm, tools)
    
    print("Type 'exit' to quit.")
    while True:
        query = input("\n💬 You: ")
        if query.strip().lower() == "exit":
            print("👋 Goodbye!")
            break
        response = router.process_message(query)
        print(f"🤖 Assistant: {response}")

if __name__ == "__main__":
    main()
