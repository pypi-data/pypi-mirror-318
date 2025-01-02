import json
import pyodbc
from azure.storage.blob import BlobServiceClient, BlobClient

def load_to_json(sql_query, connection_string, container_name, folder_path, file_name, azure_blob_url, sas_token):
    try:
        # Connect to the database and execute the query
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()

        # Convert rows to JSON
        json_data = json.dumps(rows, indent=4)

        # Ensure folder path ends with '/'
        if not folder_path.endswith('/'):
            folder_path += '/'

        # Create BlobClient with SAS token
        blob_url = f"{azure_blob_url}/{container_name}/{folder_path}{file_name}"
        blob_client = BlobClient.from_blob_url(blob_url, credential=sas_token)
        blob_client.upload_blob(json_data, overwrite=True)

        # Return status
        return {
            "status": "success",
            "message": f"Data successfully saved to Azure Storage at {folder_path + file_name}",
            "rows_uploaded": len(rows),
            "file_name": file_name,
            "container_name": container_name,
            "folder_path": folder_path,
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }