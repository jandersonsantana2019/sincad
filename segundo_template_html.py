from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return ' <html><body><hl>Hello World</h1></body></html>'

@app.route('/home')
def home():
    return render_template('index.html')

if __name__  == '__main__':
    app.run(debug = True)
