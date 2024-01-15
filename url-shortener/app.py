from flask import Flask, render_template, request

app = Flask(__name__)

# print(__name__)
@app.route('/')
def home():
    # return 'Hello flask'
    return render_template('home.html', name='Mark')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':

    # return 'This is a url shortener'
        return render_template('your_url.html', code=request.form['code'])
    else:
        return 'This is not valid'

# export FLASK_APP=hell
# flask run

# export FLASK_ENV=development

