from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class URLForm(FlaskForm):
    original_url = StringField("Вставьте ссылку", validators=[DataRequired(message="Поле не должно быть пустым"),
                                                              URL(message='Неверная ссылка')])
    submit = SubmitField('Добавить')