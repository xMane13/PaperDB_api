from flask import Blueprint, jsonify, request
from ..models import Authors, Papers, AuthorPaper, Journal
from .. import db

author_bp = Blueprint('authors', __name__)

# Ruta para crear un autor
@author_bp.route('/', methods=['POST'])
def create_author():
    data = request.json
    new_author = Authors(
        author_name=data['author_name'],
        author_last_name=data['author_last_name'],
        author_email=data['author_email'],
        author_affiliation=data['author_affiliation']
    )
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'message': 'Author created successfully'}), 201

# Ruta para obtener autores con sus papers
@author_bp.route('/authors-papers', methods=['GET'])
def authors_with_papers():
    """
    Retorna información de autores y los papers asociados usando joins.
    """
    results = (
        db.session.query(Authors, Papers)
        .join(AuthorPaper, Authors.author_id == AuthorPaper.author_id)
        .join(Papers, AuthorPaper.doi == Papers.doi)
        .all()
    )
    data = [
        {
            "author_name": author.author_name,
            "author_last_name": author.author_last_name,
            "paper_title": paper.paper_title,
            "paper_keywords": paper.paper_keywords,
        }
        for author, paper in results
    ]
    return jsonify(data)

# Ruta para obtener autores, papers y journals
@author_bp.route('/authors-papers-journals', methods=['GET'])
def authors_papers_journals():
    """
    Retorna autores, los papers asociados, y el journal en el que fueron publicados.
    """
    results = (
        db.session.query(Authors, Papers, Journal)
        .join(AuthorPaper, Authors.author_id == AuthorPaper.author_id)
        .join(Papers, AuthorPaper.doi == Papers.doi)
        .join(Journal, Papers.journal_idpk == Journal.journal_idpk)
        .all()
    )
    data = [
        {
            "author_name": author.author_name,
            "author_last_name": author.author_last_name,
            "paper_title": paper.paper_title,
            "journal_name": journal.journal_name,
            "publisher_name": journal.publisher_name,
        }
        for author, paper, journal in results
    ]
    return jsonify(data)

# Ruta para obtener autores con papers aprobados
@author_bp.route('/approved-papers', methods=['GET'])
def approved_papers():
    """
    Retorna autores cuyos papers están aprobados.
    """
    results = (
        db.session.query(Authors, Papers)
        .join(AuthorPaper, Authors.author_id == AuthorPaper.author_id)
        .join(Papers, AuthorPaper.doi == Papers.doi)
        .filter(Papers.status == "approved")
        .all()
    )
    data = [
        {
            "author_name": author.author_name,
            "author_last_name": author.author_last_name,
            "paper_title": paper.paper_title,
        }
        for author, paper in results
    ]
    return jsonify(data)


# Actualizar un autor específico
@author_bp.route('/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    author = Authors.query.get(author_id)
    if not author:
        return jsonify({'error': 'Author not found'}), 404
    data = request.json
    author.author_name = data.get('author_name', author.author_name)
    author.author_last_name = data.get('author_last_name', author.author_last_name)
    author.author_email = data.get('author_email', author.author_email)
    author.author_affiliation = data.get('author_affiliation', author.author_affiliation)
    db.session.commit()
    return jsonify({'message': 'Author updated successfully'})

# Eliminar un autor específico
@author_bp.route('/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = Authors.query.get(author_id)
    if not author:
        return jsonify({'error': 'Author not found'}), 404
    db.session.delete(author)
    db.session.commit()
    return jsonify({'message': 'Author deleted successfully'})