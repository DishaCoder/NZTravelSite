from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='pages', static_folder='style')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
