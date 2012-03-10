try:
    from json import loads as jsonsload
except ImportError:
    from simplejson import loads as jsonsload
    
class BaseJSONProcessor(object):
    def __init__(self, json_dict):
        for k,v in json_dict.iteritems():
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
