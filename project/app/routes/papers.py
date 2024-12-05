from flask import Blueprint, request, jsonify
from ..models import Papers
from ..schemas import PaperSchema
from .. import db

paper_bp = Blueprint('papers', __name__)

# Obtener todos los papers
@paper_bp.route('/', methods=['GET'])
def get_papers():
    papers = Papers.query.all()
    schema = PaperSchema(many=True)
    return jsonify(schema.dump(papers))

# Crear un nuevo paper
@paper_bp.route('/', methods=['POST'])
def create_paper():
    data = request.json
    schema = PaperSchema()
    try:
        new_paper = schema.load(data)
        db.session.add(Papers(**new_paper))
        db.session.commit()
        return jsonify(schema.dump(new_paper)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# Obtener un paper específico
@paper_bp.route('/<string:doi>', methods=['GET'])
def get_paper(doi):
    paper = Papers.query.get(doi)
    if not paper:
        return jsonify({'error': 'Paper not found'}), 404
    return jsonify({
        "doi": paper.doi,
        "paper_title": paper.paper_title,
        "paper_abstract": paper.paper_abstract,
        "paper_keywords": paper.paper_keywords,
        "submission_date": paper.submission_date,
        "status": paper.status,
        "school_idpk": paper.school_idpk,
        "journal_idpk": paper.journal_idpk
    })

# Actualizar un paper específico
@paper_bp.route('/<string:doi>', methods=['PUT'])
def update_paper(doi):
    paper = Papers.query.get(doi)
    if not paper:
        return jsonify({'error': 'Paper not found'}), 404
    data = request.json
    paper.paper_title = data.get('paper_title', paper.paper_title)
    paper.paper_abstract = data.get('paper_abstract', paper.paper_abstract)
    paper.paper_keywords = data.get('paper_keywords', paper.paper_keywords)
    paper.submission_date = data.get('submission_date', paper.submission_date)
    paper.status = data.get('status', paper.status)
    db.session.commit()
    return jsonify({'message': 'Paper updated successfully'})

# Eliminar un paper específico
@paper_bp.route('/<string:doi>', methods=['DELETE'])
def delete_paper(doi):
    paper = Papers.query.get(doi)
    if not paper:
        return jsonify({'error': 'Paper not found'}), 404
    db.session.delete(paper)
    db.session.commit()
    return jsonify({'message': 'Paper deleted successfully'})