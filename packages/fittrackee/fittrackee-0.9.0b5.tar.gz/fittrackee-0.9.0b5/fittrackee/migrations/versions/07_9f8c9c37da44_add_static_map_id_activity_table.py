"""add static map id to 'Activity' table

Revision ID: 9f8c9c37da44
Revises: 5a42db64e872
Create Date: 2018-05-30 12:48:11.714627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f8c9c37da44'
down_revision = '5a42db64e872'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activities', sa.Column('map_id', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activities', 'map_id')
    # ### end Alembic commands ###
