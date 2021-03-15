"""empty message

Revision ID: 46019f534d8f
Revises: 93f5f6967733
Create Date: 2021-03-12 15:24:33.434648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46019f534d8f'
down_revision = '93f5f6967733'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_1', sa.String(length=120), nullable=False),
    sa.Column('question_2', sa.String(length=120), nullable=False),
    sa.Column('question_3', sa.String(length=120), nullable=False),
    sa.Column('question_4', sa.String(length=120), nullable=False),
    sa.Column('question_5', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolio')
    # ### end Alembic commands ###
