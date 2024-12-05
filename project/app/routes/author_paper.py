from flask import Blueprint, request, jsonify
from ..models import AuthorPaper
from .. import db

author_paper_bp = Blueprint('author_paper', __name__)

# Ruta para crear una relación entre un autor y un paper
@author_paper_bp.route('/', methods=['POST'])
def create_author_paper():
    """
    Crea una relación entre un autor y un paper.
    """
    data = request.json
    try:
        new_author_paper = AuthorPaper(
            doi=data['doi'],
            author_id=data['author_id']
        )
        db.session.add(new_author_paper)
        db.session.commit()
        return jsonify({'message': 'Author-Paper relationship created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# Ruta para obtener todas las relaciones entre autores y papers
@author_paper_bp.route('/', methods=['GET'])
def get_author_papers():
    """
    Obtiene todas las relaciones entre autores y papers.
    """
    author_papers = AuthorPaper.query.all()
    data = [
        {
            "doi": relation.doi,
            "author_id": relation.author_id
        }
        for relation in author_papers
    ]
    return jsonify(data), 200
