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
# ------------------------------------------------------------------------------

'''Integration with RestrictedPython'''

# This module defines a specific evaluator you can pass to the Renderer, if you
# want all Python expressions evaluated by POD to pass through the
# RestrictedPython filter.

# ------------------------------------------------------------------------------
RP_N_INS  = 'Please install RestrictedPython before using this.'

# ------------------------------------------------------------------------------
try:
    import RestrictedPython as rp
    installed = True
except ImportError:
    installed = False

# ------------------------------------------------------------------------------
class Evaluator:
    '''RestrictedPython-specific evaluator'''

    # Mapping between keys to add in the context that will be used as globals
    # for RestrictedPython evaluations, and Evaluator attributes.

    contextMap = {'__builtins__': 'builtins', '_write_': 'write',
                  '_getitem_': 'item', '_unpack_sequence_': 'unpack', 
                  '_iter_unpack_sequence_': 'iterUnpack',
                  '_print_': 'safePrint'}

    def __init__(self, builtins=None, write=None, item=None, unpack=None,
                 iterUnpack=None, attr=None, custom=None):
        # Raise an error if RestrictedPython is not installed
        if not installed:
            raise Exception(RP_N_INS)
        # The replacement for Python __builtins__
        self.builtins = builtins or rp.Guards.safe_builtins
        # Prevent write access to objet attributes
        self.write = write or rp.Guards.full_write_guard
        # For "for" statements and comprehensions
        self.item = item or rp.Eval.default_guarded_getitem
        try:
            self.unpack = unpack or rp.Guards.guarded_unpack_sequence
        except AttributeError:
            self.unpack = unpack # Default may not be available
        try:
            self.iterUnpack = iterUnpack or \
                              rp.Guards.guarded_iter_unpack_sequence
        except AttributeError:
            self.iterUnpack = None
        # Prevent using stdout for printing
        self.safePrint = rp.PrintCollector
        # Protected "getattr". Any other attribute than p_attr will be
        # initialised once, globally, via m_updateContext, before any expression
        # is evaluated. p_attr, on the contrary, will be injected in the
        # context, in p_run, every time an expression is evaluated.
        self.attr = attr
        # If p_custom is None, p_self's attributes as defined hereabove will be
        # injected (by m_updateContext) in the evaluation context of any
        # evaluated expression, at standard RestrictedPython keys as defined in
        # the v_contextMap. Alternately, if you want to have full control over
        # the RestrictedPython-specific entries you want to inject in the
        # context of any evaluated expression, define them in a p_custom dict.
        # In this latter case, p_self's attributes will be ignored: entries from
        # the p_custom dict will be used instead. This option is useful if the
        # framework you use in conjunction with pod already defines a function
        # that computes such entries.
        self.custom = custom

    def updateContext(self, context):
        '''Adds, to p_context, the necessary keys for RestrictedPython, as
           configured on p_self.'''
        if self.custom is not None:
            # Use a custom dict
            context.update(self.custom)
        else:
            # Use p_self's attributes
            for key, name in Evaluator.contextMap.iteritems():
                val = getattr(self, name)
                if val:
                    context[key] = val

    def run(self, expr, context):
        '''Evaluates this p_expr(ession) in this p_context'''
        # m_updateContext has already been applied to this p_context. p_context
        # is ready, excepted if p_self.attr must be injected in it.
        if self.attr:
            context['_getattr_'] = self.attr
        return eval(rp.compile_restricted(expr, '<string>', 'eval'), context)
# ------------------------------------------------------------------------------
