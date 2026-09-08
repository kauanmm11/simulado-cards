from flask import render_template, redirect, url_for, request, session
from simulado_e_cards.form import FormCard, FormMateria, FormQuestao
from simulado_e_cards.models import Card, Materia, Questao, database, app


@app.route('/', methods=['GET', 'POST'])
def painel():
    form_card = FormCard()

    cards = Card.query.all()
    return render_template('painel.html', form_card=form_card, cards=cards)

@app.route('/flashcard/<int:materia_id>', methods=['GET', 'POST'])
def flashcard(materia_id):
    form_card = FormCard()
    modal_aberto = None
    card_edicao = None

    materia = Materia.query.get_or_404(materia_id)

    if 'botao_submit_card' in request.form:
        if form_card.validate_on_submit():
            card = Card(
                card_pergunta = form_card.card_pergunta.data,
                card_resposta = form_card.card_resposta.data,
                card_categoria = form_card.card_categoria.data,
                materia_id=materia_id
            )
            database.session.add(card)
            database.session.commit()
            return redirect(url_for('flashcard', materia_id=materia_id))
    if 'botao_submit_excluir' in request.form:
        card_id = request.form.get('card_id')
        card = Card.query.filter_by(id=card_id, materia_id=materia_id).first()
        database.session.delete(card)
        database.session.commit()
        return redirect(url_for('flashcard', materia_id=materia_id))
            
    if 'botao_submit_editar' in request.form:
        card_id = request.form.get('card_editar_id')
        card = Card.query.filter_by(id=card_id, materia_id=materia_id).first()
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
            return redirect(url_for('flashcard', materia_id=materia_id))

    cards = Card.query.filter_by(materia_id=materia_id).all()

    return render_template('flashcards.html',card_edicao=card_edicao, modal_aberto=modal_aberto, form_card=form_card, cards=cards, materia=materia)

@app.route('/materias', methods=['GET', 'POST'])
def materias():
    form_materia = FormMateria()
    modal_aberto = None
    materia_edicao = None

    if 'botao_submit_materia' in request.form:
        if form_materia.validate_on_submit():
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



@app.route('/materia/<int:materia_id>', methods=['GET', 'POST'])
def materia(materia_id):

    materia = Materia.query.get_or_404(materia_id)
    form_card = FormCard()
    form_materia = FormMateria()
    form_questao = FormQuestao()

    if 'botao_submit_questao' in request.form:
        if form_questao.validate_on_submit():
            questao = Questao(
                enunciado = form_questao.enunciado.data,
                alternativa_a = form_questao.alternativa_a.data,
                alternativa_b = form_questao.alternativa_b.data,
                alternativa_c = form_questao.alternativa_c.data,
                alternativa_d = form_questao.alternativa_d.data,
                resposta_correta = form_questao.resposta_correta.data,
                materia_id = materia_id
            )
            database.session.add(questao)
            database.session.commit()
            return redirect(url_for('materia', materia_id=materia_id))

    if 'botao_submit_card' in request.form:
        if form_card.validate_on_submit():
            card = Card(
                card_pergunta = form_card.card_pergunta.data,
                card_resposta = form_card.card_resposta.data,
                card_categoria = form_card.card_categoria.data,
                materia_id=materia_id
            )
            database.session.add(card)
            database.session.commit()
            return redirect(url_for('materia', materia_id=materia_id))

    questoes = Questao.query.filter_by(materia_id=materia_id).all()
    cards = Card.query.filter_by(materia_id=materia_id).all()

    return render_template('materia.html', form_materia=form_materia, materia=materia, form_questao=form_questao, questoes=questoes, form_card=form_card, cards=cards )