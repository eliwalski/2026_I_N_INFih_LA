import json
import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEqual({"imie": "Eliasz", "msg": "Hello World!"},
                         json.loads(rv.data))

    def test_msg_with_xml_output(self):
        rv = self.app.get('/?output=xml')
        expected = (b'<greetings>\n'
                    b'  <name>Eliasz</name>\n'
                    b'  <msg>Hello World!</msg>\n'
                    b'</greetings>')
        self.assertEqual(expected, rv.data)

    def test_nameset_with_xml_output(self):
        rv = self.app.get('/?name=Apolonia&output=xml')
        expected = (b'<greetings>\n'
                    b'  <name>Apolonia</name>\n'
                    b'  <msg>Hello World!</msg>\n'
                    b'</greetings>')
        self.assertEqual(expected, rv.data)
