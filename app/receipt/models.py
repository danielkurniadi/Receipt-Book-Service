from receipt_book.app import db


class Expense(db.Model):
    __tablename__ = 'expense'

    _id = db.Column(db.String(128), primary_key=True)
    description = db.Column(db.Text(256), default='No description')
    total_sum = db.Column(db.Float(), default=0.0)
    timestamp = db.Column.DateTime()

    #TODO: User: expenses = db.relationship('Expense', back_populates='user')
    user_id = db.Column(db.String(32), db.ForeignKey('user._id'))
    user = db.relationship('User'
        back_populates='expenses'
    )

    #TODO: Receipt: receipt_expense = db.relationship
    receipt_id = db.Column(db.String())
    receipt = db.relationship

    #TODO: Tags: tagged_expenses = db.relationship('Expense', 
    # secondary=tag_expense_association, back_populates='tags')
    #TODO: tag_expense_association table
    tags = db.relationship('Tag',
        secondary=tag_expense_association,
        backref='tagged_expenses'
    )

    def __init__(self, user, receipt,
        total_sum, timestamp=datetime.now(), tags=[]):
        self.user = user
        self.receipt = receipt
        self.total_sum = total_sum
        self.timestamp = timestamp
        self.tags = tags
