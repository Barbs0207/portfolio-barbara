# app.py
from flask import Flask, jsonify, request
from database import init_db, db
from models.paciente import Paciente
from models.consulta import Consulta
from models.medico import Medico


app = Flask(__name__)
init_db(app)

@app.route('/')
def home():
    return jsonify({"message": "FakeClinic API está no ar!"}), 200

# --- CRUD Pacientes ---
@app.route('/api/pacientes', methods=['GET'])
def listar_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([p.to_dict() for p in pacientes])

@app.route('/api/pacientes', methods=['POST'])
def criar_paciente():
    data = request.get_json()
    novo = Paciente(
        nome=data['nome'],
        email=data['email'],
        cpf=data['cpf'],
        data_nascimento=data['data_nascimento']
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()), 201

@app.route('/api/pacientes/<int:id>', methods=['GET'])
def buscar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    return jsonify(paciente.to_dict())

@app.route('/api/pacientes/<int:id>', methods=['DELETE'])
def deletar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return jsonify({"message": "Paciente deletado com sucesso"})


# --- CRUD de Consultas ---
@app.route('/api/consultas', methods=['GET'])
def listar_consultas():
    consultas = Consulta.query.all()
    return jsonify([c.to_dict() for c in consultas])

@app.route('/api/consultas', methods=['POST'])
def criar_consulta():
    data = request.get_json()
    nova = Consulta(
        paciente_id=data['paciente_id'],
        medico_id=data['medico_id'],
        data_hora=data['data_hora'],
        status=data.get('status', 'agendada'),
        observacoes=data.get('observacoes', '')
    )
    db.session.add(nova)
    db.session.commit()
    return jsonify(nova.to_dict()), 201

@app.route('/api/consultas/<int:id>', methods=['GET'])
def buscar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    return jsonify(consulta.to_dict())

@app.route('/api/consultas/<int:id>', methods=['PUT'])
def atualizar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    data = request.get_json()
    consulta.status = data.get('status', consulta.status)
    consulta.observacoes = data.get('observacoes', consulta.observacoes)
    db.session.commit()
    return jsonify(consulta.to_dict())

@app.route('/api/consultas/<int:id>', methods=['DELETE'])
def deletar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    db.session.delete(consulta)
    db.session.commit()
    return jsonify({"message": "Consulta deletada com sucesso"})

# --- CRUD de Médicos ---
@app.route('/api/medicos', methods=['GET'])
def listar_medicos():
    medicos = Medico.query.all()
    return jsonify([m.to_dict() for m in medicos])

@app.route('/api/medicos', methods=['POST'])
def criar_medico():
    data = request.get_json()
    novo = Medico(
        nome=data['nome'],
        crm=data['crm'],
        especialidade=data['especialidade']
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()), 201

@app.route('/api/medicos/<int:id>', methods=['GET'])
def buscar_medico(id):
    medico = Medico.query.get_or_404(id)
    return jsonify(medico.to_dict())

@app.route('/api/medicos/<int:id>', methods=['DELETE'])
def deletar_medico(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    return jsonify({"message": "Médico deletado com sucesso"})

# 🚀 Executar servidor
if __name__ == '__main__':
    app.run(debug=True)

