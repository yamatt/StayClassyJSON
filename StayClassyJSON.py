try:
    from json import loads as jsonsload
except ImportError:
    from simplejson import loads as jsonsload
    
class BaseJSONProcessor(object):
    def __init__(self, dict_obj):
        for k,v in dict_obj.iteritems():
            if isinstance(v, dict):
                setattr(self, k, BaseJSONProcessor(v))
            else:
                setattr(self, k, v)
    
class ClassyJSON(BaseJSONProcessor):
    def __init__(self, json_string):
        json = jsonsload(json_string)
        BaseJSONProcessor.__init__(self, json)
        
class ClassyJSONFile(ClassyJSON):
    def __init__(self, json_file):
        data = json_file.read()
        ClassyJSON.__init__(self, data)
