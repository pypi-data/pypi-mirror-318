from franz.openrdf.repository.repositoryconnection import RepositoryConnection
from franz.openrdf.query.queryresult import TupleQueryResult
from franz.openrdf.query.query import QueryLanguage
import pandas as pd
from typing import Union

class VectorSearch:
    def __init__(self,
                 conn: RepositoryConnection,
                 vdb: str) -> None:
        self.conn = conn
        self.vdb = vdb

    def nearestNeighbor(self,
                             text: str,
                             n: int = 10,
                             minScore: float = .8,
                             results_format: str = "df"
            ) -> Union[pd.DataFrame, list[dict], TupleQueryResult]:
            """
            Executes a nearest neighbor search query on the 
                        AllegroGraph database and specified vdb.

            Args:
                text (str): The text to search for.
                n (int, optional): The maximum number of results to return.
                                         Defaults to 10.
                minScore (float, optional): The minimum score threshold for 
                                                results. Defaults to 0.8.
                results_format (str, optional): The format of the results. 
                                        Can be 'df' (pandas DataFrame),
                    'list' (list of dictionaries), or 'generator' (SPARQL
                                         query result generator).
                    Defaults to 'df'.

            Returns:
                Union[pd.DataFrame, list[dict], TupleQueryResult]: The search 
                                        results in the specified format.
            """
            query_string = f"""
               PREFIX llm: <http://franz.com/ns/allegrograph/8.0.0/llm/> 
               SELECT ?uri ?score ?orignalText WHERE {{
                    ( ?uri ?score ?originalText )
                       llm:nearestNeighbor
                    ( "{text}" "{self.vdb}" {str(n)} {str(minScore)} ) . }}"""
            if results_format == "df":
                with self.conn.executeTupleQuery(query_string) as result:
                    return result.toPandas()
            elif results_format == "list":
                result = self.conn.prepareTupleQuery(QueryLanguage.SPARQL,
                                                    query_string).evaluate()
                response = []
                with result:
                    for binding_set in result:
                        response.append(binding_set._toDict())
                return response
            elif results_format == "generator":
                result = self.conn.prepareTupleQuery(QueryLanguage.SPARQL,
                                                    query_string).evaluate()
                return result
            else:
                raise ValueError("results_format must be 'df', 'list', or 'generator'")

    def ask_my_documents(self,
                       text: str,
                       n: int = 10,
                       minScore: float = .8,
                       results_format: str = "df"
            ) -> Union[pd.DataFrame, list[dict], TupleQueryResult]:
        query_string = f"""
           PREFIX llm: <http://franz.com/ns/allegrograph/8.0.0/llm/> 
           SELECT ?response ?score ?citation ?content WHERE {{
                ( ?response ?score ?citation ?content )
                   llm:askMyDocuments
                ( "{text}" "{self.vdb}" {str(n)} {str(minScore)} ) . }}"""
        if results_format == "df":
            with self.conn.executeTupleQuery(query_string) as result:
                return result.toPandas()
        elif results_format == "list":
            result = self.conn.prepareTupleQuery(QueryLanguage.SPARQL,
                                                query_string).evaluate()
            response = []
            with result:
                for binding_set in result:
                    response.append(binding_set._toDict())
            return response
        elif results_format == "generator":
            result = self.conn.prepareTupleQuery(QueryLanguage.SPARQL,
                                                query_string).evaluate()
            return result
        else:
            raise ValueError("results_format must be 'df', 'list', or 'generator'")
