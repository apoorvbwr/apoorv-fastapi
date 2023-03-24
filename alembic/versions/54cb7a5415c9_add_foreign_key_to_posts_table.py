"""add foreign-key to posts table

Revision ID: 54cb7a5415c9
Revises: e1c8ac7656e7
Create Date: 2023-03-24 11:16:52.415955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54cb7a5415c9'
down_revision = 'e1c8ac7656e7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('ownner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['ownner_id'], remote_cols=['id'], ondelete="CASCADE")
    
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
