from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

@app.route("/application-form", methods=['GET', 'POST'])
def application_form():
    """Show application form."""

    form = request.form
    print form
    print type(form)

    firstname = request.form.get("first-name", "Robin")
    lastname = request.form.get("last-name", "Smith")
    salary = request.form.get("salary", "65000")
    position = request.form.get("position", "Product Manager")

    return render_template("application-form.html",
                            firstname = firstname,
                            lastname = lastname,
                            salary = salary,
                            position = position)

@app.route("/application-response")
def application_response():
    """Show summary of responses from application-form."""

    # return render_template("application-response.html")
    return render_template("application-response.html")

                            
    



if __name__ == "__main__":
    app.run(debug=True)
