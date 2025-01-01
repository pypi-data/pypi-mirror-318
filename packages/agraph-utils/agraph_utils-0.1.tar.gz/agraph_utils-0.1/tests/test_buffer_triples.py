import pytest
from unittest.mock import MagicMock
from agraph_utils.buffer_triples import BufferTriples

@pytest.fixture
def mock_connection():
    return MagicMock()

@pytest.fixture
def buffer_triples(mock_connection):
    return BufferTriples(mock_connection, buffer_size=3)

def test_add_triple(buffer_triples):
    triple = ['subject', 'predicate', 'object']
    buffer_triples.add_triple(triple)
    assert len(buffer_triples.buffer) == 1
    assert buffer_triples.buffer[0] == triple

def test_buffer_flush(buffer_triples):
    triple = ['subject', 'predicate', 'object']
    for _ in range(3):
        buffer_triples.add_triple(triple)
    assert len(buffer_triples.buffer) == 0
    assert buffer_triples.conn.addTriples.call_count == 1

def test_partial_flush(buffer_triples):
    triple = ['subject', 'predicate', 'object']
    for _ in range(2):
        buffer_triples.add_triple(triple)
    assert len(buffer_triples.buffer) == 2
    assert buffer_triples.conn.addTriples.call_count == 0

if __name__ == "__main__":
    pytest.main()