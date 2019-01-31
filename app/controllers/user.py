from .. import *

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = escape(form.user.data)
        password = escape(form.user.password)
        user = User.query.filter(User.username == username).first()
        if user is not None:
            if bc.check_password_hash(user.password, password):
                exists = False
                for u in users:
                    if u.id == user.id:
                        exists = True
                        break
                us = UserLogin(user.id, user.username, user.display_name)
                if not exists:
                    users.append(us)
                login_user(us, force=True)
                return redirect("/")
            return render_template('user/login.html', form=form)
        return render_template('user/login.html', form=form)
    else:
        return render_template('user/login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return render_template('user/login.html')

@login_manager.user_loader
def load_user(user_id):
    for u in users:
        if u.id == user_id:
            return u
    return None