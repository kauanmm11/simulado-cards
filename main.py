from simulado_e_cards.routes import app, database, Card

with app.app_context():
    database.drop_all()
    database.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)
