import pytest
from unittest.mock import MagicMock, patch
import pandas as pd
from franz.openrdf.query.queryresult import TupleQueryResult
from franz.openrdf.repository.repositoryconnection import RepositoryConnection
from agraph_utils.utilities import query

@pytest.fixture
def mock_conn():
    return MagicMock(spec=RepositoryConnection)

#TODO Fix this test
# def test_query_returns_dataframe(mock_conn):
#     # Mock the connection's query method to return a TupleQueryResult
#     mock_result = MagicMock(spec=TupleQueryResult)
#     mock_conn.prepareTupleQuery.return_value.evaluate.return_value = mock_result
    
#     # Mock the conversion to DataFrame
#     with patch('agraph_utils.utilities.pd.DataFrame', return_value=pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})):
#         result = query(mock_conn, "SELECT * WHERE {?s ?p ?o}", results_format="df")
#         assert isinstance(result, pd.DataFrame)
#         assert not result.empty

#TODO Fix this test
# def test_query_returns_list(mock_conn):
#     # Mock the connection's query method to return a TupleQueryResult
#     mock_result = MagicMock(spec=TupleQueryResult)
#     mock_conn.prepareTupleQuery.return_value.evaluate.return_value = mock_result
    
#     # Mock the conversion to list of dictionaries
#     mock_result_to_list = [{"col1": 1, "col2": 3}, {"col1": 2, "col2": 4}]
#     mock_result.__iter__.return_value = iter(mock_result_to_list)
    
#     with patch('agraph_utils.utilities._to_dict', side_effect=lambda x: x):
#         result = query(mock_conn, "SELECT * WHERE {?s ?p ?o}", results_format="list")
#         assert isinstance(result, list)
#         assert len(result) == 2

def test_query_returns_generator(mock_conn):
    # Mock the connection's query method to return a TupleQueryResult
    mock_result = MagicMock(spec=TupleQueryResult)
    mock_conn.prepareTupleQuery.return_value.evaluate.return_value = mock_result
    
    result = query(mock_conn, "SELECT * WHERE {?s ?p ?o}", results_format="generator")
    assert isinstance(result, TupleQueryResult)

def test_query_invalid_format(mock_conn):
    with pytest.raises(ValueError):
        query(mock_conn, "SELECT * WHERE {?s ?p ?o}", results_format="invalid_format")

if __name__ == "__main__":
    pytest.main()