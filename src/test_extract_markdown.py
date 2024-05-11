import unittest
from inline_markdown import (
    extract_markdown_links,
    extract_markdown_images
)

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_md_images(self):
        node = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        new_nodes = extract_markdown_images(node)
        self.assertEqual(
            [('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')]
        ,
        new_nodes,
        )
    
    def test_extract_md_links(self):
        node = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        new_nodes = extract_markdown_links(node)
        self.assertEqual(
            [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        ,
        new_nodes,
        )

    def test_extract_md_images2(self):
        node = "This is a very simple ![image](www.9gag.com/file.jpeg) test"
        new_nodes = extract_markdown_images(node)
        self.assertEqual(
            [('image', 'www.9gag.com/file.jpeg')],
        new_nodes,
        )

if __name__ == "__main__":
    unittest.main()