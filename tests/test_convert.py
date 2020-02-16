import os
import unittest

from spreadsheetconverter import Converter, YamlConfig
from spreadsheetconverter.exceptions import TargetFieldDoesNotExistError, ForeignkeyTargetDataDoesNotExistError


class TestConvert(unittest.TestCase):
    def setUp(self):
        sample_path = os.path.join(os.getcwd(), '..', 'sample')
        base_dir = os.path.abspath(sample_path)

        os.environ.setdefault('SSC_SEARCH_PATH', base_dir)
        os.environ.setdefault('SSC_YAML_SEARCH_PATH', os.path.join(base_dir, 'yaml'))
        os.environ.setdefault('SSC_YAML_SEARCH_RECURSIVE', '1')
        os.environ.setdefault('SSC_XLS_SEARCH_PATH', os.path.join(base_dir, 'xls'))
        os.environ.setdefault('SSC_XLS_SEARCH_RECURSIVE', '1')
        os.environ.setdefault('SSC_JSON_BASE_PATH', os.path.join(base_dir, 'json'))

    def test_convert(self):
        Converter(YamlConfig.get_config('dummy1.yaml')).run()
        Converter(YamlConfig.get_config('dummy2.yaml')).run()

    def test_nothing_field_convert_error(self):
        with self.assertRaises(TargetFieldDoesNotExistError):
            Converter(YamlConfig.get_config('nothing_field.yaml')).run()

    def test_nothing_foreignkey_convert_error(self):
        with self.assertRaises(ForeignkeyTargetDataDoesNotExistError):
            Converter(YamlConfig.get_config('nothing_foreignkey.yaml')).run()
