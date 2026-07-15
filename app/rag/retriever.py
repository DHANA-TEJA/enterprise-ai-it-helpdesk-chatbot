from sentence_transformers import SentenceTransformer
import chromadb

from app.rag.loader import KnowledgeLoader


class KnowledgeRetriever:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.client = chromadb.Client()

        self.collection = self.client.get_or_create_collection(
            "enterprise_helpdesk"
        )

        self._index_documents()

    def _index_documents(self):

        if self.collection.count() > 0:
            return

        docs = KnowledgeLoader.load_documents()

        for i, doc in enumerate(docs):

            embedding = self.model.encode(
                doc["content"]
            ).tolist()

            self.collection.add(

                ids=[str(i)],

                embeddings=[embedding],

                documents=[doc["content"]],

                metadatas=[

                    {
                        "source": doc["source"]
                    }
                ]
            )

    def search(self, query):

        embedding = self.model.encode(
            query
        ).tolist()

        results = self.collection.query(

            query_embeddings=[embedding],

            n_results=1
        )

        return results["documents"][0]