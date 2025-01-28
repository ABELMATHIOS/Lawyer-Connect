from flask import Flask , render_template , flash

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page-404.html')

if __name__ == "__main__":
    app.run(debug=True)
