from app import *

@app.route("/admin", methods=['GET'])
@app.route("/admin/index", methods=['GET'])
@login_required
@require_is_admin
def admin_index():
    return render_t("admin/index.html")