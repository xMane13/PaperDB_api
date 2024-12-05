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
