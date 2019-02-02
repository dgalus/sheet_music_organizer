from app import *

@app.route("/admin/instruments", methods=['GET'])
@login_required
@require_is_admin
def admin_instruments():
    instruments = Instrument.query.all()
    hide_form = InstrumentHideForm()
    make_visible_form = InstrumentMakeVisibleForm()
    return render_t("admin/instruments.html", instruments=instruments, hide_form=hide_form, make_visible_form=make_visible_form)

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
            flash(gettext("Failed to add instrument."), "is-danger")
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
            logging.info("User " + current_user.display_name + " successfully edited instrument " + instrument.name + ".")
            flash(gettext("Successfully edited instrument."), "is-success")
            return redirect("/admin/instruments")
        except Exception as e:
            flash(gettext("Failed to edit instrument."), "is-danger")
            logging.error(gettext("Failed to edit instrument!"))
            logging.info(str(e))
    return render_t("admin/instrument_edit.html", form=form)

@app.route("/admin/instrument/hide/<public_id>", methods=['POST'])
@login_required
@require_is_admin
def admin_instrument_hide(public_id):
    instrument = Instrument.query.filter(Instrument.public_id==public_id).first()
    if instrument is None:
        return redirect("/admin/instruments")
    form = InstrumentHideForm()
    if form.validate_on_submit():
        try:
            instrument.deleted_by = current_user.id
            instrument.deleted_on = datetime.datetime.now()
            instrument.is_deleted = True
            db.session.commit()
            logging.info("Instument " + instrument.name + " was hided successfully by " + current_user.display_name + ".")
            flash(gettext("Instrument is hidden now."), "is-success")
        except Exception as e:
            flash(gettext("Failed to hide instrument."), "is-danger")
            logging.error(gettext("Failed to hide instrument!"))
            logging.info(str(e))
    return redirect("/admin/instruments")

@app.route("/admin/instrument/make_visible/<public_id>", methods=['POST'])
@login_required
@require_is_admin
def admin_instrument_make_visible(public_id):
    instrument = Instrument.query.filter(Instrument.public_id==public_id).first()
    if instrument is None:
        return redirect("/admin/instruments")
    form = InstrumentMakeVisibleForm()
    if form.validate_on_submit():
        try:
            instrument.modified_by = current_user.id
            instrument.modified_on = datetime.datetime.now()
            instrument.is_deleted = False
            db.session.commit()
            logging.info("Instument " + instrument.name + " was made visible successfully by " + current_user.display_name + ".")
            flash(gettext("Instrument is visible now."), "is-success")
        except Exception as e:
            flash(gettext("Failed to make instrument visible."), "is-danger")
            logging.error(gettext("Failed to make instrument visible!"))
            logging.info(str(e))
    return redirect("/admin/instruments")