# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cluster.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cluster.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcluster.proto\"\x1a\n\x07Workers\x12\x0f\n\x07workers\x18\x01 \x01(\x05\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x15\n\x04\x46ile\x12\r\n\x05\x66iles\x18\x01 \x01(\t\"\x1b\n\x05Words\x12\x12\n\ntotalWords\x18\x01 \x01(\x05\"&\n\tWordCount\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x0b\n\x03num\x18\x02 \x01(\x05\x32\xc3\x01\n\x06Worker\x12&\n\rCreateWorkers\x12\x08.Workers\x1a\t.Response\"\x00\x12&\n\rDeleteWorkers\x12\x08.Workers\x1a\t.Response\"\x00\x12\x1f\n\x04List\x12\x08.Workers\x1a\t.Response\"\x00\x30\x01\x12!\n\x0c\x43outingWords\x12\x05.File\x1a\x06.Words\"\x00(\x01\x12%\n\nWordCounts\x12\x05.File\x1a\n.WordCount\"\x00(\x01\x30\x01\x62\x06proto3'
)




_WORKERS = _descriptor.Descriptor(
  name='Workers',
  full_name='Workers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workers', full_name='Workers.workers', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=43,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Response.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=72,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='File.files', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=95,
)


_WORDS = _descriptor.Descriptor(
  name='Words',
  full_name='Words',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='totalWords', full_name='Words.totalWords', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=124,
)


_WORDCOUNT = _descriptor.Descriptor(
  name='WordCount',
  full_name='WordCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='WordCount.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num', full_name='WordCount.num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['Workers'] = _WORKERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Words'] = _WORDS
DESCRIPTOR.message_types_by_name['WordCount'] = _WORDCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Workers = _reflection.GeneratedProtocolMessageType('Workers', (_message.Message,), {
  'DESCRIPTOR' : _WORKERS,
  '__module__' : 'cluster_pb2'
  # @@protoc_insertion_point(class_scope:Workers)
  })
_sym_db.RegisterMessage(Workers)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'cluster_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'cluster_pb2'
  # @@protoc_insertion_point(class_scope:File)
  })
_sym_db.RegisterMessage(File)

Words = _reflection.GeneratedProtocolMessageType('Words', (_message.Message,), {
  'DESCRIPTOR' : _WORDS,
  '__module__' : 'cluster_pb2'
  # @@protoc_insertion_point(class_scope:Words)
  })
_sym_db.RegisterMessage(Words)

WordCount = _reflection.GeneratedProtocolMessageType('WordCount', (_message.Message,), {
  'DESCRIPTOR' : _WORDCOUNT,
  '__module__' : 'cluster_pb2'
  # @@protoc_insertion_point(class_scope:WordCount)
  })
_sym_db.RegisterMessage(WordCount)



_WORKER = _descriptor.ServiceDescriptor(
  name='Worker',
  full_name='Worker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=167,
  serialized_end=362,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateWorkers',
    full_name='Worker.CreateWorkers',
    index=0,
    containing_service=None,
    input_type=_WORKERS,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteWorkers',
    full_name='Worker.DeleteWorkers',
    index=1,
    containing_service=None,
    input_type=_WORKERS,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='Worker.List',
    index=2,
    containing_service=None,
    input_type=_WORKERS,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CoutingWords',
    full_name='Worker.CoutingWords',
    index=3,
    containing_service=None,
    input_type=_FILE,
    output_type=_WORDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WordCounts',
    full_name='Worker.WordCounts',
    index=4,
    containing_service=None,
    input_type=_FILE,
    output_type=_WORDCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKER)

DESCRIPTOR.services_by_name['Worker'] = _WORKER

# @@protoc_insertion_point(module_scope)
