import unittest
from unittest.mock import patch

from utils import init_db, get_data_directory, get_data_filepath


class TestUtils(unittest.TestCase):
    @patch('utils.get_data_directory')
    def test_get_data_filepath(self, mock_get_data_directory):
        mocked_return_value = '/path/to/directory/'
        mock_get_data_directory.return_value = mocked_return_value
        result = get_data_filepath()
        self.assertEqual(result, f'{mocked_return_value}data.csv')

    @patch('utils.get_data_directory')
    def test_get_data_filepath_func_called(self, mock_get_data_directory):
        get_data_filepath()
        self.assertTrue(mock_get_data_directory.called)

    def test_init_db_exception(self):
        import os
        try:
            del os.environ['DB_URL']
        except KeyError:
            pass
        self.assertRaises(ValueError, init_db)

    @patch('utils.uuid')
    @patch('utils.os')
    def test_get_data_directory(self, mock_os, mock_uuid):
        mocked_uui4_return_value = 'unique_number'
        mock_uuid.uuid4.return_value = mocked_uui4_return_value
        result = get_data_directory()
        self.assertEqual(result, f'./csv/{mocked_uui4_return_value}/')

    @patch('utils.uuid')
    @patch('utils.os')
    def test_get_data_directory_func_called(self, mock_os, mock_uuid):
        get_data_directory()
        self.assertTrue(mock_uuid.uuid4.called)

    @patch('utils.uuid')
    @patch('utils.os')
    def test_get_data_directory_func_called(self, mock_os, mock_uuid):
        get_data_directory()
        self.assertTrue(mock_os.makedirs.called)



if __name__ == '__main__':
    unittest.main()
