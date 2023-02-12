from flask import Flask, abort, render_template, send_file
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired
import os
import time
from functions import *

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class Form(FlaskForm):
    file = FileField('file', validators=[DataRequired(), FileAllowed(['docx'])])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filename = time.strftime("%H_%M_%S_%m") + filename
        if not os.path.exists('upload'):
            os.mkdir('upload')
        full_filename = os.path.join('upload', filename)
        print(filename)
        form.file.data.save(full_filename)
        folder = filename[:-5]
        crack(full_filename, os.path.join('upload', folder))
        return send_file(full_filename+'.zip', as_attachment=True)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)