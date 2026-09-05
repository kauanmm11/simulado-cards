from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import SelectField


class FormCard(FlaskForm):
    card_pergunta = StringField('Crie a Pergunta: ', validators=[DataRequired()])
    card_resposta = StringField('Crie a Resposta: ', validators=[DataRequired()])
    card_categoria = SelectField('categoria', choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('Logica', 'Logica')], validators=[DataRequired()])
    botao_submit_card = SubmitField('Criar Card')
    botao_submit_acertei = SubmitField('Acertei')
    botao_submit_errei = SubmitField('Errei')
