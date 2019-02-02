from app import *

@app.route("/admin/instruments", methods=['GET'])
@login_required
@require_is_admin
def admin_instruments():
    instruments = Instrument.query.filter(Instrument.is_deleted==False).all()
    return render_t("admin/instruments.html", instruments=instruments)

@app.route("/admin/instrument/add", methods=['GET', 'POST'])
@login_required
@require_is_admin
def admin_instrument_add():
    form = InstrumentAddForm()
    if form.validate_on_submit():
        try:
            name = escape(form.name.data)
            i = Instrument(name, current_user.id, datetime.datetime.now())
            db.session.add(i)
            db.session.commit()
            logging.info("User " + current_user.display_name + " successfully added instrument " + name + ".")
            flash(gettext("Successfully added instrument."), "is-success")
            return redirect("/admin/instruments")
        except Exception as e:
            logging.error(gettext("Failed to add instrument!"))
            logging.info(str(e))
    return render_t("admin/instrument_add.html", form=form)

@app.route("/admin/instrument/edit/<public_id>", methods=['GET', 'POST'])
@login_required
@require_is_admin
def admin_instrument_edit(public_id):
    instrument = Instrument.query.filter(Instrument.public_id==public_id).first()
    if instrument is None:
        return redirect("/admin/instruments")
    form = InstrumentEditForm()
    if request.method == "GET":
        form.name.data = instrument.name
    if form.validate_on_submit():
        try:
            name = escape(form.name.data)
            instrument.name = name
            instrument.modified_by = current_user.id
            instrument.modified_on = datetime.datetime.now()
            db.session.commit()
            logging.info("User " + current_user.display_name + " successfully edited instrument " + name + ".")
            flash(gettext("Successfully edited instrument."), "is-success")
            return redirect("/admin/instruments")
        except Exception as e:
            logging.error(gettext("Failed to edit instrument!"))
            logging.info(str(e))
    return render_t("admin/instrument_edit.html", form=form)