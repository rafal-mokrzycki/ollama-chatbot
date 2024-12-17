import pytest
from utils.loader import PineconeConnection


@pytest.fixture(name="pinecone_index_name")
def pinecone_index_name():
    yield "british-airways-test"


def test_create_index(pinecone_index_name):
    pi = PineconeConnection(index_name=pinecone_index_name)
    pi.create_index()
    assert pinecone_index_name in pi.pinecone.list_indexes().names()
    pi.pinecone.delete_index(pinecone_index_name)


def test_delete_index(pinecone_index_name):
    pi = PineconeConnection(index_name=pinecone_index_name)
    pi.create_index()
    pi._delete_index()
    assert pinecone_index_name not in pi.pinecone.list_indexes().names()


# def test_delete_data(pinecone_index_name):
#     pi = PineconeConnection(index_name=pinecone_index_name)
#     pi.create_index()
#     pi.load_data_into_index(csv_sample_filepath)
#     pi._delete_data(namespace="sentences_raw")
#     description = pi.pinecone.Index(pinecone_index_name).describe_index_stats()
#     assert description["total_vector_count"] == 0
#     pi.pinecone.delete_index(pinecone_index_name)
