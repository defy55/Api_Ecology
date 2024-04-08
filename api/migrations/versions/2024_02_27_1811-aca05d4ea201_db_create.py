"""DB create

Revision ID: aca05d4ea201
Revises: 
Create Date: 2024-02-27 18:11:38.384749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aca05d4ea201'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('analysis',
    sa.Column('analysis_id', sa.Integer(), nullable=False),
    sa.Column('district_location_id', sa.String(), nullable=False),
    sa.Column('analysis_type', sa.String(), nullable=False),
    sa.Column('result', sa.String(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_analysis_id'), 'analysis', ['id'], unique=False)
    op.create_table('districts',
    sa.Column('district_number', sa.Integer(), nullable=False),
    sa.Column('district_name', sa.String(), nullable=False),
    sa.Column('district_category', sa.String(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_districts_id'), 'districts', ['id'], unique=False)
    op.create_table('forecasts',
    sa.Column('forecast_id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('rating', sa.String(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_forecasts_id'), 'forecasts', ['id'], unique=False)
    op.create_table('mobile_sensors',
    sa.Column('power_source', sa.String(length=20), nullable=False),
    sa.Column('battery_level', sa.Float(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('error_status', sa.String(), nullable=False),
    sa.Column('activity_time', sa.String(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mobile_sensors_id'), 'mobile_sensors', ['id'], unique=False)
    op.create_table('routes',
    sa.Column('route_number', sa.Integer(), nullable=False),
    sa.Column('start_point', sa.String(), nullable=False),
    sa.Column('end_point', sa.String(), nullable=False),
    sa.Column('creation_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.Column('base_point', sa.String(), nullable=False),
    sa.Column('district_number', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_routes_id'), 'routes', ['id'], unique=False)
    op.create_table('sensor_data',
    sa.Column('data_id', sa.Integer(), nullable=False),
    sa.Column('data_type', sa.String(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('route_id', sa.Integer(), nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('sensor_type', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensor_data_id'), 'sensor_data', ['id'], unique=False)
    op.create_table('stationary_sensors',
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('power_source', sa.String(length=20), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('error_status', sa.String(), nullable=True),
    sa.Column('activity_time', sa.Integer(), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stationary_sensors_id'), 'stationary_sensors', ['id'], unique=False)
    op.create_table('user',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('fio', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('refresh_session',
    sa.Column('refresh_token', sa.UUID(), nullable=False),
    sa.Column('expires_in', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_refresh_session_id'), 'refresh_session', ['id'], unique=False)
    op.create_index(op.f('ix_refresh_session_refresh_token'), 'refresh_session', ['refresh_token'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_refresh_session_refresh_token'), table_name='refresh_session')
    op.drop_index(op.f('ix_refresh_session_id'), table_name='refresh_session')
    op.drop_table('refresh_session')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_stationary_sensors_id'), table_name='stationary_sensors')
    op.drop_table('stationary_sensors')
    op.drop_index(op.f('ix_sensor_data_id'), table_name='sensor_data')
    op.drop_table('sensor_data')
    op.drop_index(op.f('ix_routes_id'), table_name='routes')
    op.drop_table('routes')
    op.drop_index(op.f('ix_mobile_sensors_id'), table_name='mobile_sensors')
    op.drop_table('mobile_sensors')
    op.drop_index(op.f('ix_forecasts_id'), table_name='forecasts')
    op.drop_table('forecasts')
    op.drop_index(op.f('ix_districts_id'), table_name='districts')
    op.drop_table('districts')
    op.drop_index(op.f('ix_analysis_id'), table_name='analysis')
    op.drop_table('analysis')
    # ### end Alembic commands ###
