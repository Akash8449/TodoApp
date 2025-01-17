"""test

Revision ID: 6f5a963b3852
Revises: 
Create Date: 2025-01-17 16:43:36.928651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f5a963b3852'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('tasks',sa.Column('name',sa.String(),nullable=True))



def downgrade() -> None:
    op.drop_column('tasks','name')

