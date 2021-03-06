# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: acquisition_network_device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='acquisition_network_device.proto',
  package='ts_mon.proto',
  serialized_pb=_b('\n acquisition_network_device.proto\x12\x0cts_mon.proto\"\x95\x01\n\rNetworkDevice\x12\x11\n\talertable\x18\x65 \x01(\x08\x12\r\n\x05realm\x18\x66 \x01(\t\x12\r\n\x05metro\x18h \x01(\t\x12\x0c\n\x04role\x18i \x01(\t\x12\x10\n\x08hostname\x18j \x01(\t\x12\x11\n\thostgroup\x18l \x01(\t\" \n\x06TypeId\x12\x16\n\x0fMESSAGE_TYPE_ID\x10\xd5\x9d\x9e\x10')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_NETWORKDEVICE_TYPEID = _descriptor.EnumDescriptor(
  name='TypeId',
  full_name='ts_mon.proto.NetworkDevice.TypeId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_TYPE_ID', index=0, number=34049749,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=168,
  serialized_end=200,
)
_sym_db.RegisterEnumDescriptor(_NETWORKDEVICE_TYPEID)


_NETWORKDEVICE = _descriptor.Descriptor(
  name='NetworkDevice',
  full_name='ts_mon.proto.NetworkDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alertable', full_name='ts_mon.proto.NetworkDevice.alertable', index=0,
      number=101, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='realm', full_name='ts_mon.proto.NetworkDevice.realm', index=1,
      number=102, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metro', full_name='ts_mon.proto.NetworkDevice.metro', index=2,
      number=104, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='ts_mon.proto.NetworkDevice.role', index=3,
      number=105, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='ts_mon.proto.NetworkDevice.hostname', index=4,
      number=106, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hostgroup', full_name='ts_mon.proto.NetworkDevice.hostgroup', index=5,
      number=108, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKDEVICE_TYPEID,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=200,
)

_NETWORKDEVICE_TYPEID.containing_type = _NETWORKDEVICE
DESCRIPTOR.message_types_by_name['NetworkDevice'] = _NETWORKDEVICE

NetworkDevice = _reflection.GeneratedProtocolMessageType('NetworkDevice', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKDEVICE,
  __module__ = 'acquisition_network_device_pb2'
  # @@protoc_insertion_point(class_scope:ts_mon.proto.NetworkDevice)
  ))
_sym_db.RegisterMessage(NetworkDevice)


# @@protoc_insertion_point(module_scope)
