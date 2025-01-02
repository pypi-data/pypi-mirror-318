import requests
import os
from tqdm import tqdm

class Downloader():
    def __init__(self, urls, save_dir):
        """
        Initializes the Downloader with a list of URLs and a directory to save the downloaded files.

        Parameters:
        urls (list): A list of URLs to download files from.
        save_dir (str): The directory where the downloaded files will be saved.
        """
        self.urls = urls
        self.save_dir = save_dir

    def is_file_fully_downloaded(self, file_path, total_size):
        """
        Checks if the file at the given filepath is fully downloaded.

        Parameters:
        file_path (str): The path to the file to check.
        total_size (int): The expected size of the fully downloaded file.

        Returns:
        bool: True if the file exists and its size matches the expected total size, False otherwise.
        """
        return os.path.exists(file_path) and os.path.isfile(file_path) and total_size == os.path.getsize(file_path)

    def download(self):
        """
        Downloads the files from the list of URLs to the specified directory. Skips files that are already fully downloaded.
        """
        for url in self.urls:
            filename = url.split("/")[-1]
            file_path = os.path.join(self.save_dir, filename)

            response = requests.get(url, stream=True)
            possible_keys = ["Content-Length", "Content_Length", "content-length", "content_length", "ContentLength", "contentlength"]
            content_length_key = next((key for key in response.headers.keys() if key in possible_keys), None)

            total_size = int(response.headers.get(content_length_key, 0)) if content_length_key else 0
            block_size = 1024 

            if self.is_file_fully_downloaded(file_path, total_size):
                print(f"File {filename} is already Downloaded, Skipping...")
                continue

            with tqdm(desc=f"Downloading {filename}", total=total_size, unit='B', unit_divisor=block_size, unit_scale=True) as pbar:
                with open(file_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=block_size):
                        pbar.update(len(chunk))
                        f.write(chunk)
            
            print(f"File {filename} downloaded successfully")
