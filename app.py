from flask import Flask, render_template, request
import random
import hashlib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def generate_numbers():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)