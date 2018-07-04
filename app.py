from flask import Flask, render_template, request, url_for, redirect
import model
import fetch
import data

app = Flask(__name__)

#[ ROUTES ]----------

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/feed', methods=['GET', 'POST'])
def feed():
    if request.method == 'POST':
        if request.form['action'] == 'save':
            model.parse_form(request.form)
        if request.form['action'] == 'fetch':
            model.get_new_data('feed')
    template_data = {"items": model.get_lineup('feed')}
    return render_template('feed.html', data=template_data, draft_check=False)


@app.route('/about')
def about():
    return render_template('about.html')

# [MAIN]-----------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50001, debug=True)