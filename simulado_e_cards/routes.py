from flask import render_template, redirect, url_for, request,session
from simulado_e_cards.form import FormCard
from simulado_e_cards.models import Card, database, app


@app.route('/', methods=['GET', 'POST'])
def painel():
    form_card = FormCard()
    if 'botao_submit_card' in request.form:
        if form_card.validate_on_submit():
            card = Card(
                card_pergunta = form_card.card_pergunta.data,
                card_resposta = form_card.card_resposta.data,
                card_categoria = form_card.card_categoria.data
            )
            database.session.add(card)
            database.session.commit()
            return redirect(url_for('painel'))
    if 'botao_submit_excluir' in request.form:
        card_id = request.form.get('card_id')
        card = Card.query.filter_by(id=card_id).first()
        database.session.delete(card)
        database.session.commit()
        return redirect(url_for('painel'))
            
    if 'botao_submit_editar' in request.form:
        card_id = request.form.get('card_editar_id')
        card = Card.query.filter_by(id=card_id).first()
        if card:
            form_card.card_pergunta.data = card.card_pergunta
            form_card.card_resposta.data = card.card_resposta
    if 'botao_salvar_edicao' in request.form:
        card_id = request.form.get('card_editar_id')
        card = Card.query.filter_by(id=card_id).first()
        if card:
            card.card_pergunta = form_card.card_pergunta.data
            card.card_resposta = form_card.card_resposta.data
            database.session.commit()
            return redirect(url_for('painel'))

    cards = Card.query.all()
    return render_template('painel.html', form_card=form_card, cards=cards)