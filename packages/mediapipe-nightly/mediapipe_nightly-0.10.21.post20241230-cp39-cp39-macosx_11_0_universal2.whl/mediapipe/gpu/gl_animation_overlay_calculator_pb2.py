# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/gpu/gl_animation_overlay_calculator.proto
# Protobuf Python Version: 4.25.5
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3mediapipe/gpu/gl_animation_overlay_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xaa\x02\n#GlAnimationOverlayCalculatorOptions\x12\x1a\n\x0c\x61spect_ratio\x18\x01 \x01(\x02:\x04\x30.75\x12 \n\x14vertical_fov_degrees\x18\x02 \x01(\x02:\x02\x37\x30\x12\"\n\x15z_clipping_plane_near\x18\x03 \x01(\x02:\x03\x30.1\x12\"\n\x14z_clipping_plane_far\x18\x04 \x01(\x02:\x04\x31\x30\x30\x30\x12\x1f\n\x13\x61nimation_speed_fps\x18\x05 \x01(\x02:\x02\x32\x35\x32\\\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xfd\xc4\xaaS \x01(\x0b\x32..mediapipe.GlAnimationOverlayCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.gpu.gl_animation_overlay_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GLANIMATIONOVERLAYCALCULATOROPTIONS']._serialized_start=105
  _globals['_GLANIMATIONOVERLAYCALCULATOROPTIONS']._serialized_end=403
# @@protoc_insertion_point(module_scope)
