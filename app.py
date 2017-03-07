from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def home_page():
   return redirect("http://sh.ubham.com",code=302)

@app.route('/<page>/')
def redirect_function(page):
    if page == 'hi':
        return redirect("http://github.com",code=302)
    else:
        return redirect("http://isup.me",code=302)

if __name__ == '__main__':
   app.run()
