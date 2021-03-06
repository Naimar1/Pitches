"""seventh migration

Revision ID: 30ebd98d5820
Revises: f8ea0c8784d5
Create Date: 2019-02-28 09:09:51.877025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30ebd98d5820'
down_revision = 'f8ea0c8784d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('downvote', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('upvote', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'upvote')
    op.drop_column('pitches', 'downvote')
    # ### end Alembic commands ###
