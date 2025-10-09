from flask import Flask, render_template, request

# Create an instance of the Flask application
web = Flask(__name__)


@web.route('/')
@web.route('/register')

def home():
    return render_template('register.html')

@web.route('/confirmation', method = ['POST', 'GET'])

def register():
    if request.method == "POST":
        n = request.form.get("name")
        c = request.form.get("city")
        p = request.form.get("phone number")
        return render_template('confirm.html', name = n, city = c, phonenumber = p)


# Run the application (typically from the command line using 'flask run')
if __name__ == "__main__":
    web.run(debug=True)