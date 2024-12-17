from pinecone import Pinecone, ServerlessSpec
from pinecone.core.openapi.shared.exceptions import (
    PineconeApiException,
    NotFoundException,
)

from cfg.config import load_config

config = load_config()


class PineconeConnection:
    def __init__(
        self,
        index_name: str | None = None,
        pinecone_api_key: str | None = None,
        metrics: str = "cosine",
        dimension: int = 1536,
        cloud: str = "aws",
        region: str = "us-east-1",
    ):
        if index_name is None:
            self.index_name = config["pinecone"]["index_name"]
        if pinecone_api_key is None:
            self.pinecone_api_key = config["pinecone"]["api_key"]
        embeddings = ""
        self.pinecone = Pinecone(api_key=self.pinecone_api_key)
        self.metrics = metrics
        self.dimension = dimension
        self.cloud = cloud
        self.region = region
        self.vector_db = Pinecone.from_existing_index(index_name, embeddings)

    def create_index(self) -> None:
        """
        Creates index if not exists.
        """
        try:
            self.pinecone.create_index(
                name=self.index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
            print(f"Index `{self.index_name}` created.")
        except PineconeApiException:
            print(f"Index `{self.index_name}` already exists.")

    def _delete_index(self) -> None:
        """
        Deletes index.
        """
        try:
            self.pinecone.delete_index(self.index_name)
            print(f"Index `{self.index_name}` deleted.")
        except NotFoundException:
            print(f"Index `{self.index_name}` not found.")

    def _delete_data(self, namespace: str) -> None:
        """
        Deletes all data in a given namespace.

        Args:
            namespace (str): Namespace to delete data in.
        """
        self.pinecone.index.delete(delete_all=True, namespace=namespace)
        print(f"All data in namespace `{namespace}` successfully deleted.")

    def show_statistics(self):
        """
        Prints out Pinecone index statistics in JSON format.

        Example:
        --------
        {
        'deletion_protection': 'disabled',
        'dimension': 1536,
        'host': 'my-index-828a150.svc.aped-4627-b74a.pinecone.io',
        'metric': 'cosine',
        'name': 'my-index',
        'spec': {
            'serverless': {
                'cloud': 'aws', 'region': 'us-east-1'
            }
        },
        'status': {
            'ready': True, 'state': 'Ready'
            }
        }
        """
        return self.pinecone.Index(self.index_name).describe_index_stats()

    def __repr__(self):
        return str(self.pinecone.describe_index(self.index_name))
