# Data downloading and extraction
import os
import requests
import zipfile
from tqdm import tqdm

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in tqdm(response.iter_content(CHUNK_SIZE)):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


if __name__ == "__main__":
    file_id = '1ZBC4cPItmnZ594t55R0SmK4FpU1rH13A'
    path_to_zip_file = 'datasets.zip'
    directory_to_extract_to ='src/'
    download_file_from_google_drive(file_id, path_to_zip_file)
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    print("Data downloaded successfully.")
    os.rename('src/datarush', 'src/dataset')
    os.remove('datasets.zip')
    print("Removed Zipfile")
