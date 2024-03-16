from flask import Flask, render_template, request, jsonify

#Flask initialization
app = Flask(__name__)
app.secret_key = "ecommerce"
app.config['SECRET_KEY'] = "ecommerce"

@app.route("/")
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006, debug=False)
    # app.run()