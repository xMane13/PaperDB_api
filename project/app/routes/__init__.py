from .authors import author_bp
from .papers import paper_bp
from .schools import school_bp
from .journals import journal_bp
from .author_paper import author_paper_bp

def init_routes(app):
    # Registra blueprints para las rutas
    app.register_blueprint(author_paper_bp, url_prefix='/author-paper')
    app.register_blueprint(author_bp, url_prefix='/authors')
    app.register_blueprint(paper_bp, url_prefix='/papers')
    app.register_blueprint(school_bp, url_prefix='/schools')
    app.register_blueprint(journal_bp, url_prefix='/journals')
