import unittest
from pathlib import Path

class WebsiteTests(unittest.TestCase):

    def test_html_file_exists(self):
        self.assertTrue(Path("index.html").is_file())

    def test_page_title_exists(self):
        content = Path("index.html").read_text(encoding="utf-8")
        self.assertIn("<title>Basic CI/CD Pipeline</title>", content)

    def test_welcome_heading_exists(self):
        content = Path("index.html").read_text(encoding="utf-8")
        self.assertIn("Welcome to My CI/CD Application", content)

if __name__ == "__main__":
    unittest.main()
