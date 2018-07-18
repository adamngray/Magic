"""empty message

Revision ID: 0341a29c084b
Revises: None
Create Date: 2018-07-18 15:20:18.749470

"""

# revision identifiers, used by Alembic.
revision = '0341a29c084b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('slack_user', sa.String(length=21), nullable=True))
    op.drop_column('player', 'slackuser')
    op.add_column('set', sa.Column('constructed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('set', 'constructed')
    op.add_column('player', sa.Column('slackuser', sa.CHAR(length=21), autoincrement=False, nullable=True))
    op.drop_column('player', 'slack_user')
    ### end Alembic commands ###
