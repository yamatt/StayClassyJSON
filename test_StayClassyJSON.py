try:
    from json import dumps as jsonsdump
except ImportError:
    from simplejson import dumps as jsonsdump
import unittest
from StringIO import StringIO

from StayClassyJSON import ClassyJSONFile, ClassyJSON, BaseJSONProcessor


class BaseClassyJSONTests(unittest.TestCase):
    SAMPLE_JSON = {
        'foo': {
            'bar': 123
        },
        'boo': [1, 2, 3],
        'mar': "par"
    }
    
    def run_tests(self, classy_json):
        self.assertEquals(self.SAMPLE_JSON['foo']['bar'], classy_json.foo.bar)
        self.assertEquals(self.SAMPLE_JSON['boo'], classy_json.boo)
        self.assertEquals(self.SAMPLE_JSON['mar'], classy_json.mar)

class TestFileJson(BaseClassyJSONTests):
    def test_file_parser(self):
        json_str = jsonsdump(self.SAMPLE_JSON)
        json_file = StringIO(json_str)
        classy_json = ClassyJSONFile(json_file)
        self.run_tests(classy_json)
        
class TestStringJson(BaseClassyJSONTests):
    def test_json_parser(self):
        json_str = jsonsdump(self.SAMPLE_JSON)
        classy_json = ClassyJSON(json_str)
        self.run_tests(classy_json)
        
class TestBaseJsonProcessor(BaseClassyJSONTests):
    def test_base_processor(self):
        classy_json = BaseJSONProcessor(self.SAMPLE_JSON)
        self.run_tests(classy_json)

if __name__ == "__main__":
    unittest.main()
