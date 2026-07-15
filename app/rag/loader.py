import os

KNOWLEDGE_BASE_PATH = "knowledge_base"


class KnowledgeLoader:

    @staticmethod
    def load_documents():

        documents = []

        for file in os.listdir(KNOWLEDGE_BASE_PATH):

            if file.endswith(".md"):

                path = os.path.join(KNOWLEDGE_BASE_PATH, file)

                with open(path, "r", encoding="utf-8") as f:

                    documents.append({
                        "source": file,
                        "content": f.read()
                    })

        return documents