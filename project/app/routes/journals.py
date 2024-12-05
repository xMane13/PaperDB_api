from flask import Blueprint, request, jsonify
from ..models import Journal
from ..schemas import JournalSchema
from .. import db

journal_bp = Blueprint('journals', __name__)

# Ruta para crear un nuevo journal
@journal_bp.route('/', methods=['POST'])
def create_journal():
    """
    Crea un nuevo journal.
    """
    data = request.json
    new_journal = Journal(
        journal_idpk=data['journal_idpk'],
        publisher_name=data['publisher_name'],
        journal_name=data['journal_name'],
        presentation_type=data['presentation_type']
    )
    db.session.add(new_journal)
    db.session.commit()
    return jsonify({'message': 'Journal created successfully'}), 201

# Obtener todas las revistas
@journal_bp.route('/', methods=['GET'])
def get_journals():
    journals = Journal.query.all()
    schema = JournalSchema(many=True)
    return jsonify(schema.dump(journals))
