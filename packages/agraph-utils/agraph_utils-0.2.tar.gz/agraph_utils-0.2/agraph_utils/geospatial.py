import json
from franz.openrdf.repository.repositoryconnection import RepositoryConnection
from franz.openrdf.model.literal import Literal
from typing import Any

class GeoJSON:
    def __init__(self, conn: RepositoryConnection) -> None:
            """
            Initializes a class that allows for easy conversion of coordinates
              to geospatial RDF literal objects.

            Args:
                conn (RepositoryConnection): The connection to the repository.

            Returns:
                None
            """
            self.conn = conn
            self.geo = self.conn.namespace('http://www.opengis.net/ont/geosparql#')

    def create_point(self, lon: float, lat: float) -> Literal:
        """
        Creates a GeoJSON Point object with the given 
               longitude and latitude coordinates.

        Args:
            lon (float): The longitude coordinate.
            lat (float): The latitude coordinate.

        Returns:
            Literal: A GeoJSON Point object as a RDF literal.

        """
        point = f"""{{"type": "Point", "coordinates": [{str(lon)}, {str(lat)}] }}"""
        return self.conn.createLiteral(point, datatype=self.geo.geoJSONLiteral)
    
    def create_line(self, startLon: float, startLat: float,
                          endLon: float, endLat:float) -> Literal:
            """
            Create a LineString geometry object with the given start 
                 and end coordinates.

            Args:
                startLon (float): The longitude of the start point.
                startLat (float): The latitude of the start point.
                endLon (float): The longitude of the end point.
                endLat (float): The latitude of the end point.

            Returns:
                Literal: An RDF Literal object representing 
                          the LineString geometry.
            """
            line = f"""{{"type": "LineString", "coordinates": [[{startLon}, {startLat}], [{endLon}, {endLat}]]}}"""
            return self.conn.createLiteral(line,
                                           datatype=self.geo.geoJSONLiteral)

    def convert_geo_cell_to_literal(self,
                                    geometry_cell: dict,
                                    shape: str = 'MultiPolygon') -> Literal:
        """
        Converts a geometry cell to a literal value.

        Args:
            geometry_cell (dict): The geometry cell to convert.
            shape (str, optional): The shape of the geometry.
                                    Defaults to 'MultiPolygon'.

        Returns:
            Literal: The converted literal value.
        """
        if shape == 'MultiPolygon':
            _json = {"type": "MultiPolygon", "coordinates": []}
            for geom in geometry_cell.geoms:
                multi = []
                for point in geom.exterior.coords:
                    coordinates = [point[0], point[1]]
                    multi.append(coordinates)
                _json["coordinates"].append([multi])
            json_string = json.dumps(_json)
            return self.conn.createLiteral(json_string,
                                           datatype=self.geo.geoJSONLiteral)
        else:
            pass
