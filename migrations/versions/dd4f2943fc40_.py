"""empty message

Revision ID: dd4f2943fc40
Revises: 
Create Date: 2018-03-18 22:15:32.578694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd4f2943fc40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=1), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('userid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('created_on', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('userid'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###