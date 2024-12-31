# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory/v1/metric.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v2 import query_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&spaceone/api/inventory/v1/metric.proto\x12\x19spaceone.api.inventory.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"\xd4\x03\n\x13\x43reateMetricRequest\x12\x11\n\tmetric_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12:\n\x0bmetric_type\x18\x03 \x01(\x0e\x32%.spaceone.api.inventory.v1.MetricType\x12\x15\n\rresource_type\x18\x04 \x01(\t\x12\x39\n\rquery_options\x18\x05 \x01(\x0b\x32\".spaceone.api.core.v2.AnalyzeQuery\x12\x12\n\ndate_field\x18\x06 \x01(\t\x12\x0c\n\x04unit\x18\x07 \x01(\t\x12%\n\x04tags\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x14\n\x0cnamespace_id\x18\t \x01(\t\x12T\n\x0eresource_group\x18\x14 \x01(\x0e\x32<.spaceone.api.inventory.v1.CreateMetricRequest.ResourceGroup\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\"C\n\rResourceGroup\x12\x17\n\x13RESOURCE_GROUP_NONE\x10\x00\x12\n\n\x06\x44OMAIN\x10\x01\x12\r\n\tWORKSPACE\x10\x02\"\xba\x01\n\x13UpdateMetricRequest\x12\x11\n\tmetric_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x39\n\rquery_options\x18\x03 \x01(\x0b\x32\".spaceone.api.core.v2.AnalyzeQuery\x12\x12\n\ndate_field\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\x12%\n\x04tags\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\"\"\n\rMetricRequest\x12\x11\n\tmetric_id\x18\x01 \x01(\t\"a\n\x11MetricTestRequest\x12\x11\n\tmetric_id\x18\x01 \x01(\t\x12\x39\n\rquery_options\x18\x02 \x01(\x0b\x32\".spaceone.api.core.v2.AnalyzeQuery\"\xdf\x01\n\x0bMetricQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x11\n\tmetric_id\x18\x02 \x01(\t\x12:\n\x0bmetric_type\x18\x03 \x01(\x0e\x32%.spaceone.api.inventory.v1.MetricType\x12\x15\n\rresource_type\x18\x04 \x01(\t\x12\x12\n\nis_managed\x18\x05 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x14\n\x0cnamespace_id\x18\x16 \x01(\t\"\xbf\x04\n\nMetricInfo\x12\x11\n\tmetric_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12:\n\x0bmetric_type\x18\x03 \x01(\x0e\x32%.spaceone.api.inventory.v1.MetricType\x12\x15\n\rresource_type\x18\x04 \x01(\t\x12\x39\n\rquery_options\x18\x05 \x01(\x0b\x32\".spaceone.api.core.v2.AnalyzeQuery\x12\x12\n\ndate_field\x18\x06 \x01(\t\x12\x0c\n\x04unit\x18\x07 \x01(\t\x12%\n\x04tags\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0blabels_info\x18\t \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nis_managed\x18\n \x01(\x08\x12K\n\x0eresource_group\x18\x14 \x01(\x0e\x32\x33.spaceone.api.inventory.v1.MetricInfo.ResourceGroup\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x14\n\x0cnamespace_id\x18\x17 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\x12\x12\n\nupdated_at\x18  \x01(\t\"C\n\rResourceGroup\x12\x17\n\x13RESOURCE_GROUP_NONE\x10\x00\x12\n\n\x06\x44OMAIN\x10\x01\x12\r\n\tWORKSPACE\x10\x02\"Z\n\x0bMetricsInfo\x12\x36\n\x07results\x18\x01 \x03(\x0b\x32%.spaceone.api.inventory.v1.MetricInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"G\n\x0fMetricStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery*:\n\nMetricType\x12\x14\n\x10METRIC_TYPE_NONE\x10\x00\x12\x0b\n\x07\x43OUNTER\x10\x01\x12\t\n\x05GAUGE\x10\x02\x32\xe1\x07\n\x06Metric\x12\x87\x01\n\x06\x63reate\x12..spaceone.api.inventory.v1.CreateMetricRequest\x1a%.spaceone.api.inventory.v1.MetricInfo\"&\x82\xd3\xe4\x93\x02 \"\x1b/inventory/v1/metric/create:\x01*\x12\x87\x01\n\x06update\x12..spaceone.api.inventory.v1.UpdateMetricRequest\x1a%.spaceone.api.inventory.v1.MetricInfo\"&\x82\xd3\xe4\x93\x02 \"\x1b/inventory/v1/metric/update:\x01*\x12r\n\x06\x64\x65lete\x12(.spaceone.api.inventory.v1.MetricRequest\x1a\x16.google.protobuf.Empty\"&\x82\xd3\xe4\x93\x02 \"\x1b/inventory/v1/metric/delete:\x01*\x12l\n\x03run\x12(.spaceone.api.inventory.v1.MetricRequest\x1a\x16.google.protobuf.Empty\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/inventory/v1/metric/run:\x01*\x12s\n\x04test\x12,.spaceone.api.inventory.v1.MetricTestRequest\x1a\x17.google.protobuf.Struct\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/inventory/v1/metric/test:\x01*\x12{\n\x03get\x12(.spaceone.api.inventory.v1.MetricRequest\x1a%.spaceone.api.inventory.v1.MetricInfo\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/inventory/v1/metric/get:\x01*\x12|\n\x04list\x12&.spaceone.api.inventory.v1.MetricQuery\x1a&.spaceone.api.inventory.v1.MetricsInfo\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/inventory/v1/metric/list:\x01*\x12q\n\x04stat\x12*.spaceone.api.inventory.v1.MetricStatQuery\x1a\x17.google.protobuf.Struct\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/inventory/v1/metric/stat:\x01*B@Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.inventory.v1.metric_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1'
  _globals['_METRIC'].methods_by_name['create']._loaded_options = None
  _globals['_METRIC'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002 \"\033/inventory/v1/metric/create:\001*'
  _globals['_METRIC'].methods_by_name['update']._loaded_options = None
  _globals['_METRIC'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002 \"\033/inventory/v1/metric/update:\001*'
  _globals['_METRIC'].methods_by_name['delete']._loaded_options = None
  _globals['_METRIC'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002 \"\033/inventory/v1/metric/delete:\001*'
  _globals['_METRIC'].methods_by_name['run']._loaded_options = None
  _globals['_METRIC'].methods_by_name['run']._serialized_options = b'\202\323\344\223\002\035\"\030/inventory/v1/metric/run:\001*'
  _globals['_METRIC'].methods_by_name['test']._loaded_options = None
  _globals['_METRIC'].methods_by_name['test']._serialized_options = b'\202\323\344\223\002\036\"\031/inventory/v1/metric/test:\001*'
  _globals['_METRIC'].methods_by_name['get']._loaded_options = None
  _globals['_METRIC'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002\035\"\030/inventory/v1/metric/get:\001*'
  _globals['_METRIC'].methods_by_name['list']._loaded_options = None
  _globals['_METRIC'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002\036\"\031/inventory/v1/metric/list:\001*'
  _globals['_METRIC'].methods_by_name['stat']._loaded_options = None
  _globals['_METRIC'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\036\"\031/inventory/v1/metric/stat:\001*'
  _globals['_METRICTYPE']._serialized_start=1956
  _globals['_METRICTYPE']._serialized_end=2014
  _globals['_CREATEMETRICREQUEST']._serialized_start=193
  _globals['_CREATEMETRICREQUEST']._serialized_end=661
  _globals['_CREATEMETRICREQUEST_RESOURCEGROUP']._serialized_start=594
  _globals['_CREATEMETRICREQUEST_RESOURCEGROUP']._serialized_end=661
  _globals['_UPDATEMETRICREQUEST']._serialized_start=664
  _globals['_UPDATEMETRICREQUEST']._serialized_end=850
  _globals['_METRICREQUEST']._serialized_start=852
  _globals['_METRICREQUEST']._serialized_end=886
  _globals['_METRICTESTREQUEST']._serialized_start=888
  _globals['_METRICTESTREQUEST']._serialized_end=985
  _globals['_METRICQUERY']._serialized_start=988
  _globals['_METRICQUERY']._serialized_end=1211
  _globals['_METRICINFO']._serialized_start=1214
  _globals['_METRICINFO']._serialized_end=1789
  _globals['_METRICINFO_RESOURCEGROUP']._serialized_start=594
  _globals['_METRICINFO_RESOURCEGROUP']._serialized_end=661
  _globals['_METRICSINFO']._serialized_start=1791
  _globals['_METRICSINFO']._serialized_end=1881
  _globals['_METRICSTATQUERY']._serialized_start=1883
  _globals['_METRICSTATQUERY']._serialized_end=1954
  _globals['_METRIC']._serialized_start=2017
  _globals['_METRIC']._serialized_end=3010
# @@protoc_insertion_point(module_scope)
