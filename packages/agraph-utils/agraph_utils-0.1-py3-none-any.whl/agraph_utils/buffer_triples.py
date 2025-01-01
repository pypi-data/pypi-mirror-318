from franz.openrdf.repository.repositoryconnection import RepositoryConnection

class BufferTriples:
    """
    A class for buffering triples and flushing them to an AG repository.

    Args:
        conn: The AG repository to which the triples will be flushed.
        buffer_size (int): The maximum size of the buffer before flushing.

    Attributes:
        conn: The connection object to which the triples will be flushed.
        buffer: The buffer that stores the triples.
        buffer_size (int): The maximum size of the buffer before flushing.
    """

    def __init__(self,
                 conn: RepositoryConnection,
                 buffer_size: int = 10000) -> None:
        self.conn = conn
        self.buffer = []
        self.buffer_size = buffer_size

    def add_triple(self, triple: list) -> None:
        """
        Add a single triple to the buffer. If the buffer is full, it will be
        flushed to the AG repository.

        Args:
            triple (list): The triple to be added to the buffer.
        """
        self.buffer.append(triple)
        if len(self.buffer) >= self.buffer_size:
            self.flush_buffer()
            self.buffer = []
    
    def add_triples(self, triples: list[list]) -> None:
        """
        Add multiple triples to the buffer. If the list is larger than the 
        buffer size, the buffer will be flushed.

        Args:
            triples (list[list]): The list of triples to be added 
                                     to the buffer.
        """
        self.buffer += triples
        if len(self.buffer) >= self.buffer_size:
            self.flush_buffer()
            self.buffer = []

    def flush_buffer(self) -> None:
        """
        Flush the buffer by adding its contents to the AG repository.
        """
        self.conn.addTriples(self.buffer)
