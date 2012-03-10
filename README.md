# StayClassyJSON
StayClassyJSON was written in reponse to how messy using JSON dictionaries are in Python and using dot-notation is *so* much easier.

## Usage
There is more than enough information about how to use this module in the `test_StayClassyJSON` file. But here are some real world examples here:

    >>> from StayClassyJSON import ClassyJSON
    >>> SAMPLE_JSON = {
    ...   'foo': {
    ...     'bar': 123
    ...   },
    ...   'boo': [1, 2, 3],
    ...   'mar': "par"
    ... }
    >>> example = ClassyJSON(SAMPLE_JSON)
    >>> example.foo.bar
    123
 
There is also ClassyJSONString for when you know your JSON will be held in a string and ClassyJSONFile for when you know your JSON will be stored in a file. You can open the file and just pass that class the file object.

## Note
ClassyJSON could be used to turn any dictionary object in to a class like object.

## License
GPLv3
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
