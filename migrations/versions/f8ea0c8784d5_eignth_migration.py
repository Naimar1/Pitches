"""eignth migration

Revision ID: f8ea0c8784d5
Revises: b1b11be491b9
Create Date: 2019-02-27 12:23:39.712102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8ea0c8784d5'
down_revision = 'b1b11be491b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_message', sa.String(length=255), nullable=True))
    op.add_column('pitches', sa.Column('category_contents', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'category_contents')
    op.drop_column('comments', 'pitch_message')
    # ### end Alembic commands ###
