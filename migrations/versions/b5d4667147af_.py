"""empty message

Revision ID: b5d4667147af
Revises:  
Create Date: 2019-12-30 23:19:25.400322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5d4667147af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=30), nullable=True),
                    sa.Column('password', sa.String(length=30), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('recipes',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=30), nullable=True),
                    sa.Column('instructions', sa.String(
                        length=300), nullable=True),
                    sa.Column('photo', sa.BLOB(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes')
    op.drop_table('users')
    # ### end Alembic commands ###
