from flask import Flask

app = Flask(__name__)


@app.route("/studentInfo")
def student_info():
    return """
    <table>
        <tr><td>First Name:</td><td>Natpakan</td></tr>
        <tr><td>Last Name:</td><td>Tabudda</td></tr>
        <tr><td>Nick Name:</td><td>Ohm</td></tr>
        <tr><td>Mobile:</td><td>0123456789</td></tr>
        <tr><td>Student ID:</td><td>67991039</td></tr>
    </table>
    """


if __name__ == "__main__":
    app.run()
