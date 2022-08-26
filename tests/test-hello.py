import os.path as pth
import unittest
from docxpy import DOCReader

test_file = pth.join(pth.split(__file__)[0], "Hello.docx")


class Test(unittest.TestCase):
    def setUp(self):
        self.file = DOCReader(test_file)
        self.file.process()

    def test_file_data(self):
        self.assertIsInstance(self.file.data, dict)
        self.assertTrue("header" in self.file.data)
        self.assertTrue("footer" in self.file.data)
        self.assertTrue("document" in self.file.data)

    def test_hyperlinks(self):
        links = self.file.data["links"]
        self.assertEqual(
            links, [("This is a hyperlink.".encode("utf-8"), "https://www.google.com/")]
        )

    def test_text_fobject(self):
        file = DOCReader(open(test_file, "rb"))
        file.process()
        text = file.data["document"].replace("\n", "")
        self.assertEqual(text, "TitleThis is a hyperlink.")

    def test_text(self):
        text = self.file.data["document"].replace("\n", "")
        self.assertEqual(text, "TitleThis is a hyperlink.")


if __name__ == "__main__":
    unittest.main()
