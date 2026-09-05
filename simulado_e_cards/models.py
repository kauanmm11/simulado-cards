from simulado_e_cards import database, app


class Card(database.Model):
    id = database.Column(database.Integer(), primary_key=True)
    card_pergunta = database.Column(database.String(), nullable=False)
    card_resposta = database.Column(database.String(), nullable=False)
    card_categoria = database.Column(database.String(), nullable=False)