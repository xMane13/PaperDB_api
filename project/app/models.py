from . import db

class Authors(db.Model):
    __tablename__ = 'Authors'
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(20), nullable=False)
    author_last_name = db.Column(db.String(20), nullable=False)
    author_email = db.Column(db.String(50), nullable=False)
    author_affiliation = db.Column(db.String(50), nullable=False)

    # Relación con AuthorPaper
    papers = db.relationship('AuthorPaper', back_populates='author')

class Papers(db.Model):
    __tablename__ = 'Papers'
    doi = db.Column(db.String(20), primary_key=True)
    paper_title = db.Column(db.String(30), nullable=False)
    paper_abstract = db.Column(db.String(500), nullable=False)
    paper_keywords = db.Column(db.String(30), nullable=False)
    submission_date = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    school_idpk = db.Column(db.String(10), db.ForeignKey('School.school_idpk'), nullable=False)
    journal_idpk = db.Column(db.String(20), db.ForeignKey('Journal.journal_idpk'), nullable=False)

    # Relación con AuthorPaper
    authors = db.relationship('AuthorPaper', back_populates='paper')

class AuthorPaper(db.Model):
    __tablename__ = 'Author_Paper'
    doi = db.Column(db.String(20), db.ForeignKey('Papers.doi'), primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('Authors.author_id'), primary_key=True)

    # Relaciones con Authors y Papers
    author = db.relationship('Authors', back_populates='papers')
    paper = db.relationship('Papers', back_populates='authors')

class School(db.Model):
    __tablename__ = 'School'
    school_idpk = db.Column(db.String(10), primary_key=True)
    school_name = db.Column(db.String(100), nullable=False)

class Journal(db.Model):
    __tablename__ = 'Journal'
    journal_idpk = db.Column(db.String(20), primary_key=True)
    publisher_name = db.Column(db.String(20), nullable=False)
    journal_name = db.Column(db.String(100), nullable=False)
    presentation_type = db.Column(db.Integer, nullable=False)
