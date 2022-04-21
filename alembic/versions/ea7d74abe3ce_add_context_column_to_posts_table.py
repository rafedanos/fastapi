"""add context column to posts table\

Revision ID: ea7d74abe3ce
Revises: 14fe93e6670c
Create Date: 2022-04-18 14:01:39.788693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea7d74abe3ce'
down_revision = '14fe93e6670c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
