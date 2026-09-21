from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():

    # =========================
    # Student Information
    # =========================

    first_name = request.form.get("first_name", "")
    middle_name = request.form.get("middle_name", "")
    last_name = request.form.get("last_name", "")

    contact = request.form.get("contact", "")
    date_of_birth = request.form.get("date_of_birth", "")
    year = request.form.get("year", "")
    gender = request.form.get("gender", "")

    aadhaar_number = request.form.get("aadhaar_number", "")
    email = request.form.get("email", "")

    # HTML uses "blood group"
    blood_group = request.form.get("blood group", "")

    disability = request.form.get("disability", "")


    # =========================
    # Photo and Signature
    # =========================

    photo = request.files.get("photo")
    signature = request.files.get("signature")


    # =========================
    # Parent Information
    # =========================

    # NOTE:
    # Your current HTML uses the same names such as
    # first_name, contact and aadhaar_number for both
    # father and mother.
    #
    # Therefore Flask cannot correctly separate them yet.

    parent_first_names = request.form.getlist("first_name")
    parent_middle_names = request.form.getlist("middle_name")
    parent_last_names = request.form.getlist("last_name")

    occupations = request.form.getlist("occupation")
    parent_contacts = request.form.getlist("contact")
    parent_aadhaars = request.form.getlist("aadhaar_number")

    father_first_name = ""
    father_middle_name = ""
    father_last_name = ""
    father_occupation = ""
    father_contact = ""
    father_aadhaar = ""

    mother_first_name = ""
    mother_middle_name = ""
    mother_last_name = ""
    mother_occupation = ""
    mother_contact = ""
    mother_aadhaar = ""

    if len(parent_first_names) >= 3:
        father_first_name = parent_first_names[1]
        mother_first_name = parent_first_names[2]

    if len(parent_middle_names) >= 3:
        father_middle_name = parent_middle_names[1]
        mother_middle_name = parent_middle_names[2]

    if len(parent_last_names) >= 3:
        father_last_name = parent_last_names[1]
        mother_last_name = parent_last_names[2]

    if len(occupations) >= 2:
        father_occupation = occupations[0]
        mother_occupation = occupations[1]

    if len(parent_contacts) >= 3:
        father_contact = parent_contacts[1]
        mother_contact = parent_contacts[2]

    if len(parent_aadhaars) >= 3:
        father_aadhaar = parent_aadhaars[1]
        mother_aadhaar = parent_aadhaars[2]


    # =========================
    # Academic Information
    # =========================

    class10_board = request.form.get("class10_board", "")
    class10_marks = request.form.get("class10_marks", "")

    class12_board = request.form.get("class12_board", "")
    class12_marks = request.form.get("class12_marks", "")

    college = request.form.get("college", "")
    course = request.form.get("course", "")
    semester = request.form.get("semester", "")

    class10_marksheet = request.files.get("class10_marksheet")
    class12_marksheet = request.files.get("class12_marksheet")


    # =========================
    # Address Information
    # =========================

    state = request.form.get("state", "")
    city = request.form.get("city", "")
    street_name = request.form.get("street_name", "")
    pin_code = request.form.get("pin_code", "")
    address = request.form.get("address", "")


    # =========================
    # Acknowledgement
    # =========================

    acknowledge = request.form.get("acknowledge", "")


    # =========================
    # Display Submitted Data
    # =========================

    return f"""
    <h1>Registration Successful!</h1>

    <h2>Student Information</h2>

    <p>Name: {first_name} {middle_name} {last_name}</p>
    <p>Contact: {contact}</p>
    <p>Date of Birth: {date_of_birth}</p>
    <p>Year: {year}</p>
    <p>Gender: {gender}</p>
    <p>Aadhaar Number: {aadhaar_number}</p>
    <p>Email: {email}</p>
    <p>Blood Group: {blood_group}</p>
    <p>Disability: {disability}</p>


    <h2>Father's Information</h2>

    <p>Name: {father_first_name} {father_middle_name} {father_last_name}</p>
    <p>Occupation: {father_occupation}</p>
    <p>Contact: {father_contact}</p>
    <p>Aadhaar Number: {father_aadhaar}</p>


    <h2>Mother's Information</h2>

    <p>Name: {mother_first_name} {mother_middle_name} {mother_last_name}</p>
    <p>Occupation: {mother_occupation}</p>
    <p>Contact: {mother_contact}</p>
    <p>Aadhaar Number: {mother_aadhaar}</p>


    <h2>Academic Information</h2>

    <p>10th Board: {class10_board}</p>
    <p>10th Marks: {class10_marks}</p>

    <p>12th Board: {class12_board}</p>
    <p>12th Marks: {class12_marks}</p>

    <p>College: {college}</p>
    <p>Course: {course}</p>
    <p>Year: {year}</p>
    <p>Semester: {semester}</p>


    <h2>Address Information</h2>

    <p>State: {state}</p>
    <p>City: {city}</p>
    <p>Street: {street_name}</p>
    <p>Pin Code: {pin_code}</p>
    <p>Home Address: {address}</p>


    <h2>Files</h2>

    <p>Photo: {photo.filename if photo else "No photo uploaded"}</p>
    <p>Signature: {signature.filename if signature else "No signature uploaded"}</p>
    <p>10th Marksheet: {class10_marksheet.filename if class10_marksheet else "No marksheet uploaded"}</p>
    <p>12th Marksheet: {class12_marksheet.filename if class12_marksheet else "No marksheet uploaded"}</p>

    <br>
    <p><b>Registration completed successfully.</b></p>
    """


if __name__ == "__main__":
    app.run(debug=True)
