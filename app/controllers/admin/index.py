from app import *

@app.route("/admin", methods=['GET'])
@app.route("/admin/index", methods=['GET'])
@login_required
def admin_index():
    return render_t("admin/index.html")