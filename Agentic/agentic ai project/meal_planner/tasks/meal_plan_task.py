from crewai import Task
from meal_planner.agents.meal_planner import planner

meal_plan_task = Task(
    description="Create a 7-day personalized meal plan.",
    expected_output="A complete weekly meal plan.",
    agent=planner
)
