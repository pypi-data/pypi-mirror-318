import unittest
from SchoginiAI import SchoginiAIRAG
import os
import settings

class TestVectorStoreSelection(unittest.TestCase):
    def test_faiss_selection(self):
        settings.vector_store_type = 'faiss'
        rag_ai = SchoginiAIRAG()
        self.assertEqual(rag_ai.vector_store_type, 'faiss')

    def test_chroma_selection(self):
        settings.vector_store_type = 'chroma'
        rag_ai = SchoginiAIRAG()
        self.assertEqual(rag_ai.vector_store_type, 'chroma')

    # def test_default_selection(self):
    #     if 'VECTOR_STORE_TYPE' in os.environ:
    #         del os.environ['VECTOR_STORE_TYPE']
    #     rag_ai = SchoginiAIRAG(openai_api_key="test_key")
    #     self.assertEqual(rag_ai.vector_store_type, 'faiss')

if __name__ == '__main__':
    unittest.main()

