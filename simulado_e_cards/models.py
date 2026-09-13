from simulado_e_cards import database, app
from sqlalchemy import ForeignKey


class Card(database.Model):
    id = database.Column(database.Integer(), primary_key=True)
    card_pergunta = database.Column(database.String(), nullable=False)
    card_resposta = database.Column(database.String(), nullable=False)
    card_categoria = database.Column(database.String(), nullable=False)
    materia_id = database.Column(
        database.Integer(), ForeignKey("materia.id"), nullable=False
    )


class Materia(database.Model):
    id = database.Column(database.Integer(), primary_key=True)
    nome_materia = database.Column(database.String(), nullable=False)
    descricao_materia = database.Column(database.Text(40), nullable=False)
    sobre_materia = database.Column(database.Text(), nullable=False)
    cor = database.Column(database.String(7), nullable=False, default="#2E8B9F")
    anotacoes = database.relationship("Anotacao", backref="materia", lazy=True)
    questoes = database.relationship("Questao", backref="materia", lazy=True)


class Questao(database.Model):
    id = database.Column(database.Integer(), primary_key=True)
    enunciado = database.Column(database.Text(), nullable=False)
    alternativa_a = database.Column(database.Text(255), nullable=False)
    alternativa_b = database.Column(database.Text(255), nullable=False)
    alternativa_c = database.Column(database.Text(255), nullable=False)
    alternativa_d = database.Column(database.Text(255), nullable=False)
    resposta_correta = database.Column(database.String(1), nullable=False)
    materia_id = database.Column(
        database.Integer(), ForeignKey("materia.id"), nullable=False
    )


class Anotacao(database.Model):
    id = database.Column(database.Integer(), primary_key=True)
    titulo = database.Column(database.String(100), nullable=False)
    conteudo = database.Column(database.Text(), nullable=False)
    tags = database.Column(database.String(255), nullable=False)
    materia_id = database.Column(
        database.Integer(), ForeignKey("materia.id"), nullable=False
    )


class RespostaCard(database.Model):
    id = database.Column(database.Integer(), primary_key=True)
    resultado = database.Column(database.String(), nullable=False)
    card_id = database.Column(
        database.Integer(), database.ForeignKey("card.id"), nullable=False
    )

# class Simulado(database.Model):
#     id = database.Column(database.Integer(), primary_key=True)
#     nome_simulado = database.Column(database.String())
#     questoes_certas = database.Column(database.String(), nullable=False)
#     questoes_erradas = database.Column(database.String(), nullable=False)
#     duracao_simulado = database.Column(database.Integer(), nullable=False)