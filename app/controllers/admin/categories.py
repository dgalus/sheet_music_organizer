from app import *

@app.route("/admin/categories", methods=['GET'])
@login_required
@require_is_admin
def admin_categories():
    categories = Category.query.all()
    hide_form = CategoryHideForm()
    make_visible_form = CategoryMakeVisibleForm()
    return render_t("admin/categories.html", categories=categories, hide_form=hide_form, make_visible_form=make_visible_form)

@app.route("/admin/category/add", methods=['GET', 'POST'])
@login_required
@require_is_admin
def admin_category_add():
    form = CategoryAddForm()
    if form.validate_on_submit():
        try:
            name = escape(form.name.data)
            c = Category(name, current_user.id, datetime.datetime.now())
            db.session.add(c)
            db.session.commit()
            logging.info("User " + current_user.display_name + " successfully added category " + name + ".")
            flash(gettext("Successfully added category."), "is-success")
            return redirect("/admin/categories")
        except Exception as e:
            flash(gettext("Failed to add category."), "is-danger")
            logging.error(gettext("Failed to add category!"))
            logging.info(str(e))
    return render_t("admin/category_add.html", form=form)

@app.route("/admin/category/edit/<public_id>", methods=['GET', 'POST'])
@login_required
@require_is_admin
def admin_category_edit(public_id):
    category = Category.query.filter(Category.public_id==public_id).first()
    if category is None:
        return redirect("/admin/categories")
    form = CategoryEditForm()
    if request.method == "GET":
        form.name.data = category.name
    if form.validate_on_submit():
        try:
            name = escape(form.name.data)
            category.name = name
            category.modified_by = current_user.id
            category.modified_on = datetime.datetime.now()
            db.session.commit()
            logging.info("User " + current_user.display_name + " successfully edited category " + category.name + ".")
            flash(gettext("Successfully edited category."), "is-success")
            return redirect("/admin/categories")
        except Exception as e:
            flash(gettext("Failed to edit category."), "is-danger")
            logging.error(gettext("Failed to edit category!"))
            logging.info(str(e))
    return render_t("admin/category_edit.html", form=form)

@app.route("/admin/category/hide/<public_id>", methods=['POST'])
@login_required
@require_is_admin
def admin_category_hide(public_id):
    category = Category.query.filter(Category.public_id==public_id).first()
    if category is None:
        return redirect("/admin/categories")
    form = CategoryHideForm()
    if form.validate_on_submit():
        try:
            category.deleted_by = current_user.id
            category.deleted_on = datetime.datetime.now()
            category.is_deleted = True
            db.session.commit()
            logging.info("Category " + category.name + " was hided successfully by " + current_user.display_name + ".")
            flash(gettext("Category is hidden now."), "is-success")
        except Exception as e:
            flash(gettext("Failed to hide category."), "is-danger")
            logging.error(gettext("Failed to hide category!"))
            logging.info(str(e))
    return redirect("/admin/categories")

@app.route("/admin/category/make_visible/<public_id>", methods=['POST'])
@login_required
@require_is_admin
def admin_category_make_visible(public_id):
    category = Category.query.filter(Category.public_id==public_id).first()
    if category is None:
        return redirect("/admin/categories")
    form = CategoryMakeVisibleForm()
    if form.validate_on_submit():
        try:
            category.modified_by = current_user.id
            category.modified_on = datetime.datetime.now()
            category.is_deleted = False
            db.session.commit()
            logging.info("Category " + category.name + " was made visible successfully by " + current_user.display_name + ".")
            flash(gettext("Category is visible now."), "is-success")
        except Exception as e:
            flash(gettext("Failed to make category visible."), "is-danger")
            logging.error(gettext("Failed to make category visible!"))
            logging.info(str(e))
    return redirect("/admin/categories")