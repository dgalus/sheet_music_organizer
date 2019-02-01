from app import *

@app.route("/admin/instruments", methods=['GET'])
@login_required
@require_is_admin
def admin_instruments():
    instruments = User.query.filter(Instrument.is_deleted==False).all()
    return render_t("admin/instruments.html", instruments=instruments)