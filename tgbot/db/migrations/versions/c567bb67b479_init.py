"""init

Revision ID: c567bb67b479
Revises: 
Create Date: 2023-01-20 17:32:50.708454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c567bb67b479'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('product_code', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('language', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('order')
    # ### end Alembic commands ###
