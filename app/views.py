"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from forms import ProfileForm
from models import UserProfile
import os,time,random





###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
    
@app.route('/secure_page')
@login_required
def secure_page():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profiles',methods=['GET', 'POST'])
def profiles():
    profile_list = db.session.query(UserProfile).all()
    if not profile_list:
        flash('No users found.', 'danger')
        return redirect(url_for('add_profile'))
    return render_template('profiles.html',profile_list = profile_list)
    
@app.route('/profile/',methods=['GET', 'POST'])
def add_profile():
    form = ProfileForm()
    
    if request.method == 'POST' and form.validate_on_submit():
         fname = request.form['fname']
         lname = request.form['lname']
         gender = request.form['gender']
         email = request.form['email']
         location = request.form['location']
         bio = request.form['bio']
         images = app.config["UPLOAD_FOLDER"]
         image = request.files['photo']
         
         image_name = secure_filename(image.filename)
         image.save(os.path.join(images,image_name))
         
         while True:
            userid = random.randint(1,9999999)
            result = UserProfile.query.filter_by(userid=userid).first()
            if result is None:
                break
        
         created_on = time.strftime("%d %b %Y")
         new_profile = UserProfile(fname,lname,gender,email,location,bio,image_name,userid,created_on)
         db.session.add(new_profile)
         db.session.commit()
         flash('New profile sucessfully added', 'success')
         return redirect(url_for('profiles'))
    return render_template('add_profile.html',form=form) 
    
@app.route('/profile/<userid>',methods=['GET','POST'])
def user_profile(userid):
    
    new_profile = UserProfile.query.filter_by(userid=userid).first()
    if new_profile is not None:
        return render_template('profile.html', new_profile = new_profile)   
    else:
        flash('Oops! User not found.','danger')
        return redirect(url_for('home'))




# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
