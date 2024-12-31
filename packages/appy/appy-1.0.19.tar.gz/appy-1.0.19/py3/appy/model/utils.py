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
import importlib.util, sys

from appy.utils import formatNumber

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def importModule(name, fileName):
    '''Imports module p_name given its absolute file p_name'''
    spec = importlib.util.spec_from_file_location(name, fileName)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Object:
    '''At every place we need an object, but without any requirement on its
       class (methods, attributes,...) we will use this minimalist class.'''

    # Warning - This class is particular: attribute access has been modified in
    #           such a way that AttributeError is never raised.
    #
    # Example:                 o = Object(a=1)
    #
    # >>> o.a
    # >>> 1
    # >>> o.b
    # >>>                      (None is returned)
    # >>> hasattr(o, 'a')
    # >>> True
    # >>> hasattr(o, 'b')
    # >>> True                 It's like if any attribute was defined on it
    # >>> 'a' in o
    # >>> True
    # >>> 'b' in o
    # >>> False

    # While this behaviour may be questionable and dangerous, it can be very
    # practical for objects that can potentially contain any attribute (like an
    # object representing HTTP request parameters or form values). Code getting
    # attribute values can be shorter, freed from verbose "hasattr" calls.
    # Conclusion: use this class at your own risk, if you know what you are
    # doing (isn't it the Python spirit?)

    def __init__(self, **fields):
        for k, v in fields.items(): setattr(self, k, v)

    def __repr__(self):
        '''A compact, string representation of this object for debugging
           purposes.'''
        r = '‹O '
        for name, value in self.__dict__.items():
            # Avoid infinite recursion if p_self it auto-referenced
            if value == self: continue
            v = value
            if hasattr(v, '__repr__'):
                try:
                    v = v.__repr__()
                except TypeError:
                    pass
            try:
                r = f'{r}{name}={v} '
            except UnicodeDecodeError:
                r = f'{r}{name}=--encoding problem-- '
        return f'{r.strip()}›'

    def __bool__(self): return bool(self.__dict__)
    def d(self): return self.__dict__
    def get(self, name, default=None): return self.__dict__.get(name, default)
    def __contains__(self, k): return k in self.__dict__
    def keys(self): return self.__dict__.keys()
    def values(self): return self.__dict__.values()
    def items(self): return self.__dict__.items()

    def __setitem__(self, k, v):
        '''Dict-like attribute set'''
        self.__dict__[k] = v

    def __getitem__(self, k):
        '''Dict-like access self[k] must return None if key p_k doesn't exist'''
        return self.__dict__.get(k)

    def __delitem__(self, k):
        '''Dict-like attribute removal'''
        del(self.__dict__[k])

    def __getattr__(self, name):
        '''Object access o.<name> must return None if attribute p_name does not
           exist.'''
        return

    def __eq__(self, other):
        '''Equality between Object instances is, like standard Python dicts,
           based on equality of all their attributes and values.'''
        if isinstance(other, Object):
            return self.__dict__ == other.__dict__
        return False

    def update(self, other):
        '''Set information from p_other (another Object instance or a dict) into
           p_self.'''
        other = other.__dict__ if isinstance(other, Object) else other
        for k, v in other.items(): setattr(self, k, v)

    def clone(self, **kwargs):
        '''Creates a clone from p_self'''
        r = self.__class__() # p_self's class may be an Object sub-class
        r.update(self)
        # Cloning can be altered by specifying values in p_kwargs, that will
        # override those from p_self.
        for k, v in kwargs.items():
            r[k] = v
        return r

    def asTable(self, _, prefix='', suffix='', css='small', precision=2,
                order=None, language=None):
        '''Build a HTML table from p_self, having this p_css class'''
        # There will be one row per attribute set on p_self. For each row:
        # - the 1st column will be represented by a "th" tag and will contain a
        #   translated text corresponding to the attribute name. This text will
        #   be built using the translation function passed in the first arg, and
        #   the i18n label built like this:
        #
        #                 <p_prefix><attribute_name><p_suffix>
        #
        # - the 2nd column will be represented by a "td" tag and will contain
        #   the attribute value. If the value is a float, it will be rounded
        #   with this p_precision (same arg as function "formatNumber" from
        #   package appy.utils).
        #
        # If p_order is passed, it must be a list containing the names of
        # p_self's attributes, in the order you want them to be dumped in the
        # table. Every attribute that would not be in this list will be moved at
        # the end of the table.
        rows = []
        # Manage p_order
        if order is not None:
            items = [(k, v) for k, v in self.items()]
            items.sort(key=lambda e: order.index(e[0]) \
                                     if e[0] in order else sys.maxsize)
        else:
            items = self.items()
        # Dump one row for each attribute in p_self
        for name, value in items:
            text = _(f'{prefix}{name}{suffix}', language=language)
            if isinstance(value, float):
                val = formatNumber(value, precision=precision)
            elif not isinstance(value, str):
                val = str(value)
            else:
                val = value
            rows.append(f'<tr><th>{text}</th><td align="right">{val}</td></tr>')
        return f'<table class="{css}">{"".join(rows)}</table>'

    # Allow this highly manipulated Object class to be picklable
    def __getstate__(self): return self.__dict__
    def __setstate__(self, state): self.__dict__.update(state)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Fake:
    '''An instance of this Fake class may be used, in some contexts, in place of
       a standard instance from an Appy class, in order to render a field value
       in a specific context where the standard instance is unusable as-is.'''

    # For example, a fake object is useful in order to manipulate a value being
    # stored in an object's history, because this value is not directly related
    # to the object itself anymore, as are the current values of its fields.

    def __init__(self, field, value, req):
        # The field whose value must be manipulated
        self.field = field
        # The value for this field will be stored in a dict named "values", in
        # order to mimic a standard Appy instance.
        self.values = {field.name: value}
        # Other useful standard attributes
        self.req = req
        self.id = 0
        self.iid  = 0

    def getField(self, name):
        '''If p_self.field is an outer field, method m_getField may be called to
           retrieve this outer field when rendering an inner field.'''
        return self.field

    def getShownValue(self):
        '''Fake variant for Base::getShownValue'''
        # We don't have enough information for producing this
        return 'Fake'

    def translate(self, label, field=None):
        '''Fake variant for Base::translate'''
        return self.field.name

    def allows(self, perm): return True

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Hack:
    '''This class proposes methods for patching some existing code with
       alternative methods.'''

    H_PATCHED = '%d method(s) patched from %s to %s: %s.'
    H_ADDED   = '%d method(s) and/or attribute(s) added from %s to %s: %s.'

    @staticmethod
    def patch(class_, method, replacement, isStatic):
        '''This method replaces, on p_class_, this m_method with a p_replacement
           method (being static if p_isStatic is True), but keeps p_method on
           p_class_ under name "_base_<initial_method_name>_".'''
        # In the patched method, one may use method Hack.base to call the base
        # method.
        name = method.__name__
        baseName = '_base_%s_' % name
        if isStatic:
            # If "staticmethod" isn't called hereafter, the static functions
            # will be wrapped in methods.
            method = staticmethod(method)
            replacement = staticmethod(replacement)
        setattr(class_, baseName, method)
        setattr(class_, name, replacement)

    @staticmethod
    def base(method, class_=None):
        '''Allows to call the base (replaced) method. If p_method is static,
           you must specify its p_class_.'''
        class_ = class_ or method.__self__.__class__
        return getattr(class_, '_base_%s_' % method.__name__)

    @staticmethod
    def inject(patchClass, class_, verbose=False):
        '''Injects any method or attribute from p_patchClass into p_class_'''
        # As a preamble, inject methods and attributes from p_patchClass's base
        # classes, if any.
        for base in patchClass.__bases__:
            if base == object: continue
            Hack.inject(base, class_, verbose=verbose)
        patched = []
        added = []  
        # Inject p_patchClass' own methods and attributes
        for name, attr in patchClass.__dict__.items():
            # Ignore special methods
            if name.startswith('__'): continue
            # Unwrap functions from static methods
            typeName = attr.__class__.__name__
            if typeName == 'staticmethod':
                attr = attr.__get__(attr)
                static = True
            else:
                static = False
            # Is this name already defined on p_class_ ?
            if hasattr(class_, name):
                hasAttr = True
                classAttr = getattr(class_, name)
            else:
                hasAttr = False
                classAttr = None
            if hasAttr and typeName != 'type' and callable(attr) and \
               callable(classAttr):
                # Patch this method via Hack.patch
                Hack.patch(class_, classAttr, attr, static)
                patched.append(name)
            else:
                # Simply replace the static attr or add the new static
                # attribute or method.
                setattr(class_, name, attr)
                added.append(name)
        if verbose:
            pName = patchClass.__name__
            cName = class_.__name__
            print(Hack.H_PATCHED % (len(patched), pName, cName,
                                    ', '.join(patched)))
            print(Hack.H_ADDED % (len(added), pName, cName, ', '.join(added)))

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Cloner:
    '''Creates Field objects as clones of Base Field objects'''

    # By default, appy.model.base.Base fields are inherited by any other Appy
    # class (Tool, Translation, etc) as well as any Appy class from any app.
    # This may pose problems. Firstly, the container class as mentioned in such
    # commmon Field objects will be wrong. Functionalities based on it, like
    # recomputing an index from the Admin Zone > Model page will produce wrong
    # results. Moreover, m_update methods from app classes may update Field
    # objects: the develper may no realize that his changes will be propagated
    # to all classes.

    # Consequently, when generating the model for an app, Base fields must be
    # cloned in every class.

    @classmethod
    def clone(class_, field, clonePage=True):
        '''Create and return a clone for this Base p_field'''
        # The Field and sub-classes' constructors have all different attributes;
        # moreover, some of them process these attributes in some way. In order
        # to avoid running these constructors, the approach implemented here for
        # cloning a field is mechanical:
        # (1) an instance class Object is created ;
        # (2) this instance's __class__ is replaced with the class from the
        #     field to clone ;
        # (3) This instance's __dict__ is popuplated based on the field to
        #     clone's __dict__ attribute.
        r = Object()
        r.__class__ = field.__class__
        r.__dict__.update(field.__dict__)
        # Clone the page as well (when a page is defined)
        if clonePage and field.page:
            r.page = field.page.clone()
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def notFromPortlet(tool):
    '''When set in a root class' attribute "createVia", this function prevents
       instances being created from the portlet.'''

    # This is practical if you want to get the facilities provided by the
    # "portlet zone" for a class (ie, all search facilities) but without
    # allowing people people to create such classes at the root level.
    try:
        return 'form' if not tool.traversal.context.rootClasses else None
    except AttributeError:
        pass
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
