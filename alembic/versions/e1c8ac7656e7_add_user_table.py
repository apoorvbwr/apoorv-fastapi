"""add user table

Revision ID: e1c8ac7656e7
Revises: a829a0090b17
Create Date: 2023-03-23 21:45:14.024192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1c8ac7656e7'
down_revision = 'a829a0090b17'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    ),
    
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass

