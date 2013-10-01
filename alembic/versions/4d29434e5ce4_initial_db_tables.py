"""initial db tables

Revision ID: 4d29434e5ce4
Revises: None
Create Date: 2013-10-01 10:47:32.370171

"""

# revision identifiers, used by Alembic.
revision = '4d29434e5ce4'
down_revision = None

from alembic import op
import sqlalchemy as sa
from paddles.models.types import JSONType


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('runs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('run_id', sa.Integer(), nullable=True),
    sa.Column('archive_path', sa.String(length=512), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('flavor', sa.String(length=128), nullable=True),
    sa.Column('job_id', sa.String(length=32), nullable=True),
    sa.Column('kernel', JSONType(), nullable=True),
    sa.Column('last_in_suite', sa.Boolean(), nullable=True),
    sa.Column('machine_type', sa.String(length=32), nullable=True),
    sa.Column('name', sa.String(length=512), nullable=True),
    sa.Column('nuke_on_error', sa.Boolean(), nullable=True),
    sa.Column('os_type', sa.String(length=32), nullable=True),
    sa.Column('overrides', JSONType(), nullable=True),
    sa.Column('owner', sa.String(length=128), nullable=True),
    sa.Column('pid', sa.String(length=32), nullable=True),
    sa.Column('roles', JSONType(), nullable=True),
    sa.Column('success', sa.Boolean(), nullable=True),
    sa.Column('targets', JSONType(), nullable=True),
    sa.Column('tasks', JSONType(), nullable=True),
    sa.Column('teuthology_branch', sa.String(length=32), nullable=True),
    sa.Column('verbose', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['run_id'], ['runs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobs')
    op.drop_table('runs')
    ### end Alembic commands ###
