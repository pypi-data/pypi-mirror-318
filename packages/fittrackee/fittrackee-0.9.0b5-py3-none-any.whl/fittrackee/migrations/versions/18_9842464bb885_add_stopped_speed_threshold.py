"""add stopped speed threshold to sports

Revision ID: 9842464bb885
Revises: cee0830497f8
Create Date: 2021-11-03 21:39:27.310371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9842464bb885'
down_revision = 'cee0830497f8'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column(
        'sports',
        sa.Column('stopped_speed_threshold', sa.Float(), nullable=True),
    )

    op.execute(
        """
        UPDATE sports
        SET stopped_speed_threshold = 1
        WHERE label in (
              'Cycling (Sport)', 'Cycling (Transport)', 'Mountain Biking', 
              'Mountain Biking (Electric)', 'Rowing', 'Running',
              'Skiing (Alpine)'
        );
        UPDATE sports
        SET stopped_speed_threshold = 0.1
        WHERE label in (
              'Hiking', 'Skiing (Cross Country)', 'Trail', 'Walking'
        );
        """
    )
    op.alter_column('sports', 'stopped_speed_threshold', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sports', 'stopped_speed_threshold')
    # ### end Alembic commands ###
