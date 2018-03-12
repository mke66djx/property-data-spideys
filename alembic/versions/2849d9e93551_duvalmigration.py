"""DuvalMigration

Revision ID: 2849d9e93551
Revises: 65c4237f4c27
Create Date: 2018-03-11 20:55:00.284702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2849d9e93551'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('duvalcounty')
    op.drop_table('duvalcountysales')
    op.rename_table('duvalCountyTemp', 'duvalcounty')
    op.rename_table('duvalCountySalesTemp', 'duvalcountysales')

    op.drop_table('pierceCountyTemp')
    op.drop_table('pierceCountySalesTemp')

def downgrade():
    pass
