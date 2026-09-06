from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import SelectField, RadioField


class FormCard(FlaskForm):
    card_pergunta = StringField('Crie a Pergunta: ', validators=[DataRequired()])
    card_resposta = StringField('Crie a Resposta: ', validators=[DataRequired()])
    card_categoria = SelectField('categoria', choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('Logica', 'Logica')], validators=[DataRequired()])
    botao_submit_card = SubmitField('Criar Card')
    botao_submit_acertei = SubmitField('Acertei')
    botao_submit_errei = SubmitField('Errei')

class FormMateria(FlaskForm):
    nome_materia = StringField('Nome da Matéria', validators=[DataRequired()])
    descricao_materia = StringField('Descrição da Matéria', validators=[DataRequired()])
    sobre_materia = StringField('Sobre a Matéria', validators=[DataRequired()])
    botao_submit_materia = SubmitField('Adicionar')

class FormQuestao(FlaskForm):
    enunciado = StringField('enunciado', validators=[DataRequired()])
    alternativa_a = StringField('',validators=[DataRequired()])
    alternativa_b = StringField('',validators=[DataRequired()])
    alternativa_c = StringField('',validators=[DataRequired()])
    alternativa_d = StringField('',validators=[DataRequired()])
    resposta_correta = RadioField('Alternativas (marque a correta)', choices=[('A', 'Alternativa A'), ('B','Alternativa B'), ('C', 'Alternativa C'), ('D', 'Alternativa D')], validators=[DataRequired()])
    botao_submit_questao = SubmitField('Adicionar')
