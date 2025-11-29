from flask import Flask, render_template, request
from meal_planner.main import create_meal_plan

app = Flask(
    __name__,
    template_folder="web_app/templates",
    static_folder="web_app/static"
)

# Reload templates automatically without restarting server
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    goal = request.form.get("goal")
    preferences = request.form.get("preferences")

    # Call your meal-planner function
    result = create_meal_plan(goal, preferences)

    # Send result to result.html
    return render_template("result.html", result=result)


if __name__ == "__main__":
    # Use 0.0.0.0 to allow access from phone (optional)
    app.run(debug=True, host="0.0.0.0", port=5000)
