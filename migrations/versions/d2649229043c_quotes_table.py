"""quotes_table

Revision ID: d2649229043c
Revises: 
Create Date: 2021-08-28 12:57:42.279247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2649229043c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quotes_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote_id', sa.String(length=10), nullable=False),
    sa.Column('quote_text', sa.String(length=300), nullable=True),
    sa.Column('quote_by', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id', 'quote_id')
    )
    op.create_index(op.f('ix_quotes_table_quote_by'), 'quotes_table', ['quote_by'], unique=True)
    op.create_index(op.f('ix_quotes_table_quote_id'), 'quotes_table', ['quote_id'], unique=True)
    op.create_index(op.f('ix_quotes_table_quote_text'), 'quotes_table', ['quote_text'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quotes_table_quote_text'), table_name='quotes_table')
    op.drop_index(op.f('ix_quotes_table_quote_id'), table_name='quotes_table')
    op.drop_index(op.f('ix_quotes_table_quote_by'), table_name='quotes_table')
    op.drop_table('quotes_table')
    # ### end Alembic commands ###