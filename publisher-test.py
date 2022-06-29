import unittest
from mqtt_pub import parse_argv

class SimpleTest(unittest.TestCase):
    def test_conf_file_details(self):
        self.assertEqual(parse_argv(['--conf', 'pub_conf.json', '--data', 'data.json']),{'conf': 'pub_conf.json', 'data': 'data.json'})