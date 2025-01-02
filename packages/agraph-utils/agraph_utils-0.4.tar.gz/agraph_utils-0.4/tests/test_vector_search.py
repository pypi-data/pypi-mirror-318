import pytest
from unittest.mock import MagicMock
import pandas as pd
from agraph_utils.vector_search import VectorSearch

@pytest.fixture
def vector_search():
    # Create mock objects for conn and vdb
    mock_conn = MagicMock()
    mock_vdb = MagicMock()
    return VectorSearch(conn=mock_conn, vdb=mock_vdb)

def test_nearest_neighbor_default(vector_search):
    # Mock the method's return value
    vector_search.nearestNeighbor = MagicMock(return_value=pd.DataFrame({"result": [1, 2, 3]}))
    
    result = vector_search.nearestNeighbor("test")
    assert isinstance(result, pd.DataFrame)
    assert not result.empty

def test_nearest_neighbor_custom_params(vector_search):
    # Mock the method's return value
    vector_search.nearestNeighbor = MagicMock(return_value=[{"result": 1}, {"result": 2}])
    
    result = vector_search.nearestNeighbor("test", n=5, minScore=0.5, results_format="list")
    assert isinstance(result, list)
    assert len(result) == 2

def test_nearest_neighbor_edge_case(vector_search):
    # Mock the method's return value
    vector_search.nearestNeighbor = MagicMock(return_value=pd.DataFrame())
    
    result = vector_search.nearestNeighbor("")
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_ask_my_documents_default(vector_search):
    # Mock the method's return value
    vector_search.ask_my_documents = MagicMock(return_value=pd.DataFrame({"response": ["answer1", "answer2"], "score": [0.9, 0.85]}))
    
    result = vector_search.ask_my_documents("test")
    assert isinstance(result, pd.DataFrame)
    assert not result.empty

def test_ask_my_documents_custom_params(vector_search):
    # Mock the method's return value
    vector_search.ask_my_documents = MagicMock(return_value=[{"response": "answer1", "score": 0.9}, {"response": "answer2", "score": 0.85}])
    
    result = vector_search.ask_my_documents("test", n=5, minScore=0.5, results_format="list")
    assert isinstance(result, list)
    assert len(result) == 2

def test_ask_my_documents_edge_case(vector_search):
    # Mock the method's return value
    vector_search.ask_my_documents = MagicMock(return_value=pd.DataFrame())
    
    result = vector_search.ask_my_documents("")
    assert isinstance(result, pd.DataFrame)
    assert result.empty

if __name__ == "__main__":
    pytest.main()