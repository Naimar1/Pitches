"""sixth migration

Revision ID: 84140848962e
Revises: 97b282343950
Create Date: 2019-02-27 11:27:06.080298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84140848962e'
down_revision = '97b282343950'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category_id', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('category_title', sa.String(), nullable=True))
    op.drop_column('pitches', 'title')
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('title', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'category_title')
    op.drop_column('pitches', 'category_id')
    # ### end Alembic commands ###
