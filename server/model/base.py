from sqlalchemy.orm import DeclarativeBase
from geoalchemy2.shape import to_shape 
from shapely import to_geojson
import json
class Base(DeclarativeBase):
    def to_geo_json(self):
        geo_data = { "type": "Feature", "properties": { } }
        props = geo_data["properties"]
        for key, value in vars(self).items():
            if key == 'geom':
                val = to_geojson(to_shape(value))
                geo_data["geometry"] = json.loads(val)
            else:
                props[key] = value
        return geo_data


