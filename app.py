from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple in-memory list to store the tasks
tasks = []


# The landing page.
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


# The form action sends the user to the `/add` page.
@app.route("/add", methods=["POST"])
def add_task():
    today = datetime.today().strftime("%Y-%m-%d")
    task = request.form.get("input_task")
    priority = request.form.get("priority")
    due_date = request.form.get("due_date")
    tasks.append(
        {
            "description": task,
            "done": False,
            "created": today,
            "priority": priority,
            "due_date": due_date,
        }
    )
    # Send the user back to the index page.
    return redirect(url_for("index"))


# The Delete link sends the user to the `/delete/` page followed by an integer.
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks.pop(task_id)
    # Send the user back to the index page.
    return redirect(url_for("index"))


# The Toggle link sends the user to the `/toggle/` page followed by an integer.
@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    tasks[task_id]["done"] = not tasks[task_id]["done"]
    return redirect(url_for("index"))


# The Edit link sends the user to the `/edit/` page followed by an integer.
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        # Update the task with new values
        task = request.form.get("input_task")
        priority = request.form.get("priority")
        due_date = request.form.get("due_date")

        tasks[task_id] = {
            "description": task,
            "done": tasks[task_id]["done"],  # Keep the done status unchanged
            "created": tasks[task_id]["created"],  # Keep the created date unchanged
            "priority": priority,
            "due_date": due_date,
        }
        return redirect(url_for("index"))

    # If GET request, render the edit form with current task details
    task_to_edit = tasks[task_id]
    return render_template("edit_task.html", task=task_to_edit, task_id=task_id)


if __name__ == "__main__":
    app.run(debug=True)
