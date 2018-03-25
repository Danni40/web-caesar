from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form action="/encrypt" method="post">
            <label for="Rotate by">Rotate By</label>
            <input id="Rotate by" type="text" name="rot" value="0">
            <br>
            <textarea name="text"></textarea>
            <br>
            <input type="submit" />
        </form>
    </body>
</html>
"""


@app.route('/')
def index():
    return form

@app.route('/encrypt', methods=['POST'])
def encrypt():
    rot=request.form['rot']
    text=request.form['text']
    rot = int(rot)
    encryptedStr = rotate_string(text, rot)
    return '<h1>{0}</h1>'.format(encryptedStr)




app.run()