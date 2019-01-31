from .. import *

@app.errorhandler(401)
def unauthorized(e):
    return redirect('/login')

@app.errorhandler(403)
def forbidden(e):
    return render_template('errorpage.html',
                           errorcode="Błąd 403",
                           contents="Nie masz uprawnień do przeglądania tej strony!"
                          ), 403

@app.errorhandler(404)
def not_found(e):
    return render_template('errorpage.html',
                           errorcode="Bład 404",
                           contents="Nie znaleziono strony!"
                          ), 404