"""empty message

Revision ID: d37c03b853e2
Revises: 
Create Date: 2025-04-28 19:26:25.394329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd37c03b853e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('celestial_object',
    sa.Column('object_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('object_type', sa.String(length=50), nullable=True),
    sa.Column('right_ascension', sa.Float(), nullable=True),
    sa.Column('declination', sa.Float(), nullable=True),
    sa.Column('magnitude', sa.Float(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('object_id')
    )
    op.create_table('location',
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('bortle_class', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('location_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.Text(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('profile_image', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('gear',
    sa.Column('gear_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('gear_type', sa.String(length=50), nullable=True),
    sa.Column('brand', sa.String(length=100), nullable=True),
    sa.Column('model', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('gear_id')
    )
    op.create_table('image',
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('file_path', sa.Text(), nullable=True),
    sa.Column('capture_date_time', sa.DateTime(), nullable=True),
    sa.Column('exposure_time', sa.Float(), nullable=True),
    sa.Column('iso', sa.Integer(), nullable=True),
    sa.Column('aperture', sa.Float(), nullable=True),
    sa.Column('focal_length', sa.Float(), nullable=True),
    sa.Column('focus_score', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('image_id')
    )
    op.create_table('session',
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('session_date', sa.Date(), nullable=True),
    sa.Column('weather_conditions', sa.Text(), nullable=True),
    sa.Column('seeing_conditions', sa.Text(), nullable=True),
    sa.Column('moon_phase', sa.String(length=50), nullable=True),
    sa.Column('light_pollution_index', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.location_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_table('frame_set',
    sa.Column('frameset_id', sa.Integer(), nullable=False),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['image.image_id'], ),
    sa.PrimaryKeyConstraint('frameset_id'),
    sa.UniqueConstraint('image_id')
    )
    op.create_table('frame_summary',
    sa.Column('summary_id', sa.Integer(), nullable=False),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.Column('light_frame_count', sa.Integer(), nullable=True),
    sa.Column('dark_frame_count', sa.Integer(), nullable=True),
    sa.Column('flat_frame_count', sa.Integer(), nullable=True),
    sa.Column('bias_frame_count', sa.Integer(), nullable=True),
    sa.Column('dark_flat_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['image.image_id'], ),
    sa.PrimaryKeyConstraint('summary_id'),
    sa.UniqueConstraint('image_id')
    )
    op.create_table('image_gear',
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('gear_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gear_id'], ['gear.gear_id'], ),
    sa.ForeignKeyConstraint(['image_id'], ['image.image_id'], ),
    sa.PrimaryKeyConstraint('image_id', 'gear_id')
    )
    op.create_table('image_object',
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('object_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['image_id'], ['image.image_id'], ),
    sa.ForeignKeyConstraint(['object_id'], ['celestial_object.object_id'], ),
    sa.PrimaryKeyConstraint('image_id', 'object_id')
    )
    op.create_table('image_session',
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['image_id'], ['image.image_id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['session.session_id'], ),
    sa.PrimaryKeyConstraint('image_id', 'session_id')
    )
    op.create_table('processing_log',
    sa.Column('log_id', sa.Integer(), nullable=False),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.Column('step_description', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('software_used', sa.String(length=100), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['image.image_id'], ),
    sa.PrimaryKeyConstraint('log_id')
    )
    op.create_table('raw_frame',
    sa.Column('frame_id', sa.Integer(), nullable=False),
    sa.Column('frameset_id', sa.Integer(), nullable=True),
    sa.Column('frame_type', sa.String(length=20), nullable=True),
    sa.Column('file_path', sa.Text(), nullable=True),
    sa.Column('exposure_time', sa.Float(), nullable=True),
    sa.Column('iso', sa.Integer(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('capture_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['frameset_id'], ['frame_set.frameset_id'], ),
    sa.PrimaryKeyConstraint('frame_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('raw_frame')
    op.drop_table('processing_log')
    op.drop_table('image_session')
    op.drop_table('image_object')
    op.drop_table('image_gear')
    op.drop_table('frame_summary')
    op.drop_table('frame_set')
    op.drop_table('session')
    op.drop_table('image')
    op.drop_table('gear')
    op.drop_table('user')
    op.drop_table('location')
    op.drop_table('celestial_object')
    # ### end Alembic commands ###
