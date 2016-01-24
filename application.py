from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"


@app.route("/application-form")
def application_form():
    """Show application form."""

    return render_template("application-form.html")
     


@app.route("/application-response")
def application_response():
    """Show summary of responses from application-form."""

    form = request.form
    print "#######################", form
    print type(form)

    firstname = request.form.get("first-name", "Robin")
    lastname = request.form.get("last-name", "Smith")
    salary = request.form.get("salary", "65000")
    position = request.form.get("position", "Product Manager")

    return render_template("application-response.html",   
                            firstname = firstname,
                            lastname = lastname,
                            salary = salary,
                            position = position)


                            
    



if __name__ == "__main__":
    app.run(debug=True)
