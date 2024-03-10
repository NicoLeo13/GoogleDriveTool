from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json

# Credenciales y ámbito de la API
SCOPES = ['https://www.googleapis.com/auth/drive']

#Autenticación con Google Drive.
def authenticate():
    with open('env\Include\credentials.json', 'r') as f:
        client_config = json.load(f)
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    return flow.run_local_server()

#Obtener la lista de archivos en una carpeta de Google Drive
def list_files(service, folder_id):
    results = service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name)").execute()
    return results.get('files', [])

#Renombrar los archivos que comienzan con un patrón específico
def rename_files(service, files, pattern):
    counter_total_files = len(files)
    counter_files_pattern = 0
    counter_success = 0
    for index, file in enumerate(files):
        if file['name'].startswith(pattern):
            counter_files_pattern += 1
            old_name = file['name']
            new_name = file['name'].replace(pattern, '', 1)
            file_id = file['id']
            service.files().update(fileId=file_id, body={'name': new_name}).execute()
            if file['name'] != old_name:
                counter_success += 1
    return counter_total_files, counter_files_pattern, counter_success

def main():
    # Crear un servicio de Google Drive
    service = build('drive', 'v3', credentials=authenticate())
    folder_id = input("\nEnter target folder ID: ")
    pattern = input("\nEnter file start pattern to remove: ")
    
    files = list_files(service, folder_id)
    counter_total_files, counter_files_pattern, counter_success = rename_files(service, files, pattern)
    
    print("\nTotal files found in folder: " + str(counter_total_files))
    print("Files found with pattern: " + str(counter_files_pattern))
    print("Files renamed successfully: " + str(counter_success))

if __name__ == "__main__":
    main()