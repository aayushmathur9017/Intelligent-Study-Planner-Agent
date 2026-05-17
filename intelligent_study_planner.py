from langchain import agents
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage


@tool("create_study_plan", description="Create a personalized study plan from a natural language request. The tool should return a structured schedule, study tips, and review steps.")
def create_study_plan(query: str) -> str:
    """Generate a study plan from a student query."""
    # A simple planning helper that can be improved with more parsing logic.
    return (
        "Intelligent Study Planner\n\n"
        "1. Assess goals and deadlines\n"
        "2. Break subjects into focused daily sessions\n"
        "3. Include review and practice time\n\n"
        "Based on your request:\n"
        f"{query}\n\n"
        "Example plan:\n"
        "- Day 1: Review core concepts and create an outline for each subject.\n"
        "- Day 2: Study the first key topic in depth with active recall exercises.\n"
        "- Day 3: Practice problems and summarize summaries.\n"
        "- Day 4: Review previous topics and adjust focus based on weak areas.\n"
        "- Day 5: Complete a mock test or quiz and revise mistakes.\n"
        "- Day 6: Restudy difficult material, and schedule a final review.\n\n"
        "For an intelligent plan, include: subject priorities, available study hours, deadlines, and preferred learning style."
    )


def main() -> None:
    llm = init_chat_model(model="llama3.2:latest", model_provider="ollama")

    agent = agents.create_agent(
        llm,
        tools=[create_study_plan],
        debug=True,
    )

    print("=== Intelligent Study Planner Agent ===")
    print("Enter your study request, or type 'exit' to quit.")

    while True:
        user_input = input("\n> ")
        if user_input.strip().lower() in {"exit", "quit"}:
            break

        try:
            response = agent.invoke({"messages": [HumanMessage(content=user_input)]})
            print("\n" + str(response))
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
