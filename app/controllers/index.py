from app import *


@app.route('/', methods=['GET'])
@app.route('/search', methods=['GET'])
@login_required
def search():
    form = SearchForm()
    titles_count = Title.query.filter(Title.is_deleted==False).count()
    users_count = User.query.filter(User.is_active==True).count()
    categories_count = Category.query.filter(Category.is_deleted==False).count()
    return render_t("index/search.html", form=form, titles_count=titles_count, users_count=users_count, categories_count=categories_count)

@app.route('/search_by_title', methods=['GET', 'POST'])
@login_required
def search_by_title():
    return render_r("index/search_by_title.html")