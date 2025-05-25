"""Create freebies table

Revision ID: b9d68a0a8d94
Revises: a5db1557f425
Create Date: 2025-05-26 00:20:13.862585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9d68a0a8d94'
down_revision = 'a5db1557f425'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('item_name', sa.String, nullable=False),
        sa.Column('value', sa.Integer, nullable=False),
        sa.Column('dev_id', sa.Integer, sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('freebies')
