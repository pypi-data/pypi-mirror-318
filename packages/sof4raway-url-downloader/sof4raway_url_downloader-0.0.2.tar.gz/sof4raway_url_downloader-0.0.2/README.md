# URL Downloader

A custom Python library for downloading files from a URL.

## Features

- Download multiple files from a list of URLs.
- Resume interrupted downloads.
- Display progress of downloads using `tqdm`.

## Installation

To install the library, you can use pip:
```sh
pip install url_downloader
```

## Usage

```python
from my_downloader import Downloader

# List of URLs to download files from
urls = ["http://example.com/file1.zip", "http://example.com/file2.zip"]

# Directory where the downloaded files will be saved
# It's recommended to use the os library to handle file paths and directories
save_dir = "./Downloads"

# Create a Downloader instance with the list of URLs and the save directory
downloader = Downloader(urls, save_dir)

# Start the download process
downloader.download()

```

## Requirements

- Python 3.10 or higher
- requests
- tqdm

## Contributing 

Contribution are welcomed! Please fork the repository and submit a pull request with your improvements.

## Author

- Muhammad Farid Rahman - [GitHub Profile](github.com/sof4raway)

## Acknowledgement

Thanks to the author of requests and tqdm for their excellent libraries