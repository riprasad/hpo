# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hpo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\thpo.proto\x12\nhelloworld\"\'\n\x16NumberExperimentsReply\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"+\n\x13NewExperimentsReply\x12\x14\n\x0ctrial_number\x18\x01 \x01(\x05\"*\n\x14\x45xperimentsListReply\x12\x12\n\nexperiment\x18\x01 \x03(\t\"\x19\n\x17NumberExperimentsParams\"\x17\n\x15\x45xperimentsListParams\"\x16\n\x14\x45xperimentTrialReply\"/\n\x14\x45xperimentNameParams\x12\x17\n\x0f\x65xperiment_name\x18\x01 \x01(\t\"9\n\x0f\x45xperimentTrial\x12\x17\n\x0f\x65xperiment_name\x18\x01 \x01(\t\x12\r\n\x05trial\x18\x02 \x01(\x05\"\xbe\x01\n\x15\x45xperimentTrialResult\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\x12\r\n\x05trial\x18\x02 \x01(\x05\x12\x38\n\x06result\x18\x03 \x01(\x0e\x32(.helloworld.ExperimentTrialResult.Result\x12\x12\n\nvalue_type\x18\x04 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\x01\"\"\n\x06Result\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\"\x85\x03\n\x11\x45xperimentDetails\x12\x17\n\x0f\x65xperiment_name\x18\x01 \x01(\t\x12\x14\n\x0ctotal_trials\x18\x02 \x01(\x05\x12\x17\n\x0fparallel_trials\x18\x03 \x01(\x05\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x15\n\rhpo_algo_impl\x18\x05 \x01(\t\x12\x0b\n\x03id_\x18\x06 \x01(\t\x12\x1a\n\x12objective_function\x18\x07 \x01(\t\x12\x38\n\ttuneables\x18\x08 \x03(\x0b\x32%.helloworld.ExperimentDetails.Tunable\x12\x12\n\nvalue_type\x18\t \x01(\t\x12\x11\n\tslo_class\x18\n \x01(\t\x12\x0f\n\x07started\x18\x0b \x01(\x08\x1a\x63\n\x07Tunable\x12\x12\n\nvalue_type\x18\x01 \x01(\t\x12\x13\n\x0blower_bound\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0bupper_bound\x18\x04 \x01(\x05\x12\x0c\n\x04step\x18\x05 \x01(\x01\",\n\rTunableConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"8\n\x0bTrialConfig\x12)\n\x06\x63onfig\x18\x01 \x03(\x0b\x32\x19.helloworld.TunableConfig2\xf5\x04\n\nHpoService\x12^\n\x11NumberExperiments\x12#.helloworld.NumberExperimentsParams\x1a\".helloworld.NumberExperimentsReply\"\x00\x12X\n\x0f\x45xperimentsList\x12!.helloworld.ExperimentsListParams\x1a .helloworld.ExperimentsListReply\"\x00\x12Q\n\rNewExperiment\x12\x1d.helloworld.ExperimentDetails\x1a\x1f.helloworld.NewExperimentsReply\"\x00\x12Y\n\x14GetExperimentDetails\x12 .helloworld.ExperimentNameParams\x1a\x1d.helloworld.ExperimentDetails\"\x00\x12H\n\x0eGetTrialConfig\x12\x1b.helloworld.ExperimentTrial\x1a\x17.helloworld.TrialConfig\"\x00\x12Z\n\x11UpdateTrialResult\x12!.helloworld.ExperimentTrialResult\x1a .helloworld.ExperimentTrialReply\"\x00\x12Y\n\x12GenerateNextConfig\x12 .helloworld.ExperimentNameParams\x1a\x1f.helloworld.NewExperimentsReply\"\x00\x42#\n\rio.kruize.hpoB\nHpoServiceP\x01\xa2\x02\x03HLWb\x06proto3')



_NUMBEREXPERIMENTSREPLY = DESCRIPTOR.message_types_by_name['NumberExperimentsReply']
_NEWEXPERIMENTSREPLY = DESCRIPTOR.message_types_by_name['NewExperimentsReply']
_EXPERIMENTSLISTREPLY = DESCRIPTOR.message_types_by_name['ExperimentsListReply']
_NUMBEREXPERIMENTSPARAMS = DESCRIPTOR.message_types_by_name['NumberExperimentsParams']
_EXPERIMENTSLISTPARAMS = DESCRIPTOR.message_types_by_name['ExperimentsListParams']
_EXPERIMENTTRIALREPLY = DESCRIPTOR.message_types_by_name['ExperimentTrialReply']
_EXPERIMENTNAMEPARAMS = DESCRIPTOR.message_types_by_name['ExperimentNameParams']
_EXPERIMENTTRIAL = DESCRIPTOR.message_types_by_name['ExperimentTrial']
_EXPERIMENTTRIALRESULT = DESCRIPTOR.message_types_by_name['ExperimentTrialResult']
_EXPERIMENTDETAILS = DESCRIPTOR.message_types_by_name['ExperimentDetails']
_EXPERIMENTDETAILS_TUNABLE = _EXPERIMENTDETAILS.nested_types_by_name['Tunable']
_TUNABLECONFIG = DESCRIPTOR.message_types_by_name['TunableConfig']
_TRIALCONFIG = DESCRIPTOR.message_types_by_name['TrialConfig']
_EXPERIMENTTRIALRESULT_RESULT = _EXPERIMENTTRIALRESULT.enum_types_by_name['Result']
NumberExperimentsReply = _reflection.GeneratedProtocolMessageType('NumberExperimentsReply', (_message.Message,), {
  'DESCRIPTOR' : _NUMBEREXPERIMENTSREPLY,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.NumberExperimentsReply)
  })
