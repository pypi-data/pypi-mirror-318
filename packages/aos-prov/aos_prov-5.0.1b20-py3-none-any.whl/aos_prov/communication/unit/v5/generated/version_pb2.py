# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iamanager/version.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17iamanager/version.proto\x12\tiamanager\x1a\x1bgoogle/protobuf/empty.proto\"\x1d\n\nAPIVersion\x12\x0f\n\x07version\x18\x01 \x01(\x04\x32U\n\x11IAMVersionService\x12@\n\rGetAPIVersion\x12\x16.google.protobuf.Empty\x1a\x15.iamanager.APIVersion\"\x00\x62\x06proto3')



_APIVERSION = DESCRIPTOR.message_types_by_name['APIVersion']
APIVersion = _reflection.GeneratedProtocolMessageType('APIVersion', (_message.Message,), {
  'DESCRIPTOR' : _APIVERSION,
  '__module__' : 'iamanager.version_pb2'
  # @@protoc_insertion_point(class_scope:iamanager.APIVersion)
  })
_sym_db.RegisterMessage(APIVersion)

_IAMVERSIONSERVICE = DESCRIPTOR.services_by_name['IAMVersionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _APIVERSION._serialized_start=67
  _APIVERSION._serialized_end=96
  _IAMVERSIONSERVICE._serialized_start=98
  _IAMVERSIONSERVICE._serialized_end=183
# @@protoc_insertion_point(module_scope)
