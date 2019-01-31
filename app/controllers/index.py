from .. import *


@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    return render_t("index/search.html")

@app.route('/search_by_title', methods=['GET', 'POST'])
@login_required
def search_by_title():
    return render_r("index/search_by_title.html")