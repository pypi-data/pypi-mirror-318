import csv
import pyodbc
from io import StringIO
from azure.storage.blob import BlobClient

def load_to_csv(sql_query, connection_string, container_name, folder_path, file_name, azure_blob_url, sas_token):
    try:
        # Connect to the database and execute the query
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        conn.close()

        # Create CSV content
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(columns)
        writer.writerows(rows)
        output.seek(0)

        # Ensure folder path ends with '/'
        if not folder_path.endswith('/'):
            folder_path += '/'

        # Construct the Blob URL
        blob_url = f"{azure_blob_url}/{container_name}/{folder_path}{file_name}"
        
        # Create BlobClient with SAS token
        blob_client = BlobClient.from_blob_url(blob_url, credential=sas_token)
        
        # Upload CSV content to Azure Blob Storage
        blob_client.upload_blob(output.getvalue(), overwrite=True)

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