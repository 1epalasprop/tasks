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


# The Delete link sends the user to the `/delete/`
# page followed by an integer.
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks.pop(task_id)
    # Send the user back to the index page.
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)
