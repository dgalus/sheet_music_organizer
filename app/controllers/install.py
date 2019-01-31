from .. import *

@app.route('/install', methods=['GET', 'POST'])
def install():
    config = json.load(open("app/config/app.json"))
    if config["app_name"]:
        return redirect('/')
    form = InstallForm()
    if form.validate_on_submit():
        try:
            app_name = escape(form.app_name.data)
            user = escape(form.user.data)
            password = escape(form.password.data)
            u = User(user, password, user, True)
            db.session.add(u)
            db.session.commit()
            config["app_name"] = app_name
            config["installed"] = True
            with open('app/config/app.json', 'w') as outfile:
                json.dump(config, outfile)
            flash(gettext("Software was successfully installed!"), "is-success")
            return redirect('/')
        except Exception as e:
            logging.critical("Failed to install software.")
            logging.info(str(e))
            flash(gettext("Failed to install software!"), "is-danger")
    return render_template("install/install.html", form=form)