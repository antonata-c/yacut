from http import HTTPStatus

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short:
            short = get_unique_short_id()
        if URLMap.query.filter_by(short=short).first():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)
        urlmap = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(urlmap)
        db.session.commit()
        return render_template(
            'index.html',
            form=form,
            url=url_for('redirect_view', short=short, _external=True)
        )
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    urlmap = URLMap.query.filter_by(short=short).first()
    if not urlmap:
        abort(HTTPStatus.NOT_FOUND)
    return redirect(urlmap.original)
