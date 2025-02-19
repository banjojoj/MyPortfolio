from flask import Flask, render_template, request, redirect, url_for, session
import smtplib
import os


# define flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# initialize credentials for email
email = os.getenv("EMAIL")
password = os.getenv("EMAIL_PW")


# home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        useremail = request.form.get("email")
        message = request.form.get("message")

        send_email(name, useremail, message)
        # store success message in session
        session['message_sent'] = True

        return redirect(url_for('home'))        # redirect to home page after submitting a message
    return render_template("index.html", message_sent=session.pop('message_sent', False))


def send_email(name, useremail, message):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()  # secure connection

    connection.login(user=email, password=password)
    subject = "New Contact Form Submission"
    body = f"""
    You have received a new message from your portfolio contact form.

    📌 Name: {name}
    📧 Email: {useremail}

    📝 Message:
    {message}

    ---
    Best,  
    Your Portfolio Website
    """

    msg = f"Subject: {subject}\n\n{body}"

    connection.sendmail(
        from_addr=email,
        to_addrs="ajmdineros@gmail.com",
        msg=msg.encode("utf-8")  # Ensures special characters are supported
    )


if __name__ == "__main__":
    app.run(debug=True)
