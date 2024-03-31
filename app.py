from flask import Flask, request, jsonify

app = Flask(__name__)

#Base de dados com países
COUNTRIES = [
    {'id':1,'name':'Brasil', 'capital': 'Brasilia'},
    {'id':2,'name':'Estados Unidos', 'capital': 'Washington' },
    {'id':3,'name':'Argentina', 'capital': 'Buenos Aires' }
]

#Variável global para manter índice único
max_id = 3


#Retorna lista com todos países
@app.get("/countries")
def getCountries():
    return jsonify(COUNTRIES)

#Busca de um país para um id específico
#ID aqui deve ser passado na URL do recurso
#http://localhost:5000/country/<id>
@app.get("/country/<int:id>")
def getCountry(id):
    for country in COUNTRIES:
        if country['id'] == id:
            return jsonify(country), 200
    return {"erro": "Pais nao encontrado"}, 404


#Busca de um país para um id específico
#ID aqui deve ser passado como um argumento na URL
#http://localhost:5000/country?id=valor
@app.get("/country")
def getCountryByQuery():
    id = request.args.get('id',type=int)
    for country in COUNTRIES:
        if country['id'] == id:
            return jsonify(country), 200
    return {"erro": "Pais nao encontrado"}, 404



#Adiciona um novo país recebendo um JSON
#com name e capital
#content-type da mensagem precisa ser application/json
#Não tem nenhum tipo de validação!
@app.post("/country")
def addCountry():
    if request.is_json:
        country = request.get_json()
        global max_id
        max_id += 1
        country['id'] = max_id
        COUNTRIES.append(country)
        return {'id':max_id}, 201
    return {"erro":"Formato deve ser JSON"}, 415

#Remove país pelo id passado como variável na URL
#http://localhost:5000/country/<id>
@app.delete("/country/<int:id>")
def deleteCountry(id):
    for c in COUNTRIES:
        if(c['id'] == id):
            COUNTRIES.remove(c)
            return "removido", 200
    return {"erro": 'Pais nao encontrado'}, 404
