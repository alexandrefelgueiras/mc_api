from sqlalchemy import create_engine, Column, Integer, String, Float, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Criando a engine de conexão com o banco SQLite
db_path = "database/"
if not os.path.exists(db_path):
    os.makedirs(db_path)

db_url = "sqlite:///%s/database.db" % db_path
engine = create_engine(db_url, echo=True)  # Set echo to True for debugging

# Criação da base de dados declarativa
Base = declarative_base()


# Definição do modelo Mc
class Mc(Base):
    __tablename__ = "mc"
    id = Column(Integer, primary_key=True)
    cliente = Column(String(60), nullable=False)
    descricao = Column(String(120), nullable=False)
    proposta = Column(Integer, nullable=False)
    item = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    custo = Column(Float, nullable=False)
    margem_abs = Column(Float, default=0)
    margem_rel = Column(Float, default=0)


# Criação das tabelas
Base.metadata.create_all(engine)

# Criação da sessão
Session = sessionmaker(bind=engine)
session = Session()

# Verifica se a tabela "mc" já existe no banco
inspector = inspect(engine)
existing_tables = inspector.get_table_names()
if "mc" in existing_tables:
    # Inserindo dados
    registros_iniciais = [
        {
            "cliente": "CEDAE",
            "descricao": "BOMBA SUB 0.5cv-2P 1F/127/220V/60Hz",
            "proposta": 1,
            "item": 1,
            "preco": 1175.25,
            "custo": 590.90,
        },
        {
            "cliente": "LIGHT",
            "descricao": "Transformador Óleo 112.5kVA 13.2/0.22kV CNA ONAN",
            "proposta": 2,
            "item": 1,
            "preco": 28175.25,
            "custo": 18175.25,
        },
        {
            "cliente": "LIGHT",
            "descricao": "DISJUNTOR-MOTOR AZ MPW12-3-C016S",
            "proposta": 2,
            "item": 2,
            "preco": 1250.25,
            "custo": 798.90,
        },
    ]

    for registro in registros_iniciais:
        novo_registro = Mc(**registro)
        novo_registro.margem_abs = novo_registro.preco - novo_registro.custo
        novo_registro.margem_rel = (
            novo_registro.margem_abs / novo_registro.preco
        ) * 100
        session.add(novo_registro)

    session.commit()

    # Exibindo itens cadastrados
    print(15 * "-" + " Itens Cadastrados: " + 15 * "-")
    itens_cadastrados = session.query(Mc).all()
    for item in itens_cadastrados:
        print(item.__dict__)
else:
    print("A tabela 'mc' já existe. Não foram adicionados novos registros.")
