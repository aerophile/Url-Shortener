from flask import Flask, render_template, flash, redirect
from forms import UrlForm,ChangeUrlForm
import forms as f
from random import randint
import db_crud
import bijective

app = Flask(__name__)

#app.config.from_object('config')
redirect_type = 301 #change as appropriate
home_url = "Sh.ubham.com" # replace with your own domain or server public IP

@app.route('/')
def home_page():
   return redirect("/shorten",code = redirect_type)

@app.route('/shorten/', methods=['GET', 'POST'])
def shortener():

    form = UrlForm()
    bijective_obj = bijective.ShortURL()

    if form.validate_on_submit():
        change_key ="~ck"+str(bijective_obj.encode(randint(100000000,99999999999)))

        if form.custom_alias.data == '': #No custom alias given
            form.custom_alias.data = str(bijective_obj.encode(randint(100000000000,999999999999)))

        if db_crud.add_url_record( form.custom_alias.data,f.validate_urls( form.long_url.data),change_key) == "inserted":
            flash('Great ! Go checkout '+ home_url +'/%s' %(form.custom_alias.data))    
            return render_template('form.html',form=form,home_url=home_url,custom_alias=form.custom_alias.data,link_to = "http://"+ home_url +"/"+form.custom_alias.data, short_url_creation = True ,changekey=change_key)
        else:
            flash('Woops! The custom alias '+ home_url +'/%s  is taken. Try a different one. '%(form.custom_alias.data))    
            return render_template('form.html',form=form, home_url = home_url , link_to = "http://"+ home_url +"/shorten", short_url_creation = False) 

    return render_template('form.html', form = form , home_url = home_url)

@app.route('/None/')
def not_found():
    return render_template('notfound.html', home_url = home_url)

@app.route('/<page>/', methods = ['GET', 'POST'] )
def redirect_function(page):
    if page[0:3] == "~ck":
        form1 = ChangeUrlForm()
        if form1.validate_on_submit(): 
            new_long_url = f.validate_urls(form1.new_long_url.data)
            if db_crud.update_url_record(page,new_long_url) == "updated":
                flash('Destination changed to %s '%(new_long_url))
                return render_template('change_form.html', home_url = home_url , form1 = form1,new_long_url = new_long_url)
        return render_template('change_form.html',form1 = form1, home_url = home_url)
    else:
        return redirect( db_crud.expand_url(page) ,code = redirect_type)

if __name__ == '__main__':
    app.run()

