from flask import Flask, render_template, request, redirect, url_for, session
import smtplib
import os


# define flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# # initialize email connection
# my_email = "ajmdineros@gmail.com"
# password = "12345"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()       # makes connection secure
#
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="ajmdineros@gmail.com",
#     msg="hello!"
# )
# connection.close()


# home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(name, email, message)

        # store success message in session
        session['message_sent'] = True

        return redirect(url_for('home'))        # redirect to home page after submitting a message
    return render_template("index.html", message_sent=session.pop('message_sent', False))


if __name__ == "__main__":
    app.run(debug=True)
