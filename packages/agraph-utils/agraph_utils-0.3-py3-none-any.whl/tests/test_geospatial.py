import pytest
from unittest.mock import MagicMock
import json

from agraph_utils.geospatial import GeoJSON


@pytest.fixture
def mock_conn():
    conn = MagicMock()
    conn.namespace.return_value = MagicMock(geoJSONLiteral="geoJSONLiteral")
    conn.createLiteral = MagicMock(side_effect=lambda x, datatype: f"Literal({x}, {datatype})")
    return conn

def test_create_point(mock_conn):
    geojson = GeoJSON(mock_conn)
    lon, lat = 12.34, 56.78
    result = geojson.create_point(lon, lat)
    expected = 'Literal({"type": "Point", "coordinates": [12.34, 56.78] }, geoJSONLiteral)'
    assert result == expected

def test_create_line(mock_conn):
    geojson = GeoJSON(mock_conn)
    startLon, startLat, endLon, endLat = 12.34, 56.78, 98.76, 54.32
    result = geojson.create_line(startLon, startLat, endLon, endLat)
    expected = 'Literal({"type": "LineString", "coordinates": [[12.34, 56.78], [98.76, 54.32]]}, geoJSONLiteral)'
    assert result == expected

def test_convert_geo_cell_to_literal(mock_conn):
    geojson = GeoJSON(mock_conn)
    geometry_cell = MagicMock()
    geometry_cell.geoms = [MagicMock(exterior=MagicMock(coords=[(1, 2), (3, 4), (5, 6), (1, 2)]))]
    result = geojson.convert_geo_cell_to_literal(geometry_cell)
    expected_json = {
        "type": "MultiPolygon",
        "coordinates": [
            [[[1, 2], [3, 4], [5, 6], [1, 2]]]
        ]
    }
    expected = f'Literal({json.dumps(expected_json)}, geoJSONLiteral)'
    assert result == expected

if __name__ == "__main__":
    pytest.main()