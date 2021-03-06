"""quotes_table

Revision ID: 5a9854d8be0c
Revises: 61c51b2f4e32
Create Date: 2021-08-28 13:38:06.356468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a9854d8be0c'
down_revision = '61c51b2f4e32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_quotes_table_quote_by', table_name='quotes_table')
    op.create_index(op.f('ix_quotes_table_quote_by'), 'quotes_table', ['quote_by'], unique=False)
    op.drop_index('ix_quotes_table_quote_text', table_name='quotes_table')
    op.create_index(op.f('ix_quotes_table_quote_text'), 'quotes_table', ['quote_text'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quotes_table_quote_text'), table_name='quotes_table')
    op.create_index('ix_quotes_table_quote_text', 'quotes_table', ['quote_text'], unique=False)
    op.drop_index(op.f('ix_quotes_table_quote_by'), table_name='quotes_table')
    op.create_index('ix_quotes_table_quote_by', 'quotes_table', ['quote_by'], unique=False)
    # ### end Alembic commands ###
