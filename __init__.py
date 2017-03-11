from flask import Flask, redirect
app = Flask(__name__)
import db_crud

@app.route('/')
def home_page():
   return redirect("http://sh.ubham.com",code=302)

@app.route('/<page>/')
def redirect_function(page):
    return redirect( db_crud.expand_url(page) ,code=302)

if __name__ == '__main__':
    app.run()
