import requests
from config import API_URL

def upload_files_api(files):
    files_payload = [('files', (file.name, file, 'application/pdf')) for file in files]
    try:
        response = requests.post(f"{API_URL}/upload_pdfs", files=files_payload)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Error uploading files: {e}")
        return None
    
    
def query_bot(question):
    try:
        response = requests.post(f"{API_URL}/ask/", data={"question": question})
        return response
    except requests.RequestException as e:
        print(f"Error querying bot: {e}")
        return None