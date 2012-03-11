#!/usr/bin/env python
"""
 This file is part of StayClassyJSON.

 StayClassyJSON is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 StayClassyJSON is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with StayClassyJSON.  If not, see <http://www.gnu.org/licenses/>.
"""

try:
    from json import dumps as jsonsdump
except ImportError:
    from simplejson import dumps as jsonsdump
import unittest
from io import StringIO

from StayClassyJSON import ClassyJSON, ClassyJSONString, ClassyJSONFile, BaseJSONProcessor


class BaseClassyJSONTests(unittest.TestCase):
    SAMPLE_JSON = {
        'foo': {
            'bar': 123
        },
        'boo': [1, 2, 3],
        'mar': "par"
    }
    
    def run_tests(self, classy_json):
        self.assertEqual(self.SAMPLE_JSON['foo']['bar'], classy_json.foo.bar)
        self.assertEqual(self.SAMPLE_JSON['boo'], classy_json.boo)
        self.assertEqual(self.SAMPLE_JSON['mar'], classy_json.mar)

class TestFileJson(BaseClassyJSONTests):
    def test_file_parser(self):
        json_str = jsonsdump(self.SAMPLE_JSON)
        json_file = StringIO(json_str)
        classy_json = ClassyJSONFile(json_file)
        self.run_tests(classy_json)
        
class TestStringJson(BaseClassyJSONTests):
    def test_json_parser(self):
        json_str = jsonsdump(self.SAMPLE_JSON)
        classy_json = ClassyJSONString(json_str)
        self.run_tests(classy_json)

class TestClassyJson(BaseClassyJSONTests):
    def test_json_parser(self):
        classy_json = ClassyJSON(self.SAMPLE_JSON)
        self.run_tests(classy_json)
        
class TestBaseJsonProcessor(BaseClassyJSONTests):
    def test_base_processor(self):
        classy_json = BaseJSONProcessor(self.SAMPLE_JSON)
        self.run_tests(classy_json)

if __name__ == "__main__":
    unittest.main()
