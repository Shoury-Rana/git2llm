from flask import Flask, request, render_template
import subprocess
import os
import shutil

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""

    if request.method == "POST":
        repo_url = request.form.get("repo_url")
        folder_name = "operations/temp_repo"

        if os.path.exists(folder_name):
            shutil.rmtree(folder_name)

        try:
            subprocess.run(["git", "clone", repo_url, folder_name], check=True)
            output = f"Cloned {repo_url} successfully"
        except subprocess.CalledProcessError as e:
            output = f"Error: {e}"

    return render_template("index.html", output=output)
