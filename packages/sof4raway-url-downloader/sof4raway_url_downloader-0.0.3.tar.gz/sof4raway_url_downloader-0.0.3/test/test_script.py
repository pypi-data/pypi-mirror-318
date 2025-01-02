import unittest
import os
from sof4raway_url_downloader import Downloader

class TestDownloader(unittest.TestCase):
    def setUp(self):
        self.urls = ["https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Ec5f3KYU1CpbKRp1whFLZw/new-Policies.txt",
       "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/94hiHUNLZdb0bLMkrCh79g/file-sample.docx",]
        self.save_dir = "./test_downloads"
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        self.downloader = Downloader(self.urls, self.save_dir)

    def test_initialization(self):
        self.assertEqual(self.downloader.urls, self.urls)
        self.assertEqual(self.downloader.save_dir, self.save_dir)

    def test_is_file_fully_downloaded(self):
        filepath = os.path.join(self.save_dir, "test_file.zip")
        # Create a dummy file
        with open(filepath, "wb") as f:
            f.write(b"dummy content")
        total_size = os.path.getsize(filepath)
        self.assertTrue(self.downloader.is_file_fully_downloaded(filepath, total_size))

    def tearDown(self):
        # Clean up: remove the test directory and its contents
        for file in os.listdir(self.save_dir):
            os.remove(os.path.join(self.save_dir, file))
        os.rmdir(self.save_dir)

if __name__ == '__main__':
    unittest.main()
