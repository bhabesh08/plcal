from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    a = b = ""
    if request.method == "POST":
        a = request.form.get("a", "").strip()
        b = request.form.get("b", "").strip()
        try:
            x = float(a)
            y = float(b)
            result = x + y
        except ValueError:
            error = "Please enter valid numbers (e.g., 5, 12.3, -7)."
    return render_template("index.html", result=result, error=error, a=a, b=b)

if __name__ == "__main__":
    # This is used for local testing; Render will use gunicorn (set later)
    app.run(host="0.0.0.0", port=5000)
