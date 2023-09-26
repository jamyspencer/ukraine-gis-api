def feature_group(child_array: [dict], name: str = "") -> dict:
    group = { "type": "FeatureCollection", "name": name, "features": child_array }
    return group