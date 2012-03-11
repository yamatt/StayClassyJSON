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
    from json import loads as jsonsload
except ImportError:
    from simplejson import loads as jsonsload
    
class BaseJSONProcessor(object):
    def __init__(self, json_dict):
        for k,v in json_dict.items():
            if isinstance(v, dict):
                setattr(self, k, BaseJSONProcessor(v))
            else:
                setattr(self, k, v)
                
class ClassyJSON(BaseJSONProcessor):
    def __init__(self, json_dict):
        BaseJSONProcessor.__init__(self, json_dict)
        
class ClassyJSONString(BaseJSONProcessor):
    def __init__(self, json_string):
        json_str = jsonsload(json_string)
        BaseJSONProcessor.__init__(self, json_str)
        
class ClassyJSONFile(ClassyJSONString):
    def __init__(self, json_file):
        data = json_file.read()
        ClassyJSONString.__init__(self, data)
