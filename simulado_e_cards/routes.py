from flask import render_template, redirect, url_for, request, session
from simulado_e_cards.form import FormCard, FormMateria
from simulado_e_cards.models import Card, Materia, database, app


@app.route('/', methods=['GET', 'POST'])
def painel():
    form_card = FormCard()

    cards = Card.query.all()
    return render_template('painel.html', form_card=form_card, cards=cards)

@app.route('/flashcard', methods=['GET', 'POST'])
def flashcard():
    form_card = FormCard()
    modal_aberto = None
    card_edicao = None

    if 'botao_submit_card' in request.form:
        if form_card.validate_on_submit():
            card = Card(
                card_pergunta = form_card.card_pergunta.data,
                card_resposta = form_card.card_resposta.data,
                card_categoria = form_card.card_categoria.data
            )
            database.session.add(card)
            database.session.commit()
            return redirect(url_for('flashcard'))
    if 'botao_submit_excluir' in request.form:
        card_id = request.form.get('card_id')
        card = Card.query.filter_by(id=card_id).first()
        database.session.delete(card)
        database.session.commit()
        return redirect(url_for('flashcard'))
            
    if 'botao_submit_editar' in request.form:
        card_id = request.form.get('card_editar_id')
        card = Card.query.filter_by(id=card_id).first()
        if card:
            card_edicao = card

            form_card.card_pergunta.data = card.card_pergunta
            form_card.card_resposta.data = card.card_resposta
            form_card.card_categoria.data = card.card_categoria

            modal_aberto = 'editar'
    if 'botao_salvar_edicao' in request.form:
        card_id = request.form.get('card_editar_id')
        card = Card.query.filter_by(id=card_id).first()
        if card:
            card.card_pergunta = form_card.card_pergunta.data
            card.card_resposta = form_card.card_resposta.data
            card.card_categoria = form_card.card_categoria.data
            database.session.commit()
            return redirect(url_for('flashcard'))

    cards = Card.query.all()
    return render_template('flashcards.html',card_edicao=card_edicao, modal_aberto=modal_aberto, form_card=form_card, cards=cards)

@app.route('/materias', methods=['GET', 'POST'])
def materias():
    form_materia = FormMateria()
    modal_aberto = None
    materia_edicao = None

    if 'botao_submit_materia' in request.form:
        if form_materia.validate_on_submit:
            materia = Materia(
                nome_materia = form_materia.nome_materia.data,
                descricao_materia = form_materia.descricao_materia.data,
                sobre_materia = form_materia.sobre_materia.data
            )
            database.session.add(materia)
            database.session.commit()
            return redirect(url_for('materias'))
    if 'botao_submit_excluir' in request.form:
        materia_id = request.form.get('materia_id')
        materia = Materia.query.filter_by(id=materia_id).first()
        database.session.delete(materia)
        database.session.commit()
        return redirect(url_for('materias'))
    if 'botao_submit_editar' in request.form:
        materia_id = request.form.get('materia_id')
        materia = Materia.query.filter_by(id=materia_id).first()
        if materia:
            materia_edicao = materia

            form_materia.nome_materia.data = materia.nome_materia
            form_materia.descricao_materia.data = materia.descricao_materia
            form_materia.sobre_materia.data = materia.sobre_materia

            modal_aberto = 'editar'
    if 'botao_salvar_edicao' in request.form:
        materia_id = request.form.get('materia_id')
        materia = Materia.query.filter_by(id=materia_id).first()
        if materia:

            materia.nome_materia = form_materia.nome_materia.data
            materia.descricao_materia = form_materia.descricao_materia.data
            materia.sobre_materia = form_materia.sobre_materia.data
            database.session.commit()
            return redirect(url_for('materias'))



    materias = Materia.query.all()

    return render_template('materias.html', form_materia=form_materia, materias=materias, modal_aberto=modal_aberto, materia_edicao=materia_edicao)



@app.route('/materia', methods=['GET', 'POST'])
def materia():
    form_materia = FormMateria()

    materias = Materia.query.all()
    return render_template('materia.html', form_materia=form_materia, materias=materias)