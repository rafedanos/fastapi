"""create users table

Revision ID: 14fe93e6670c
Revises: 1aac8ff7319b
Create Date: 2022-04-18 13:48:57.167310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14fe93e6670c'
down_revision = '1aac8ff7319b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email',sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                        server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')  
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
