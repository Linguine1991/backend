from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pizzaria/<sabor>')
def ver_pizza(sabor):
    cardapio = {
        "calabresa": "Calabresa Acebolada",
        "margherita": "Margherita com Manjericão Fresco",
        "frango": "Frango Desfiado com Catupiry"
    }
    
    if sabor in cardapio:
        dados_da_pizza = {
            "nome": cardapio[sabor],
            "imagem": f"{sabor}.jpg"
        }
        return render_template('pizza.html', pizza=dados_da_pizza)
    
    return "<h1>Ops Esse sabor ainda não está no nosso forno. </h1>", 404

if __name__ == '__main__':
    app.run(debug=True)