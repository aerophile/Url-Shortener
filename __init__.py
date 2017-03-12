from flask import Flask, render_template, flash, redirect
from forms import UrlForm
import forms as f
from random import randint
import db_crud

app = Flask(__name__)

#app.config.from_object('config')

@app.route('/')
def home_page():
   return redirect("http://sh.ubham.com/shorten",code=302)

@app.route('/shorten/', methods=['GET', 'POST'])
def shortener():
    form = UrlForm()

    if form.validate_on_submit():
        if db_crud.add_url_record( form.custom_alias.data,f.validate_urls( form.long_url.data),"_"+str(randint(1000000,9999999))+"ck") == "inserted":
            flash('Great ! Go checkout sh.ubham.com/%s' %(form.custom_alias.data))    
            return render_template('form.html',form=form,custom_alias=form.custom_alias.data)
        else:
            flash('Woops! The custom alias sh.ubham.com/%s  is taken. Try a different one. '%(form.custom_alias.data))    
            return render_template('form.html',form=form) 

    return render_template('form.html', form=form)



@app.route('/<page>/')
def redirect_function(page):
    return redirect( db_crud.expand_url(page) ,code=302)

if __name__ == '__main__':
    app.run()


