"""initial migration

Revision ID: 392d72db2a3a
Revises: 911c73d41b62
Create Date: 2024-07-30 06:48:46.323396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '392d72db2a3a'
down_revision: Union[str, None] = '911c73d41b62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
