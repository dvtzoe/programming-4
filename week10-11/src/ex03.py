from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <table>
        <tr><td><a href="/studentInfo">Student information</a></td></tr>
        <tr><td><a href="/contactInfo">Contact information</a></td></tr>
        <tr><td><a href="/projectInfo">Project information</a></td></
    </table>
    """


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


@app.route("/contactInfo")
def contact_info():
    return """
    <table>
        <tr><td>Email:</td><td>dvtzoe@dvtzoe.com</td></tr>
        <tr><td>Phone:</td><td>0123456789</td></tr>
    </table>
    """


@app.route("/projectInfo")
def project_info():
    return """
    <table>
        <tr><td>Projects</td></tr>
        <tr><td><a href="https://github.com/dvtzoe/nexus-archive">Nexus Archive</a></td></tr>
        <tr><td><a href="https://github.com/dvtzoe/acacia">Acacia</a></td></tr>
        <tr><td><a href="https://github.com/dvtzoe/japanese-homework">Japanese Homework</a></td></tr>
        <tr><td><a href="https://github.com/dvtzoe/ace-mix">Ace Mix</a></td></tr>
    </table>
    """


if __name__ == "__main__":
    app.run()
