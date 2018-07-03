from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

#[ ROUTES ]----------

@app.route('/')
def index():
    return render_template('index.html')

# [MAIN]-----------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50001, debug=True)