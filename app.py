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
    task = request.form.get("input_task")
    tasks.append(task)
    # Send the user back to the index page.
    return redirect(url_for("index"))

