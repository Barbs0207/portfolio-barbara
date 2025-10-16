# models/medico.py
from database import db

class Medico(db.Model):
    __tablename__ = 'medicos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    crm = db.Column(db.String(20), unique=True, nullable=False)
    especialidade = db.Column(db.String(50), nullable=False)

    consultas = db.relationship('Consulta', backref='medico_rel', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "crm": self.crm,
            "especialidade": self.especialidade
        }
