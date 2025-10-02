from logger import logger

def query_chain(chain, user_query:str):
    try:
        logger.debug(f"running chain for input: {user_query}")
        result = chain({"query": user_query})
        response = {
            "response": result['result'],
            "sources": [doc.metadata.get("source","") for doc in result['source_documents']]
        }
        logger.debug(f"chain result: {response}")
        return response
        
    except Exception as e:
        logger.exception(f"Error on query_chain: {e}")
        raise