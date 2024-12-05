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


# Obtener una revista específica
@journal_bp.route('/<string:journal_idpk>', methods=['GET'])
def get_journal(journal_idpk):
    journal = Journal.query.get(journal_idpk)
    if not journal:
        return jsonify({'error': 'Journal not found'}), 404
    return jsonify({
        "journal_idpk": journal.journal_idpk,
        "publisher_name": journal.publisher_name,
        "journal_name": journal.journal_name,
        "presentation_type": journal.presentation_type
    })

# Actualizar una revista específica
@journal_bp.route('/<string:journal_idpk>', methods=['PUT'])
def update_journal(journal_idpk):
    journal = Journal.query.get(journal_idpk)
    if not journal:
        return jsonify({'error': 'Journal not found'}), 404
    data = request.json
    journal.publisher_name = data.get('publisher_name', journal.publisher_name)
    journal.journal_name = data.get('journal_name', journal.journal_name)
    journal.presentation_type = data.get('presentation_type', journal.presentation_type)
    db.session.commit()
    return jsonify({'message': 'Journal updated successfully'})

# Eliminar una revista específica
@journal_bp.route('/<string:journal_idpk>', methods=['DELETE'])
def delete_journal(journal_idpk):
    journal = Journal.query.get(journal_idpk)
    if not journal:
        return jsonify({'error': 'Journal not found'}), 404
    db.session.delete(journal)
    db.session.commit()
    return jsonify({'message': 'Journal deleted successfully'})