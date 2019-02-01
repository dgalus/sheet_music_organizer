from app import *

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    title = json.load(open("app/config/app.json"))["app_name"] or "Sheet music organizer"
    if form.validate_on_submit():
        username = escape(form.user.data)
        password = escape(form.password.data)
        user = User.query.filter(User.username == username).first()
        if user is not None:
            if bc.check_password_hash(user.password, password):
                exists = False
                for u in users:
                    if u.id == user.id:
                        exists = True
                        break
                us = UserLogin(user.id, user.username, user.display_name, user.is_admin)
                if not exists:
                    users.append(us)
                login_user(us, force=True)
                return redirect("/")
            return render_t('user/login.html', form=form)
        return render_t('user/login.html', form=form)
    else:
        return render_t('user/login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")

@login_manager.user_loader
def load_user(user_id):
    for u in users:
        if u.id == user_id:
            return u
    return None