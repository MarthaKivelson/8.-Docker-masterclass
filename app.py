from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Templates as strings
home_html = """
<!doctype html>
<html>
<head><title>Enter Name</title></head>
<body>
    <h2>Enter your name</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Your name" required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

welcome_html = """
<!doctype html>
<html>
<head><title>Welcome</title></head>
<body>
    <h1>Welcome, {{ name }}!</h1>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("username")
        return render_template_string(welcome_html, name=name)
    return render_template_string(home_html)

if __name__ == "__main__":
    app.run(debug=True)
