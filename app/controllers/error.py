from app import *

@app.errorhandler(401)
def unauthorized(e):
    return redirect('/login')

@app.errorhandler(403)
def forbidden(e):
    return render_template('errorpage.html',
                           errorcode=gettext("Error 403"),
                           contents=gettext("Forbidden!")
                          ), 403

@app.errorhandler(404)
def not_found(e):
    return render_template('errorpage.html',
                           errorcode=gettext("Error 404"),
                           contents=gettext("Not found!")
                          ), 404