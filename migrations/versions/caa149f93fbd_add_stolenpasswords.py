"""add StolenPasswords

Revision ID: caa149f93fbd
Revises: 
Create Date: 2021-01-19 19:16:30.458709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caa149f93fbd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stolen_passwords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stolen_passwords_username'), 'stolen_passwords', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stolen_passwords_username'), table_name='stolen_passwords')
    op.drop_table('stolen_passwords')
    # ### end Alembic commands ###