from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    render_var = {}
    render_var['page_name'] = "Home";
    render_var['user'] = {'nickname':'Idol fan'}
    render_var['styles'] = []
    render_var['styles'].append('css/style.css')
    render_var['scripts'] = []
    render_var['scripts'].append('js/script.js')
    return render_template("index.html",
                           vars = render_var)
