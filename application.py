import os
from flask import Flask, render_template, request, redirect
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from functions import apology, convert1, convert2, convert3, convert4, convert5


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
        return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Validate submission
        if not request.form.get("input"):
            return apology("Please enter text to convert", 403)

        elif not request.form.get("method"):
            return apology("Please select your conversion method", 403)

        # Convert user's input according to their selected method
        method = request.form.get("method")

        if method == "convert1":
            output = convert1(request.form.get("input"))
        elif method == "convert2":
            output = convert2(request.form.get("input"))
        elif method == "convert3":
            output = convert3(request.form.get("input"))
        elif method == "convert4":
            output = convert4(request.form.get("input"))
        elif method == "convert5":
            output = convert5(request.form.get("input"))
        elif method == "all":
            output1 = convert1(request.form.get("input"))
            output2 = convert2(request.form.get("input"))
            output3 = convert3(request.form.get("input"))
            output4 = convert4(request.form.get("input"))
            output5 = convert5(request.form.get("input"))

        if method == "all":
            return render_template("sample.html", output1=output1, output2=output2, output3=output3, output4=output4, output5=output5)
        else:
            return render_template("result.html", output=output)
    else:
        return redirect("/")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == '__main__':
 app.debug = True
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port)