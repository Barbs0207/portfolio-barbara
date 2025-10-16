# models/consulta.py
from database import db
from datetime import datetime

class Consulta(db.Model):
    __tablename__ = 'consultas'

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    data_hora = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='agendada')
    observacoes = db.Column(db.Text, nullable=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "paciente_id": self.paciente_id,
            "medico_id": self.medico_id,
            "data_hora": self.data_hora,
            "status": self.status,
            "observacoes": self.observacoes,
            "criado_em": self.criado_em.strftime("%Y-%m-%d %H:%M:%S")
        }

