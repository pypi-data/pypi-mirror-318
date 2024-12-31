#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Copyright (C) 2007-2024 Gaetan Delannay

# This file is part of Appy.

# Appy is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# Appy is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# Appy. If not, see <http://www.gnu.org/licenses/>.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import datetime
from base64 import decodebytes

from DateTime import DateTime

from appy.xml import Parser
from appy.utils.path import getShownSize
from appy.model.utils import Object as O

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CONVERSION_ERROR = '"%s" value "%s" could not be converted by the XML ' \
                   'unmarshaller.'
CUSTOM_CONVERSION_ERROR = 'Custom converter for "%s" values produced an ' \
                          'error while converting value "%s". %s'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class UnmarshalledFile:
    '''Used for reading XML-marshalled files and converting them to Python
       objects.'''

    def __init__(self):
        self.name = ''       # The name of the file on disk
        self.type = None     # The MIME type of the file
        self.value = b''     # The binary content of the file or a file object
        self.size = 0        # The length of the file in bytes
        self.location = None # As an alternative to attributes "value" and
                             # "size", "location" may refer to the disk location
                             # of the file, if its content is not unmarshalled
                             # on p_self.

    def __repr__(self):
        '''p_self's short string representation'''
        if self.location:
            info = '@%s' % self.location
        else:
            info = '(%s)' % getShownSize(self.size)
        return '<File %s %s>' % (self.name or '-unnamed-', info)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Unmarshaller(Parser):
    '''Allows to parse a XML file and recreate the corresponding web of Python
       objects.'''

    # This parser assumes that the XML file respects this convention: any tag
    # may define in attribute "type" storing the type of its content, which may
    # be:

    #                   bool * int * float * long * bytes
    #              datetime * DateTime * tuple * list * object

    # If "object" is specified, it means that the tag contains sub-tags, each
    # one corresponding to the value of an attribute for this object. if "tuple"
    # is specified, it will be converted to a list. "long" is supported for
    # backward compatibility with Python 2.

    def __init__(self, classes={}, tagTypes={}, conversionFunctions={},
                 contentAttributes={}):
        Parser.__init__(self)
        # p_classes is a dict whose keys are tag names and values are Python
        # classes. During the unmarshalling process, when an object is
        # encountered within a given tag, if it corresponds to a key in this
        # dict, the marshaller will create a instance of this class. Else, an
        # instance of generic class appy.model.utils.Object will created
        # instead. Note that the constructor of classes specified in p_classes
        # will not be called: the marshaller will dynamically set the class to
        # the created instance.
        if not isinstance(classes, dict) and classes:
            # The user may only need to define a class for the root tag. The
            # default name for a root tag is "appyData". This is a naming
            # convention taken by the marshaller corresponding by this
            # unmarshaller, defined in appy/xml/marshaller.py.
            self.classes = {'appyData': classes}
        else:
            self.classes = classes

        # If the XML file to parse does not respect the conventions described
        # above, you can provide type information in p_tagTypes. Here is an
        # example of p_tagTypes:
        #
        #      {"information": "list", "days": "list", "person": "object"}
        #
        self.tagTypes = tagTypes

        # The parser assumes that data is represented in some standard way. If
        # it is not the case, you may provide, in this dict, custom functions
        # allowing to convert values of basic types (long, float, datetime...).
        # Every such function must take a single arg which is the value to
        # convert and return the converted value. Dict keys are strings
        # representing types ('bool', 'int', 'datetime', etc) and dict values
        # are conversion functions. Here is an example:
        #
        #        {'int': convertInteger, 'DateTime': convertDate}
        #
        # NOTE: you can even invent a new basic type, put it in self.tagTypes,
        # and create a specific conversionFunction for it. This way, you can
        # for example convert strings that have specific values (in this case,
        # knowing that the value is a "string" is not sufficient).
        self.conversionFunctions = conversionFunctions

        # If you have the special case of a tag whose type is "object" and that
        # has direct text content, you can specify, in attribute
        # "contentAttributes", the name of the attribute onto which this content
        # will be stored. For example, suppose you have:
        #
        #        <parent><child attr1="a1" attr2="a2">c1</child></parent>
        #
        # If you specify:
        #
        #                   tagTypes={'child': 'object'}
        #              contentAttributes={'child': 'content'}
        #
        # you will get, for "child", an object
        #
        #             O(attr1='a1', attr2='a2', content='c1')
        self.contentAttributes = contentAttributes

    def convertAttrs(self, attrs):
        '''Converts XML attrs to a dict'''
        r = {}
        for k, v in attrs.items():
            # Ignore structural attribute "type"
            if k == 'type': continue
            if ':' in k: # An attr prefixed with a namespace. Remove this.
                k = k.split(':')[-1]
            r[str(k)] = v
        return r

    def getDatetime(self, value):
        '''From this string p_value representing a date, produce an instance of
           datetime.datime.'''
        r = value.split()
        # First part should be the date part
        year, month, day = r[0].split('/')
        return datetime.datetime(int(year), int(month), int(day))

    def startDocument(self):
        # Standard parser attribute "r" will contain the resulting web of
        # unmarshalled Python objects.
        Parser.startDocument(self)
        # The name of the root tag
        self.rootTag = None
        # The stack of current "containers" where to store the next parsed
        # element. A container can be a list, dict or an object (the root object
        # of the whole web or a sub-object). Every entry in this stack is of the
        # form
        #                            (type, elem)
        #
        # If a list is pushed on this stack, the pushed element will be:
        #                      (<class 'list'> , [])
        # For a dict:          (<class 'dict'> , {})
        # For a tuple:         (<class 'tuple'>, ())
        # For an object,       (<class 'type'> , <some object>)
        self.env.containerStack = []
        # The name of the currently set object attribute, if the last
        # encountered container is an object.
        self.env.currentName = None
        # The name of the currently parsed basic type (string, float...)
        self.env.currentBasicType = None
        # The content of the currently walked tag
        self.env.currentContent = ''

    def addContainer(self, o, otype=None):
        '''Adds this container p_o(bject) to the current stack of containers'''
        otype = otype or type(o)
        self.env.containerStack.append((otype, o))

    def getLastContainer(self):
        '''Returns the last container as stored on the environment, or None if
           there is no such container.'''
        containers = self.env.containerStack
        return (None, None) if not containers else containers[-1]

    containerTags = ('tuple', 'list', 'dict', 'object', 'file')
    numericTypes  = ('bool', 'int', 'long', 'float')
    fileAttributes = {'name':None, 'mimeType':'type', 'location':None}

    def startElement(self, tag, attrs):
        # Remember the name of the previous element
        previousTag = None
        if self.env.currentTag:
            previousTag = self.env.currentTag.name
        else:
            # We are walking the root tag
            self.rootTag = tag
        e = Parser.startElement(self, tag, attrs)
        # Determine the type of the element (the default is "str")
        type = 'str'
        if 'type' in attrs:
            type = attrs['type']
        elif tag in self.tagTypes:
            type = self.tagTypes[tag]
        if type in self.containerTags:
            # I must create a new container object
            newType = None # For most types, it will be automatically deduced 
            if   type == 'object': new = O(**self.convertAttrs(attrs))
            elif type == 'tuple' :
                new = [] # Temporarily, it will be a list
                newType = tuple
            elif type == 'list'  : new = []
            elif type == 'dict'  : new = {}
            elif type == 'file':
                new = UnmarshalledFile()
                for dname, name in self.fileAttributes.items():
                    if dname in attrs:
                        name = name or dname
                        setattr(new, name, attrs[dname])
            else: new = O(**self.convertAttrs(attrs))
            # Store the value on the last container, or on the root object
            self.storeValue(tag, new)
            # Push the new object on the container stack
            self.addContainer(new, otype=newType)
        else:
            # If we are already parsing a basic type, it means that we were
            # wrong for our diagnostic of the containing element: it was not
            # basic. We will make the assumption that the containing element is
            # then an object.
            if e.currentBasicType:
                # Previous elem was an object: create it on the stack
                new = O()
                self.storeValue(previousTag, new)
                self.addContainer(new)
            e.currentBasicType = type

    def storeValue(self, name, value):
        '''Stores the newly parsed p_value (contained in tag p_name) on the
           current container in environment self.env.'''
        e = self.env
        # Remove namespace prefix when relevant
        if ':' in name: name = name.split(':')[-1]
        # Change the class of the value if relevant
        if name in self.classes and isinstance(value, O):
            value.__class__ = self.classes[name]
        # Where must I store this value?
        if not e.containerStack:
            # The object must be stored at the root of the web
            self.r = value
        else:
            ctype, container = e.containerStack[-1]
            if isinstance(container, list):
                container.append(value)
            elif isinstance(container, dict):
                # If the current container is a dict, it means that p_value is
                # a dict entry object named "entry" by convention and having
                # attributes "k" and "v" that store, respectively, the key and
                # the value of the entry. But this object is under construction:
                # at this time, attributes "k" and "v" are not created yet. We
                # will act in m_endElement, when the object will be finalized.
                pass
            elif isinstance(container, UnmarshalledFile):
                val = value or b''
                container.value += val
                container.size += len(val)
            else:
                # Current container is an object
                if name in container.__dict__:
                    # We have already encountered a sub-object with this name.
                    # Having several sub-objects with the same name, we will
                    # create a list.
                    val = getattr(container, name)
                    if val is None:
                        val = value
                    elif isinstance(val, list):
                        val.append(value)
                    else:
                        val = [val, value]
                else:
                    val = value
                setattr(container, name, val)
                e.currentName = name

    def characters(self, content):
        e = Parser.characters(self, content)
        if e.currentBasicType:
            if e.currentBasicType == 'base64':
                content = content.strip()
            e.currentContent += content
        elif e.currentTag.name in self.contentAttributes:
            # Store p_content in attribute named according to
            # p_self.contentAttributes on the current object.
            name = self.contentAttributes[e.currentTag.name]
            ctype, current = e.containerStack[-1]
            if hasattr(current, name):
                setattr(current, name, getattr(current, name) + content)
            else:
                setattr(current, name, content)

    def endElement(self, tag):
        e = Parser.endElement(self, tag)
        type = e.currentBasicType
        if type:
            value = e.currentContent.strip()
            if not value: value = None
            else:
                # If we have a custom converter for values of this type, use it
                if type in self.conversionFunctions:
                    try:
                        value = self.conversionFunctions[type](value)
                    except Exception as err:
                        raise Exception(CUSTOM_CONVERSION_ERROR % \
                                        (type, value, str(err)))
                # If not, try a standard conversion
                elif type in self.numericTypes:
                    # Manage obsolete type "long"
                    type = 'int' if type == 'long' else type
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError) as e:
                        raise Exception(CONVERSION_ERROR % (type, value))
                    # Convert ints to floats
                    if type == 'float' and isinstance(value, int):
                        value = float(value)
                    # Check that the value is of the correct type. For instance,
                    # a float value with a comma in it could have been converted
                    # to a tuple instead of a float.
                    if not isinstance(value, eval(type)):
                        raise Exception(CONVERSION_ERROR % (type, value))
                elif type == 'bytes':
                    # Convert the string value to bytes
                    value = value.encode()
                elif type == 'DateTime':
                    value = DateTime(value)
                elif type == 'datetime':
                    value = self.getDatetime(value)
                elif type == 'base64':
                    value = decodebytes(e.currentContent.encode())
            # Store the value on the last container
            self.storeValue(tag, value)
            # Clean the environment
            e.currentBasicType = None
            e.currentContent = ''
        else:
            otype, o = e.containerStack.pop()
            # Get the previous container
            ptype, previous = self.getLastContainer()
            # v_o may need to be converted to a tuple
            if otype == tuple:
                o = tuple(o)
                # Hook this tuple to its container
                if not previous:
                    self.r = o
                elif ptype == list:
                    previous[-1] = o
                else:
                    setattr(previous, e.currentName, o)
            # v_o can be a temporary "entry" object representing a dict entry
            if ptype == dict:
                previous[o.k] = o.v
    # Alias: "unmarshall" > "parse"
    unmarshall = Parser.parse
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
