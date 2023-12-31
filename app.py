from flask import (
    Flask,
    jsonify,
    request,
    make_response,
    render_template,
    redirect,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
import os

# coletando informacoes do diretorio atual da aplicacao.
base_dir = os.path.abspath(os.path.dirname(__file__))

# instanciando a aplicação Flask
app = Flask(__name__)


# cria a engine de conexão com o banco
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "database", "database.db"
)

# desativando o rastreamento de modificações, para evitar o consumo excessivo de memória.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# configuraçao do swagger
SWAGGER_URL = "/apidocs"
API_URL = "/static/swagger.json"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Margem Certa API"}
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# criando uma instância da classe SQLAlchemy e associando-a à instância do aplicativo Flask (app)
db = SQLAlchemy(app)

# criando uma instância do objeto Marshmallow associado à instância do aplicativo Flask
ma = Marshmallow(app)


# Models
class Mc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    proposta = db.Column(db.Integer, nullable=False)
    item = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float(10, 2), nullable=False)
    custo = db.Column(db.Float(10, 2), nullable=False)
    margem_abs = db.Column(db.Float(10, 2), default=0)
    margem_rel = db.Column(db.Float(5, 2), default=0)

    # Propriedades para campos calculados para margem_abs e margem_rel
    @property
    def margem_abs(self):
        return self.preco - self.custo

    @property
    def margem_rel(self):
        return (self.margem_abs / self.preco) * 100


# create db schema class
class McSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "cliente",
            "descricao",
            "proposta",
            "item",
            "preco",
            "custo",
            "margem_abs",
            "margem_rel",
        )


# criando objetos schema para Mc e Mcs
mc_schema = McSchema(
    many=False
)  # Instancia Marshmallow para serializar ou desserializar um único objeto na tabela Mc

mcs_schema = McSchema(
    many=True
)  # Instancia Marshmallow para serializar ou desserializar muitos objetos (lista) na tabela Mc


# tratamento de erros específicos e fornecimento de respostas personalizadas na execução da sua aplicação
@app.errorhandler(400)
def handle_400_error(_error):
    """Returna erro http 400 para o cliente"""
    return make_response(jsonify({"error": "Solicitação mal compreendida"}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Returna erro http 401 para o cliente"""
    return make_response(jsonify({"error": "Solicitação não autorizada"}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Returna erro http 404 para o cliente"""
    return make_response(jsonify({"error": "Recurso solicitado não encontrado"}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Returna erro http 500 para o cliente"""
    return make_response(jsonify({"error": "Erro no servidor"}), 500)


"""
**********************************************************
ROTAS DE PAGINA
*********************************************************
"""


# PAGINA INICIAL
@app.route("/")
def home():
    mc_data = get_mcs().json
    return render_template("home.html", mcs=mc_data)


# FORMULARIO NOVO ITEM
@app.route("/novo")
def novo():
    mc_data = get_mcs().json
    return render_template("novo.html", titulo="Novo Item", mcs=mc_data)


# FORMULARIO VER ITEM
@app.route("/ver/<int:id>", methods=["GET"])
def ver(id: int):
    mc_data = get_mcs().json
    mc = Mc.query.filter_by(id=id).first()
    return render_template("ver.html", titulo="Detalhando Item", mcs=mc_data, mc=mc)


# FORMULARIO DELETAR ITEM
@app.route("/deletar/<int:id>", methods=["GET"])
def deletar(id: int):
    mc_data = get_mcs().json
    mc = Mc.query.filter_by(id=id).first()
    return render_template("deletar.html", titulo="Excluindo Item", mcs=mc_data, mc=mc)


"""
**********************************************************
ROTAS DE API
*********************************************************
"""


# adiciona uma Margem de Contribuição (mc)
@app.route("/margemcerta", methods=["POST"])
def add_mc():
    try:
        cliente = request.json["cliente"]
        descricao = request.json["descricao"]
        proposta = request.json["proposta"]
        item = request.json["item"]
        preco = request.json["preco"]
        custo = request.json["custo"]

        nova_mc = Mc(
            cliente=cliente,
            descricao=descricao,
            proposta=proposta,
            item=item,
            preco=preco,
            custo=custo,
        )

        db.session.add(nova_mc)
        db.session.commit()

        return mc_schema.jsonify(nova_mc)
    except Exception as e:
        return jsonify({"Erro": "Requisição invalida, tente novamente."})


# lista todas os registros de Margem de Contribuição (mc)
@app.route("/margemcerta", methods=["GET"])
def get_mcs():
    mcs = Mc.query.all()
    result_set = mcs_schema.dump(mcs)
    return jsonify(result_set)


# ajuste de formatacao
@app.template_filter()
def brl_format(value):
    value = float(value)
    return "{:,.2f}".format(value).replace(",", "v").replace(".", ",").replace("v", ".")


# lista um registro específico de Margem de Contribuição (mc)
@app.route("/margemcerta/<int:id>", methods=["GET"])
def get_mc(id):
    mc = Mc.query.get_or_404(int(id))
    return mc_schema.jsonify(mc)


# atualiza um registro específico de Margem de Contribuição (mc)
@app.route("/margemcerta/<int:id>", methods=["PUT"])
def update_mc(id):
    print(id)
    mc = Mc.query.get_or_404(int(id))
    print(mc)

    try:
        cliente = request.json["cliente"]
        descricao = request.json["descricao"]
        proposta = request.json["proposta"]
        item = request.json["item"]
        preco = request.json["preco"]
        custo = request.json["custo"]

        print(
            f"Valores recebidos: {cliente}, {descricao}, {proposta}, {item}, {preco}, {custo}"
        )

        mc.cliente = cliente
        mc.descricao = descricao
        mc.proposta = proposta
        mc.item = item
        mc.preco = preco
        mc.custo = custo

        db.session.commit()

    except Exception as e:
        print(f"Erro na atualização: {e}")
        return jsonify({"Erro": "Requisição invalida, tente novamente."})

    return mc_schema.jsonify(mc)


# Deleta um registro específico de Margem de Contribuição (mc)


@app.route("/margemcerta/<int:id>", methods=["DELETE", "POST"])
def delete_mc(id):
    mc = Mc.query.get_or_404(int(id))
    db.session.delete(mc)
    db.session.commit()
    if request.method == "DELETE":
        return jsonify(
            {
                "Sucesso": True,
                "message": f"Item de Margem de Contribuiçao id({id}) deletado com sucesso.",
            }
        )
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
