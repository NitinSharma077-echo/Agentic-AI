from crewai import Agent

planner = Agent(
    role="Meal Planner",
    goal="Create personalized 7-day meal plans.",
    backstory="You are a certified dietician and expert meal planner.",
    verbose=True
)
