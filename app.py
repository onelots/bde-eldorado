from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    # return index.html
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
