"""add index on workout_equipments

Revision ID: 0ea28f1e6c60
Revises: 171dcd7e5f2b
Create Date: 2024-04-21 16:50:26.813151

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '0ea28f1e6c60'
down_revision = '171dcd7e5f2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout_equipments', schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f('ix_workout_equipments_equipment_id'),
            ['equipment_id'],
            unique=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout_equipments', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_workout_equipments_equipment_id'))

    # ### end Alembic commands ###
