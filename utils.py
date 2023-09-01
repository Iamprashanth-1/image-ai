import g4f
import re
import cv2
class GPT4ALL:
    def __init__(self):
        pass

    def call(self,_promt):
        #print(_promt)
        response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', messages=[
                                     {"role": "user", "content": _promt}], stream=False)
        output = ''
        for message in response:
            output+= message
        #print(output)
        try:
            _code = re.search(r'<startCode>(.*?)<endCode>', output, re.DOTALL).group(1)
            return _code
        except:
            return None
        
def run_python_code(_code , args_dict):
    #print(args_dict)
    _code = 'import numpy as np\n'+_code
    print(_code)
    try:
        exec(_code, globals(), args_dict)

        result = args_dict['generate_code'](args_dict['_in_img'], args_dict['_out_img'])
        return result
    except Exception as e:
        #print(e ,'hi')
        return "Something went wrong. Please try again."