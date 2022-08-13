"""empty message

Revision ID: b3877bac16e6
Revises: 709bf25f5b36
Create Date: 2022-08-05 19:52:17.888085

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "b3877bac16e6"
down_revision = "709bf25f5b36"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tag")
    op.drop_table("post")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "post",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("title", sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column("url", sa.VARCHAR(length=140), autoincrement=False, nullable=True),
        sa.Column("body", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column(
            "created", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.PrimaryKeyConstraint("id", name="post_pkey"),
        sa.UniqueConstraint("url", name="post_url_key"),
    )
    op.create_table(
        "tag",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(length=100), autoincrement=False, nullable=True),
        sa.Column("url", sa.VARCHAR(length=100), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="tag_pkey"),
    )
    # ### end Alembic commands ###
