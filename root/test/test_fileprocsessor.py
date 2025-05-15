# tests/test_fileprocessor.py
import os
import unittest
from fingerprint import FingerPrint
import fileprocessor

class TestFileProcessor(unittest.TestCase):
    """
    Tests for fileprocessor.py module using .txt files under root/data/.
    """
    @classmethod
    def setUpClass(cls):
        # Locate the data directory at project root
        tests_dir = os.path.dirname(__file__)
        project_root = os.path.abspath(os.path.join(tests_dir, '..'))
        cls.data_dir = os.path.join(project_root, 'data')
        # TODO: assert that data_dir exists and contains .txt files
        cls.sample_files = [
            os.path.join(cls.data_dir, fn)
            for fn in os.listdir(cls.data_dir)
            if fn.lower().endswith('.txt')
        ]

    def test_load_fingerprint(self):
        """
        For each real fingerprint file, load it and verify header fields.
        """
        for path in self.sample_files:
            with self.subTest(file=path):
                # TODO: Read the first four lines of 'path' manually
                # TODO: Call fileprocessor.load_fingerprint(path)
                # TODO: Assert get_name(), get_year(), get_rows(), get_cols()
                pass

    def test_main_access_granted(self):
        """
        Simulate entering the original file path and expect access granted.
        """
        # TODO: Set fileprocessor.original to one of the sample FingerPrint text files.
        # Pass that as input into the method which compares two fingerprints,
        # the second fingerprint being the same one as the original.
        # Use assertions to verify that the access is granted successfully when fingerprints match.
        
        # TODO: (OPTIONAL) Duplicate one of the fingerprint text files and change just a few characters
        # in the actual fingerprint. Now test that the access is granted successfully, given that
        # the error threshold is met.
        pass

    def test_main_lockout(self):
        """
        Simulate entering wrong files and expect lockout message after max_tries.
        """
        # TODO: Set fileprocessor.original appropriately.
        # Override input() to return wrong fingerprint repeatedly.
        # Set max_tries to small number.
        # Use assertions to ensure that the lockout message is displayed correctly. 
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)