_sym_db.RegisterMessage(NumberExperimentsReply)

NewExperimentsReply = _reflection.GeneratedProtocolMessageType('NewExperimentsReply', (_message.Message,), {
  'DESCRIPTOR' : _NEWEXPERIMENTSREPLY,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.NewExperimentsReply)
  })
_sym_db.RegisterMessage(NewExperimentsReply)

ExperimentsListReply = _reflection.GeneratedProtocolMessageType('ExperimentsListReply', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTSLISTREPLY,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ExperimentsListReply)
  })
_sym_db.RegisterMessage(ExperimentsListReply)

NumberExperimentsParams = _reflection.GeneratedProtocolMessageType('NumberExperimentsParams', (_message.Message,), {
  'DESCRIPTOR' : _NUMBEREXPERIMENTSPARAMS,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.NumberExperimentsParams)
  })
_sym_db.RegisterMessage(NumberExperimentsParams)

ExperimentsListParams = _reflection.GeneratedProtocolMessageType('ExperimentsListParams', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTSLISTPARAMS,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ExperimentsListParams)
  })
_sym_db.RegisterMessage(ExperimentsListParams)

ExperimentTrialReply = _reflection.GeneratedProtocolMessageType('ExperimentTrialReply', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTTRIALREPLY,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ExperimentTrialReply)
  })
_sym_db.RegisterMessage(ExperimentTrialReply)

ExperimentNameParams = _reflection.GeneratedProtocolMessageType('ExperimentNameParams', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTNAMEPARAMS,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ExperimentNameParams)
  })
_sym_db.RegisterMessage(ExperimentNameParams)

ExperimentTrial = _reflection.GeneratedProtocolMessageType('ExperimentTrial', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTTRIAL,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ExperimentTrial)
  })
_sym_db.RegisterMessage(ExperimentTrial)

ExperimentTrialResult = _reflection.GeneratedProtocolMessageType('ExperimentTrialResult', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTTRIALRESULT,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ExperimentTrialResult)
  })
_sym_db.RegisterMessage(ExperimentTrialResult)

ExperimentDetails = _reflection.GeneratedProtocolMessageType('ExperimentDetails', (_message.Message,), {

  'Tunable' : _reflection.GeneratedProtocolMessageType('Tunable', (_message.Message,), {
    'DESCRIPTOR' : _EXPERIMENTDETAILS_TUNABLE,
    '__module__' : 'hpo_pb2'
    # @@protoc_insertion_point(class_scope:helloworld.ExperimentDetails.Tunable)
    })
  ,
  'DESCRIPTOR' : _EXPERIMENTDETAILS,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ExperimentDetails)
  })
_sym_db.RegisterMessage(ExperimentDetails)
_sym_db.RegisterMessage(ExperimentDetails.Tunable)

TunableConfig = _reflection.GeneratedProtocolMessageType('TunableConfig', (_message.Message,), {
  'DESCRIPTOR' : _TUNABLECONFIG,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.TunableConfig)
  })
_sym_db.RegisterMessage(TunableConfig)

TrialConfig = _reflection.GeneratedProtocolMessageType('TrialConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRIALCONFIG,
  '__module__' : 'hpo_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.TrialConfig)
  })
_sym_db.RegisterMessage(TrialConfig)

_HPOSERVICE = DESCRIPTOR.services_by_name['HpoService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rio.kruize.hpoB\nHpoServiceP\001\242\002\003HLW'
  _NUMBEREXPERIMENTSREPLY._serialized_start=25
  _NUMBEREXPERIMENTSREPLY._serialized_end=64
  _NEWEXPERIMENTSREPLY._serialized_start=66
  _NEWEXPERIMENTSREPLY._serialized_end=109
  _EXPERIMENTSLISTREPLY._serialized_start=111
  _EXPERIMENTSLISTREPLY._serialized_end=153
  _NUMBEREXPERIMENTSPARAMS._serialized_start=155
  _NUMBEREXPERIMENTSPARAMS._serialized_end=180
  _EXPERIMENTSLISTPARAMS._serialized_start=182
  _EXPERIMENTSLISTPARAMS._serialized_end=205
  _EXPERIMENTTRIALREPLY._serialized_start=207
  _EXPERIMENTTRIALREPLY._serialized_end=229
  _EXPERIMENTNAMEPARAMS._serialized_start=231
  _EXPERIMENTNAMEPARAMS._serialized_end=278
  _EXPERIMENTTRIAL._serialized_start=280
  _EXPERIMENTTRIAL._serialized_end=337
  _EXPERIMENTTRIALRESULT._serialized_start=340
  _EXPERIMENTTRIALRESULT._serialized_end=530
  _EXPERIMENTTRIALRESULT_RESULT._serialized_start=496
  _EXPERIMENTTRIALRESULT_RESULT._serialized_end=530
  _EXPERIMENTDETAILS._serialized_start=533
  _EXPERIMENTDETAILS._serialized_end=922
  _EXPERIMENTDETAILS_TUNABLE._serialized_start=823
  _EXPERIMENTDETAILS_TUNABLE._serialized_end=922
  _TUNABLECONFIG._serialized_start=924
  _TUNABLECONFIG._serialized_end=968
  _TRIALCONFIG._serialized_start=970
  _TRIALCONFIG._serialized_end=1026
  _HPOSERVICE._serialized_start=1029
  _HPOSERVICE._serialized_end=1658
# @@protoc_insertion_point(module_scope)
