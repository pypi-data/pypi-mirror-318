"""add analysis visibility level

Revision ID: 8a80bec0a410
Revises: 70f12f8c0218
Create Date: 2024-12-23 10:16:23.026455

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '8a80bec0a410'
down_revision = '70f12f8c0218'
branch_labels = None
depends_on = None

visibility_levels = postgresql.ENUM(
    'PUBLIC',
    'FOLLOWERS_AND_REMOTE',  # for a next version, not used for now
    'FOLLOWERS',
    'PRIVATE',
    name='visibility_levels',
)


def upgrade():
    visibility_levels.create(op.get_bind())
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'analysis_visibility',
                visibility_levels,
                server_default='PRIVATE',
                nullable=True,
            )
        )
    op.execute("UPDATE users SET analysis_visibility = 'PRIVATE';")
    op.alter_column('users', 'analysis_visibility', nullable=False)

    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'analysis_visibility',
                visibility_levels,
                server_default='PRIVATE',
                nullable=True,
            )
        )
    op.execute("UPDATE workouts SET analysis_visibility = 'PRIVATE';")
    op.alter_column('workouts', 'analysis_visibility', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.drop_column('analysis_visibility')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('analysis_visibility')

    # ### end Alembic commands ###
