from http import HTTPStatus

from flask import abort, flash, redirect, render_template, url_for

from . import app
from .constants import NOT_UNIQUE_SHORT_ID
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    if URLMap.get_by_short(form.custom_id.data) is not None:
        flash(NOT_UNIQUE_SHORT_ID)
        return render_template('index.html', form=form)
    url_map = URLMap.create(form.data)
    return render_template(
        'index.html',
        form=form,
        url=url_for('redirect_view', short=url_map.short, _external=True)
    )


@app.route('/<string:short>')
def redirect_view(short):
    urlmap = URLMap.get_by_short(short)
    if not urlmap:
        abort(HTTPStatus.NOT_FOUND)
    return redirect(urlmap.original)
