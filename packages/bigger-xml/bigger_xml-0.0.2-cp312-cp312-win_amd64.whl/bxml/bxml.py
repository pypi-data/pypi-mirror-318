# MIT License
# Copyright (c) 2025 Bhautik Sudani
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from bxml import xmlmodule

class _ElementWrapper:
    def __init__(self, pointer, root = False):
        self.root = root
        self.ptr = pointer

    @property
    def text(self):
        pass
    
    @text.setter
    def text(self, new_value):
        xmlmodule.setText(self.ptr,str(new_value))

    def set(self,key,value):
        try:
            xmlmodule.addKey(self.ptr,str(key),str(value))
            # _xmlCLib.setKey(self.ptr,str(key).encode(),str(value).encode())
        except Exception as e:
            print(str(e))

    def __del__(self):
        self.ptr = None

    def findAll(self,key):
        result_arr = xmlmodule.findAll(self.ptr,key)
        final_result= []
        for i,capsule in enumerate(result_arr):
            final_result.append(_ElementWrapper(capsule))
        return final_result
    
    def save(self,file_name,xmlDeclaration = True,encoding="ASCII"):
        try:
            xmlmodule.generateXML(self.ptr,file_name,encoding,xmlDeclaration)
            return {
                "status":0,
                "msg":"XML Generation Successfull."
            }
        except Exception as e:
            return {
                "status":1,
                "msg":"Exception While Generating XML."
            }
        

class etree:

    @staticmethod
    def Element(key):
        root_element = xmlmodule.baseElement(key)
        return _ElementWrapper(root_element)

    @staticmethod
    def SubElement(parent,key):
        element = xmlmodule.childElement(parent.ptr,key)
        return _ElementWrapper(element)
    
    @staticmethod
    def remove(element):
        xmlmodule.deleteElement(element.ptr)
        element.ptr = None
    