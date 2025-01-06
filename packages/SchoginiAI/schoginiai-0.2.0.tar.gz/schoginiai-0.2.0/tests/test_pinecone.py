import unittest
from SchoginiAI import SchoginiAIRAG
import settings
import os
# import warnings
# warnings.filterwarnings("ignore") #, category=DeprecationWarning, module="faiss.loader")

class TestVectorStoreSelection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up common configurations
        cls.sample_text = """
        Schogini Systems is a pioneer in AI Chatbots.
        We specialize in automation solutions for small businesses.
        """
        # cls.test_directory = "test_chroma_store"
        settings.vector_store_type = "pinecone"
        settings.vector_store_dir = "none"
        cls.test_directory = settings.vector_store_dir
    def test_chroma_selection(self):
        # Test if the vector store type is correctly set to Chroma
        rag_ai = SchoginiAIRAG()
        self.assertEqual(rag_ai.vector_store_type, "pinecone")

    def test_build_and_save_vector_store(self):
        # Test building and saving a Chroma vector store
        rag_ai = SchoginiAIRAG()
        rag_ai.build_vector_store(self.sample_text)
        rag_ai.save_vector_store() #directory=self.test_directory)

        # Check if the Chroma directory was created
        # self.assertTrue(os.path.exists(self.test_directory))
        # print(f"Vector store saved at {self.test_directory}")

    def test_load_vector_store(self):
        # Test loading the Chroma vector store
        rag_ai = SchoginiAIRAG()
        rag_ai.load_vector_store()
        self.assertIsNotNone(rag_ai._retriever)
        print("Vector store loaded successfully")

    def test_query_vector_store(self):
        # Test querying the Chroma vector store
        rag_ai = SchoginiAIRAG()
        rag_ai.load_vector_store()
        answer = rag_ai.ask_question("What is your company doing?")

        # Verify the structure of the returned result
        self.assertIsInstance(answer, dict, "The response should be a dictionary.")
        self.assertIn('query', answer, "The response should include a 'query' key.")
        self.assertIn('result', answer, "The response should include a 'result' key.")
        
        # Verify the content of the result
        self.assertEqual(answer['query'], "What is your company doing?", "Query does not match.")
        self.assertIsInstance(answer['result'], str, "The result value should be a string.")
        print("Query Answer:", answer['result'])


    @classmethod
    def tearDownClass(cls):
        # Clean up test directory after tests
        if os.path.exists(cls.test_directory):
            for root, dirs, files in os.walk(cls.test_directory, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(cls.test_directory)
        print("Cleaned up test directory")

if __name__ == '__main__':
    unittest.main()




# from SchoginiAI import SchoginiAIRAG
# import settings
# rag_ai = SchoginiAIRAG()

# # Your text corpus
# sample_text = """
# Schogini Systems is a pioneer in AI Chatbots.
# We specialize in automation solutions for small businesses.
# """
# rag_ai.save_vector_store()
# rag_ai.load_vector_store()

# answer = rag_ai.ask_question("Do you offer image recognition?")
# print("Answer:", answer)
