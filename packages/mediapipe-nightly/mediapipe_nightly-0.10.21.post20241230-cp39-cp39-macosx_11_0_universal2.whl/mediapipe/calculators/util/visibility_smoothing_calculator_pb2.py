# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/visibility_smoothing_calculator.proto
# Protobuf Python Version: 4.25.5
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@mediapipe/calculators/util/visibility_smoothing_calculator.proto\x12\tmediapipe\x1a,mediapipe/framework/calculator_options.proto\"\xf2\x02\n$VisibilitySmoothingCalculatorOptions\x12M\n\tno_filter\x18\x01 \x01(\x0b\x32\x38.mediapipe.VisibilitySmoothingCalculatorOptions.NoFilterH\x00\x12X\n\x0flow_pass_filter\x18\x02 \x01(\x0b\x32=.mediapipe.VisibilitySmoothingCalculatorOptions.LowPassFilterH\x00\x1a\n\n\x08NoFilter\x1a#\n\rLowPassFilter\x12\x12\n\x05\x61lpha\x18\x01 \x01(\x02:\x03\x30.12^\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf6\xa7\xe1\xab\x01 \x01(\x0b\x32/.mediapipe.VisibilitySmoothingCalculatorOptionsB\x10\n\x0e\x66ilter_options')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.util.visibility_smoothing_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VISIBILITYSMOOTHINGCALCULATOROPTIONS']._serialized_start=126
  _globals['_VISIBILITYSMOOTHINGCALCULATOROPTIONS']._serialized_end=496
  _globals['_VISIBILITYSMOOTHINGCALCULATOROPTIONS_NOFILTER']._serialized_start=335
  _globals['_VISIBILITYSMOOTHINGCALCULATOROPTIONS_NOFILTER']._serialized_end=345
  _globals['_VISIBILITYSMOOTHINGCALCULATOROPTIONS_LOWPASSFILTER']._serialized_start=347
  _globals['_VISIBILITYSMOOTHINGCALCULATOROPTIONS_LOWPASSFILTER']._serialized_end=382
# @@protoc_insertion_point(module_scope)
