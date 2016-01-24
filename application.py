from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"


@app.route("/application-form")
def application_form():
    """Show application form."""

    print "Application form successful"
    return render_template("application-form.html")
    


@app.route("/application-response", methods=['POST'])
def application_response():
    """Show summary of responses from application-form."""

    app_form = request.form
    print "#######################", app_form
    print type(app_form)

    firstname = request.form.get("first-name", "failure").title()
    lastname = request.form.get("last-name", "failure").title()
    salary = "%.2f" % float(request.form.get("salary", 0))
    # salary = float((request.form.get("salary", 0)))
    position = request.form.get("position", "failure").title()

    return render_template("application-response.html",   
                            firstname = firstname,
                            lastname = lastname,
                            salary = salary,
                            position = position)


                            
    



if __name__ == "__main__":
    app.run(debug=True)
