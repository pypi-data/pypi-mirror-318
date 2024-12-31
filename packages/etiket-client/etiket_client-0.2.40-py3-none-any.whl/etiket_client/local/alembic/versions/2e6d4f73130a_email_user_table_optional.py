"""email user table optional

Revision ID: 2e6d4f73130a
Revises: 05eeaf971b07
Create Date: 2024-10-22 15:27:41.292572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e6d4f73130a'
down_revision: Union[str, None] = '05eeaf971b07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_temp',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('firstname', sa.String(), nullable=False),
        sa.Column('lastname', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('created', sa.DateTime(timezone=True), nullable=False),
        sa.Column('modified', sa.DateTime(timezone=True), nullable=False),
        sa.Column('active', sa.Boolean(), nullable=False),
        sa.Column('disable_on', sa.DateTime(), nullable=True),
        sa.Column('user_type', sa.Enum('admin', 'scope_admin', 'standard_user', 'superuser', name='usertype'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )
    op.execute("""
INSERT INTO users_temp (id, username, firstname, lastname, email, created, modified, disable_on, user_type, active)
SELECT id, username, firstname, lastname, email, created, modified, disable_on, user_type, true
FROM users""")
    
    op.drop_table('users')
    op.execute("ALTER TABLE users_temp RENAME TO users;")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
