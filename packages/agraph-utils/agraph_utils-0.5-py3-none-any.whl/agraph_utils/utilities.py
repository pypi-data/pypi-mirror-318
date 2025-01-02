from franz.openrdf.repository.repositoryconnection import RepositoryConnection
from franz.openrdf.query.queryresult import TupleQueryResult
from franz.openrdf.query.query import QueryLanguage
import pandas as pd
from typing import Union

def query(conn: RepositoryConnection,
          query: str,
          results_format: str = "df"
    ) -> Union[TupleQueryResult, pd.DataFrame, list[dict]]:
    """
    Executes a SPARQL query on a given connection and returns the
          results in the specified format.

    Args:
        conn (RepositoryConnection): The connection to the RDF repository.
        query (str): The SPARQL query to execute.
        results_format (str, optional): The format in which to return the results. 
            Valid options are 'df' (pandas DataFrame), 'list' (list of 
                 dictionaries), or 'generator' (SPARQL result generator).
            Defaults to 'df'.

    Returns:
        Union[TupleQueryResult, pd.DataFrame, list[dict]]: The query results 
                  in the specified format.

    Raises:
        ValueError: If the results_format is not one of 'df', 
               'list', or 'generator'.
    """
    if results_format == "df":
        with conn.executeTupleQuery(query) as result:
            return result.toPandas()
    elif results_format == "list":
        result = conn.prepareTupleQuery(QueryLanguage.SPARQL,
                                            query).evaluate()
        response = []
        with result:
            for binding_set in result:
                response.append(binding_set._toDict())
        return response
    elif results_format == "generator":
        result = conn.prepareTupleQuery(QueryLanguage.SPARQL,
                                            query).evaluate()
        return result
    else:
        raise ValueError("results_format must be 'df', 'list', or 'generator'")