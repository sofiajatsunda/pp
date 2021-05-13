"""create account table

Revision ID: 61daf7ff9f43
Revises: 
Create Date: 2021-05-13 16:56:52.066949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61daf7ff9f43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(20), unique=True),
        sa.Column('firstName', sa.String),
        sa.Column('lastName', sa.String),
        sa.Column('email', sa.String),
        sa.Column('password', sa.String),
        sa.Column('phone', sa.String),
    )
    op.create_table(
        'event',
        sa.Column('creatorid', sa.Integer),
       # sa.Column('usersid', sa.Integer),
        sa.Column('eventid', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('content', sa.String),
        sa.Column('tags', sa.String),
        sa.Column('date', sa.String),
    )
    op.create_table(
        'connected_users',
        sa.Column('eventid', sa.Integer, primary_key=True, foreign_key='Event.id'),
        sa.Column('usersid', sa.Integer, autoincrement=True, foreign_key='User.id')
    )


def downgrade():
    op.drop_table('user')
    op.drop_table('event')
    op.drop_table('connected_users')
