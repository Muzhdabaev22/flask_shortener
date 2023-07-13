from flask import redirect, url_for, render_template
from . import db, app
from .forms import URLForm
from .models import URLModel, get_short


@app.route("/", methods=["GET", "POST"])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = URLModel()
        url.original_url = form.original_url.data
        url.short = get_short()
        db.session.add(url)
        db.session.commit()
        return redirect(url_for('urls'))
    return render_template("index.html", form=form)


@app.route("/urls", methods=["GET"])
def urls():
    urls = URLModel.query.all()
    return render_template("urls.html", urls=urls[::-1])


@app.route("/<string:short>", methods=["GET"])
def url_redirect(short):
    url = URLModel.query.filter(URLModel.short == short).first()
    if url:
        url.visits += 1
        db.session.add(url)
        db.session.commit()
        return redirect(url.original_url)