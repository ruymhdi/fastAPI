"""Create Products Table

Revision ID: 2b4e63a820b6
Revises: 878f336384cd
Create Date: 2024-01-14 11:46:20.416009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2b4e63a820b6"
down_revision: Union[str, None] = "878f336384cd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
