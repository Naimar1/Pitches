"""fifth migration

Revision ID: d89657447a27
Revises: 9eb1cd1269f1
Create Date: 2019-02-27 11:05:34.027034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd89657447a27'
down_revision = '9eb1cd1269f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_writer', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.drop_constraint('users_pitch_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_pitch_id_fkey', 'users', 'pitches', ['pitch_id'], ['id'])
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    op.drop_column('comments', 'pitch_writer')
    # ### end Alembic commands ###
