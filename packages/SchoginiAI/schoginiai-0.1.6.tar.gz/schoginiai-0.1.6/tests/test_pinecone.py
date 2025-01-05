import unittest
from unittest.mock import patch
from SchoginiAI import SchoginiAIRAG
import os

class TestSchoginiAIRAG(unittest.TestCase):
    def setUp(self):
        self.api_key = "test_openai_api_key"
        self.pinecone_api_key = "test_pinecone_api_key"
        self.text_data = "Schogini Systems is a pioneer in AI Chatbots. We specialize in automation solutions for small businesses."
    
    @patch('SchoginiAI.main.pinecone')
    def test_pinecone_vector_store_creation(self, mock_pinecone):
        os.environ['VECTOR_STORE_TYPE'] = 'pinecone'
        os.environ['PINECONE_API_KEY'] = self.pinecone_api_key
        os.environ['PINECONE_ENVIRONMENT'] = 'us-west1-gcp'
        os.environ['PINECONE_INDEX_NAME'] = 'test-index'
        
        rag_ai = SchoginiAIRAG(
            openai_api_key=self.api_key,
            pinecone_api_key=self.pinecone_api_key,
            vector_store_type='pinecone',
            pinecone_index_name='test-index'
        )
        
        rag_ai.build_vector_store(self.text_data)
        
        mock_pinecone.init.assert_called_with(api_key=self.pinecone_api_key, environment='us-west1-gcp')
        mock_pinecone.create_index.assert_called_with('test-index', dimension=rag_ai._vector_store.embedding.dimension)
        mock_pinecone.Index.assert_called_with('test-index')
    
    def tearDown(self):
        del os.environ['VECTOR_STORE_TYPE']
        del os.environ['PINECONE_API_KEY']
        del os.environ['PINECONE_ENVIRONMENT']
        del os.environ['PINECONE_INDEX_NAME']

if __name__ == '__main__':
    unittest.main()

