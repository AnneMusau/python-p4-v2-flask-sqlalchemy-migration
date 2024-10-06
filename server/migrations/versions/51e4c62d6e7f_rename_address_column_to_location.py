"""Rename address column to location

Revision ID: 51e4c62d6e7f
Revises: 
Create Date: 2024-10-06 19:28:06.347220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51e4c62d6e7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Rename the 'address' column to 'location' in the appropriate table
    op.alter_column('your_table_name', 'address', new_column_name='location')

    # If you don't need the auto-generated table creation, you can remove these lines
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    # Revert the column rename from 'location' back to 'address'
    op.alter_column('your_table_name', 'location', new_column_name='address')

    # If you removed the table creation commands in the upgrade, remove these too
    op.drop_table('employees')
    op.drop_table('departments')
