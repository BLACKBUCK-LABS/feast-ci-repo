from datetime import timedelta
from feast import RedshiftSource, Entity, Feature, FeatureView, ValueType

mp_sp_ll_lt_fv = FeatureView(
    name="mp_sp_ll_lt",
    entities=["sp_id", "from_location_id", "to_location_id"],
    ttl=timedelta(weeks=3650),
    features=[
        Feature(name="find_loads", dtype=ValueType.INT32),
        Feature(name="indent_click", dtype=ValueType.INT32),
        Feature(name="select_truck_type", dtype=ValueType.INT32),
        Feature(name="book_load", dtype=ValueType.INT32),
        Feature(name="bid", dtype=ValueType.INT32),
        Feature(name="call", dtype=ValueType.INT32),
        Feature(name="confirm_booking", dtype=ValueType.INT32)
    ],
    batch_source = RedshiftSource(
    table="mp_sp_ll_lt",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
)
)