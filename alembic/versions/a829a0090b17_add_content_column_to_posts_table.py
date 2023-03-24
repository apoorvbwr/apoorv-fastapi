"""add content column to posts table

Revision ID: a829a0090b17
Revises: 1c461b6c250d
Create Date: 2023-03-23 19:40:00.957936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a829a0090b17'
down_revision = '1c461b6c250d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

