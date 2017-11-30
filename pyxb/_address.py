# ./_address.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7f85d8ac51794a92230f8d329a8485ecb3bed77a
# Generated 2017-11-23 21:29:53.460397 by PyXB version 1.2.6-DEV using Python 3.6.3.final.0
# Namespace URN:address [xmlns:address]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:3e3fb354-d039-11e7-8f32-185e0fec9474')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6-DEV'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('URN:address', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {URN:address}USState
class USState (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'USState')
    _XSDLocation = pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 39, 2)
    _Documentation = None
USState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=USState, enum_prefix=None)
USState.AK = USState._CF_enumeration.addEnumeration(unicode_value='AK', tag='AK')
USState.AL = USState._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
USState.AR = USState._CF_enumeration.addEnumeration(unicode_value='AR', tag='AR')
USState.AZ = USState._CF_enumeration.addEnumeration(unicode_value='AZ', tag='AZ')
USState._InitializeFacetMap(USState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'USState', USState)
_module_typeBindings.USState = USState

# Atomic simple type: {URN:address}UKPostcode
class UKPostcode (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UKPostcode')
    _XSDLocation = pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 51, 2)
    _Documentation = None
UKPostcode._CF_pattern = pyxb.binding.facets.CF_pattern()
UKPostcode._CF_pattern.addPattern(pattern='[A-Z]{2}\\d\\s\\d[A-Z]{2}')
UKPostcode._InitializeFacetMap(UKPostcode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'UKPostcode', UKPostcode)
_module_typeBindings.UKPostcode = UKPostcode

# Complex type {URN:address}Address with content type ELEMENT_ONLY
class Address (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {URN:address}Address with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Address')
    _XSDLocation = pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:address}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__URNaddress_Address_URNaddressname', False, pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 8, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {URN:address}street uses Python identifier street
    __street = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'street'), 'street', '__URNaddress_Address_URNaddressstreet', False, pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 9, 6), )

    
    street = property(__street.value, __street.set, None, None)

    
    # Element {URN:address}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__URNaddress_Address_URNaddresscity', False, pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 10, 6), )

    
    city = property(__city.value, __city.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __street.name() : __street,
        __city.name() : __city
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Address = Address
Namespace.addCategoryObject('typeBinding', 'Address', Address)


# Complex type {URN:address}USAddress with content type ELEMENT_ONLY
class USAddress (Address):
    """Complex type {URN:address}USAddress with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'USAddress')
    _XSDLocation = pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 14, 2)
    _ElementMap = Address._ElementMap.copy()
    _AttributeMap = Address._AttributeMap.copy()
    # Base type is Address
    
    # Element name ({URN:address}name) inherited from {URN:address}Address
    
    # Element street ({URN:address}street) inherited from {URN:address}Address
    
    # Element city ({URN:address}city) inherited from {URN:address}Address
    
    # Element {URN:address}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'state'), 'state', '__URNaddress_USAddress_URNaddressstate', False, pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 18, 10), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {URN:address}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zip'), 'zip', '__URNaddress_USAddress_URNaddresszip', False, pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 19, 10), )

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Attribute country uses Python identifier country
    __country = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'country'), 'country', '__URNaddress_USAddress_country', pyxb.binding.datatypes.NMTOKEN, fixed=True, unicode_default='US')
    __country._DeclarationLocation = pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 21, 8)
    __country._UseLocation = pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 21, 8)
    
    country = property(__country.value, __country.set, None, None)

    _ElementMap.update({
        __state.name() : __state,
        __zip.name() : __zip
    })
    _AttributeMap.update({
        __country.name() : __country
    })
_module_typeBindings.USAddress = USAddress
Namespace.addCategoryObject('typeBinding', 'USAddress', USAddress)


# Complex type {URN:address}UKAddress with content type ELEMENT_ONLY
class UKAddress (Address):
    """Complex type {URN:address}UKAddress with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UKAddress')
    _XSDLocation = pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 26, 2)
    _ElementMap = Address._ElementMap.copy()
    _AttributeMap = Address._AttributeMap.copy()
    # Base type is Address
    
    # Element name ({URN:address}name) inherited from {URN:address}Address
    
    # Element street ({URN:address}street) inherited from {URN:address}Address
    
    # Element city ({URN:address}city) inherited from {URN:address}Address
    
    # Element {URN:address}postcode uses Python identifier postcode
    __postcode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postcode'), 'postcode', '__URNaddress_UKAddress_URNaddresspostcode', False, pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 30, 10), )

    
    postcode = property(__postcode.value, __postcode.set, None, None)

    _ElementMap.update({
        __postcode.name() : __postcode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UKAddress = UKAddress
Namespace.addCategoryObject('typeBinding', 'UKAddress', UKAddress)




Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=Address, location=pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 8, 6)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'street'), pyxb.binding.datatypes.string, scope=Address, location=pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 9, 6)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string, scope=Address, location=pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 10, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 8, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'street')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 9, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 10, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Address._Automaton = _BuildAutomaton()




USAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'state'), USState, scope=USAddress, location=pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 18, 10)))

USAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zip'), pyxb.binding.datatypes.positiveInteger, scope=USAddress, location=pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 19, 10)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 8, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'street')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 9, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 10, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(USAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'state')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 18, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(USAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zip')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 19, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
USAddress._Automaton = _BuildAutomaton_()




UKAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postcode'), UKPostcode, scope=UKAddress, location=pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 30, 10)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UKAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 8, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UKAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'street')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 9, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UKAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 10, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UKAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postcode')), pyxb.utils.utility.Location('/home/james/code/learn_py/pyxb/nsaddress.xsd', 30, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UKAddress._Automaton = _BuildAutomaton_2()

