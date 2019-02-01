from app import *

@app.route("/admin/users", methods=['GET'])
@login_required
@require_is_admin
def admin_users():
    return "admin users"