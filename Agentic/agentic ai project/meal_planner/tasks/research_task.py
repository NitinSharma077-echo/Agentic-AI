from crewai import Task
from meal_planner.agents.nutrition_researcher import researcher

research_task = Task(
    description="Research foods based on user goal and preferences.",
    expected_output="Detailed nutrition research results.",
    agent=researcher
)
