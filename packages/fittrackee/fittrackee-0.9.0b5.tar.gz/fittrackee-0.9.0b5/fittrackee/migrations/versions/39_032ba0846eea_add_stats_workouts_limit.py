"""add stats_workouts_limit to AppConfig

Revision ID: 032ba0846eea
Revises: 0ea28f1e6c60
Create Date: 2024-06-19 10:27:12.825484

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '032ba0846eea'
down_revision = '0ea28f1e6c60'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('app_config', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('stats_workouts_limit', sa.Integer(), nullable=True)
        )

    op.execute("UPDATE app_config SET stats_workouts_limit = 10000")
    op.alter_column('app_config', 'stats_workouts_limit', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app_config', schema=None) as batch_op:
        batch_op.drop_column('stats_workouts_limit')

    # ### end Alembic commands ###
