from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from meal_planner.tasks.research_task import research_task
from meal_planner.tasks.meal_plan_task import meal_plan_task


def create_meal_plan(goal, preferences):
    """
    This function will be used by Flask to generate a meal plan.
    """

    # Update task descriptions dynamically based on form input
    research_task.description = (
        f"Research the best foods based on the user's fitness goal: {goal}. "
        f"Consider dietary preferences: {preferences}."
    )

    meal_plan_task.description = (
        f"Using the research findings, create a detailed 7-day meal plan "
        f"for a user whose goal is '{goal}' and food preferences are '{preferences}'."
    )

    # Build the crew
    crew = Crew(
        agents=[
            research_task.agent,
            meal_plan_task.agent
        ],
        tasks=[research_task, meal_plan_task],
        verbose=True
    )

    # Run CrewAI workflow
    result = crew.kickoff()

    # Always convert result to string for Flask template
    return str(result)
