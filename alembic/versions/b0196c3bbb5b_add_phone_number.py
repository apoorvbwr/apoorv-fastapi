"""add phone number

Revision ID: b0196c3bbb5b
Revises: fc38b616ed21
Create Date: 2023-03-24 14:09:07.437005

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b0196c3bbb5b'
down_revision = 'fc38b616ed21'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('postss')
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    op.create_table('postss',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='postss_pkey')
    )
    op.create_table('products',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('is_sale', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('inventory', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIME(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='products_pkey')
    )
    # ### end Alembic commands ###