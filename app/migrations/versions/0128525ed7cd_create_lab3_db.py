"""create lab3 db

Revision ID: 0128525ed7cd
Revises: ee540936c5dc
Create Date: 2024-09-02 17:18:04.629833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0128525ed7cd'
down_revision = 'ee540936c5dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    # ### end Alembic commands ###
