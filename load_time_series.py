import requests


def download_time_series(url, file_path):
    """
    Download file from URL and save it in directory time_series_data
    :param url: (str) URL with data
    :param file_path: directory time_series_data with file
    :return: None
    """
    try:
        response = requests.get(url, stream=True)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f'File saved: {file_path}')
    except requests.exceptions.RequestException as err:
        print(f'Downloading error: {err}')
