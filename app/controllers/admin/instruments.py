from app import *

@app.route("/admin/instruments", methods=['GET'])
@login_required
@require_is_admin
def admin_instruments():
    instruments = User.query.filter(Instrument.is_deleted==False).all()
    return render_t("admin/instruments.html", instruments=instruments)

@app.route("/admin/instrument/add", methods=['GET', 'POST'])
@login_required
@require_is_admin
def admin_instrument_add():
    form = InstrumentAddForm()
    if form.validate_on_submit():
        pass
    return render_t("admin/instrument_add.html", form=form)