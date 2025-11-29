from crewai import Agent

researcher = Agent(
    role="Nutrition Researcher",
    goal="Research healthy foods based on user goals and preferences.",
    backstory="You specialize in nutrition science and dietary research.",
    verbose=True
)
