from .. import *

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter(User.name == username).first()
        if user is not None:
            if bc.check_password_hash(user.password, password):
                exists = False
                for u in users:
                    if u.id == user.id:
                        exists = True
                        break
                us = UserLogin(user.id, user.name, user.display_name, [])
                if not exists:
                    users.append(us)
                login_user(us, force=True)
                return redirect("/")
            return render_template('user/login.html')
        return render_template('user/login.html')
    else:
        return render_template('user/login.html')

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