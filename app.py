from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    student_id = request.form["student_id"]
    date_of_birth = request.form["date_of_birth"]
    email = request.form["email"]

    return f"""
    <h1>Registration Successful!</h1>
    <p>Welcome, {first_name} {last_name}!</p>
    <p>Student ID: {student_id}</p>
    <p>Date of Birth: {date_of_birth}</p>
    <p>Email: {email}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
