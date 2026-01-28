from flask import Flask, redirect, render_template, request

# create Flask object
app = Flask(__name__)


# if access the route (/)
@app.route("/")
def index():
    return render_template("loginPage.html")


# if access the route (/scoreForm)
@app.route("/scoreForm")
def scoreForm():
    return render_template("evaluateForm.html")


# if access the route (/evaluate)
@app.route("/evaluate")
def evaluate():
    bodyContent = "<center>Incomplete Input</center>"
    """ 
    Your implementation 
    getName  = request.args.get('name')
    getTH    = ???
    getEN    = request.args.get('en')
            ??????
    """
    getName = request.args.get("name")
    getTH = request.args.get("th")
    getEN = request.args.get("en")
    getES = request.args.get("es")
    getJP = request.args.get("jp")

    if not getName or not getTH or not getEN or not getES or not getJP:
        return bodyContent
    else:
        """ 
            Your implementation 
            getTH     = ????
            getEN     = ????
            getES     = int(getES)
            getJP     = int(???)
            total     = getTH + getES + getEN + getJP
            percentTH = 100*ge ?????
            percentEN = 100*ge ?????
            percentES = 100*ge ?????
            percentJP = 100*ge ????

        """

        getTH = int(getTH)
        getEN = int(getEN)
        getES = int(getES)
        getJP = int(getJP)
        total = getTH + getEN + getES + getJP
        percentTH = 100 * getTH / total
        percentEN = 100 * getEN / total
        percentES = 100 * getES / total
        percentJP = 100 * getJP / total

        bodyContent = (
            """<html lang="en"><head> <mata charset="UTF-8">
                         <script src="https://cdn.jsdelivr.net/npm/chart.js"></script></head>
                        <body><center><table style = "width:60%"><tr><td><center>"""
            + getName
            + """</center></td><tr/>
                              <tr><td><canvas id="PiChart"></canvas></td><tr/>
                              </table></center>
                        <script>
                            var labels  = [ 'TH','EN','ES','JP' ];
                            const colorsList = [ 'rgb(255, 99, 132)','rgb(54, 162, 235)','rgb(255, 181, 51)',
                                                 'rgb(25, 181, 51)','rgb(213, 213, 213)'];
                            var holder  = ["""
            + str(percentTH)
            + """, """
            + str(percentEN)
            + """, """
            + str(percentES)
            + """, """
            + str(percentJP)
            + """];
                                function drawPieHolder(){
                                let data = {
                                        labels: labels,
                                        datasets: [{
                                            label: 'Language ability score',
                                            backgroundColor: colorsList,
                                            borderColor: 'rgb(25, 409, 132)',
                                            data: holder,
                                        }]
                                };
                                config = {
                                    type: 'pie',data: data,
                                    options: { 
                                        animateRotate: false,   
                                        animateScale: false
                                    }
                                };
                                let chartStatus = Chart.getChart('PiChart'); 
                                if (chartStatus != undefined) { chartStatus.destroy(); }
                                let myChart = new Chart(document.getElementById('PiChart'),config);
                                }
                                const set_autoPi = setInterval( drawPieHolder ,3000);
                        </script>
                        </body>
                        </html>"""
        )
        return bodyContent


# if access the route (/checkLogin)
@app.route("/checkLogin", methods=["GET", "POST"])
def verifyLogin():
    correctLog = "ping"
    correctPass = "systemx"
    bodyContent = "<center>You are not allowed to enter this site!</center>"
    if request.method == "POST":
        getLog = request.form["login"]
        getPass = request.form["passwd"]
        if correctLog == getLog and correctPass == getPass:
            # bodyContent = "<center>Welcome "+getLog+" </center>"
            bodyContent = (
                "<center>Welcome "
                + getLog
                + " <br> <a href='scoreForm'>ability score</a></center>"
            )
            return bodyContent
        else:
            return bodyContent
    elif request.method == "GET":
        getLog = request.args.get("login")
        getPass = request.args.get("passwd")

        if not getLog or not getPass:
            return bodyContent

        if correctLog == getLog and correctPass == getPass:
            bodyContent = "<center>Welcome " + getLog + " </center>"
            return bodyContent
        else:
            return bodyContent
    else:
        return redirect("https://www.google.com/")


app.run(host="0.0.0.0", port=5000)
