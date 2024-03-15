from flask import Flask

#Flask initialization
app = Flask(__name__)
app.secret_key = "ecommerce"
app.config['SECRET_KEY'] = "ecommerce"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006, debug=True)
    # app.run()