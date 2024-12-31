# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/alert_manager/v1/notification_protocol.proto
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
from spaceone.api.core.v2 import plugin_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_plugin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9spaceone/api/alert_manager/v1/notification_protocol.proto\x12\x1dspaceone.api.alert_manager.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\x1a!spaceone/api/core/v2/plugin.proto\"\x92\x01\n!NotificationProtocolCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x0bplugin_info\x18\x02 \x01(\x0b\x32#.spaceone.api.core.v2.PluginRequest\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\"m\n!NotificationProtocolUpdateRequest\x12\x13\n\x0bprotocol_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\"\xc7\x02\n\'NotificationProtocolUpdatePluginRequest\x12\x13\n\x0bprotocol_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12(\n\x07options\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12|\n\x0cupgrade_mode\x18\x04 \x01(\x0e\x32\x66.spaceone.api.alert_manager.v1.NotificationProtocolUpdatePluginRequest.NotificationProtocolUpgradeMode\"N\n\x1fNotificationProtocolUpgradeMode\x12\x15\n\x11UPGRADE_MODE_NONE\x10\x00\x12\x08\n\x04\x41UTO\x10\x01\x12\n\n\x06MANUAL\x10\x02\"2\n\x1bNotificationProtocolRequest\x12\x13\n\x0bprotocol_id\x18\x01 \x01(\t\"p\n+NotificationProtocolUpdateSecretDataRequest\x12\x13\n\x0bprotocol_id\x18\x01 \x01(\t\x12,\n\x0bsecret_data\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xaa\x02\n\x1fNotificationProtocolSearchQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x13\n\x0bprotocol_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12g\n\x05state\x18\x04 \x01(\x0e\x32X.spaceone.api.alert_manager.v1.NotificationProtocolSearchQuery.NotificationProtocolState\"O\n\x19NotificationProtocolState\x12\x17\n\x13PROTOCOL_STATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"U\n\x1dNotificationProtocolStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery\"\xf5\x02\n\x18NotificationProtocolInfo\x12\x13\n\x0bprotocol_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12`\n\x05state\x18\x03 \x01(\x0e\x32Q.spaceone.api.alert_manager.v1.NotificationProtocolInfo.NotificationProtocolState\x12\x35\n\x0bplugin_info\x18\x04 \x01(\x0b\x32 .spaceone.api.core.v2.PluginInfo\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\"O\n\x19NotificationProtocolState\x12\x17\n\x13PROTOCOL_STATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"z\n\x19NotificationProtocolsInfo\x12H\n\x07results\x18\x01 \x03(\x0b\x32\x37.spaceone.api.alert_manager.v1.NotificationProtocolInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\xec\x0e\n\x14NotificationProtocol\x12\xbe\x01\n\x06\x63reate\x12@.spaceone.api.alert_manager.v1.NotificationProtocolCreateRequest\x1a\x37.spaceone.api.alert_manager.v1.NotificationProtocolInfo\"9\x82\xd3\xe4\x93\x02\x33\"./alert-manager/v1/notification-protocol/create:\x01*\x12\xbe\x01\n\x06update\x12@.spaceone.api.alert_manager.v1.NotificationProtocolUpdateRequest\x1a\x37.spaceone.api.alert_manager.v1.NotificationProtocolInfo\"9\x82\xd3\xe4\x93\x02\x33\"./alert-manager/v1/notification-protocol/update:\x01*\x12\xd2\x01\n\rupdate_plugin\x12\x46.spaceone.api.alert_manager.v1.NotificationProtocolUpdatePluginRequest\x1a\x37.spaceone.api.alert_manager.v1.NotificationProtocolInfo\"@\x82\xd3\xe4\x93\x02:\"5/alert-manager/v1/notification-protocol/update-plugin:\x01*\x12\xe0\x01\n\x12update_secret_data\x12J.spaceone.api.alert_manager.v1.NotificationProtocolUpdateSecretDataRequest\x1a\x37.spaceone.api.alert_manager.v1.NotificationProtocolInfo\"E\x82\xd3\xe4\x93\x02?\":/alert-manager/v1/notification-protocol/update-secret-data:\x01*\x12\xb8\x01\n\x06\x65nable\x12:.spaceone.api.alert_manager.v1.NotificationProtocolRequest\x1a\x37.spaceone.api.alert_manager.v1.NotificationProtocolInfo\"9\x82\xd3\xe4\x93\x02\x33\"./alert-manager/v1/notification-protocol/enable:\x01*\x12\xba\x01\n\x07\x64isable\x12:.spaceone.api.alert_manager.v1.NotificationProtocolRequest\x1a\x37.spaceone.api.alert_manager.v1.NotificationProtocolInfo\":\x82\xd3\xe4\x93\x02\x34\"//alert-manager/v1/notification-protocol/disable:\x01*\x12\x97\x01\n\x06\x64\x65lete\x12:.spaceone.api.alert_manager.v1.NotificationProtocolRequest\x1a\x16.google.protobuf.Empty\"9\x82\xd3\xe4\x93\x02\x33\"./alert-manager/v1/notification-protocol/delete:\x01*\x12\xb2\x01\n\x03get\x12:.spaceone.api.alert_manager.v1.NotificationProtocolRequest\x1a\x37.spaceone.api.alert_manager.v1.NotificationProtocolInfo\"6\x82\xd3\xe4\x93\x02\x30\"+/alert-manager/v1/notification-protocol/get:\x01*\x12\xb9\x01\n\x04list\x12>.spaceone.api.alert_manager.v1.NotificationProtocolSearchQuery\x1a\x38.spaceone.api.alert_manager.v1.NotificationProtocolsInfo\"7\x82\xd3\xe4\x93\x02\x31\",/alert-manager/v1/notification-protocol/list:\x01*\x12\x96\x01\n\x04stat\x12<.spaceone.api.alert_manager.v1.NotificationProtocolStatQuery\x1a\x17.google.protobuf.Struct\"7\x82\xd3\xe4\x93\x02\x31\",/alert-manager/v1/notification-protocol/stat:\x01*BDZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/alert-manager/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.alert_manager.v1.notification_protocol_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/alert-manager/v1'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['create']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['create']._serialized_options = b'\202\323\344\223\0023\"./alert-manager/v1/notification-protocol/create:\001*'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['update']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['update']._serialized_options = b'\202\323\344\223\0023\"./alert-manager/v1/notification-protocol/update:\001*'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['update_plugin']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['update_plugin']._serialized_options = b'\202\323\344\223\002:\"5/alert-manager/v1/notification-protocol/update-plugin:\001*'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['update_secret_data']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['update_secret_data']._serialized_options = b'\202\323\344\223\002?\":/alert-manager/v1/notification-protocol/update-secret-data:\001*'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['enable']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['enable']._serialized_options = b'\202\323\344\223\0023\"./alert-manager/v1/notification-protocol/enable:\001*'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['disable']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['disable']._serialized_options = b'\202\323\344\223\0024\"//alert-manager/v1/notification-protocol/disable:\001*'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['delete']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\0023\"./alert-manager/v1/notification-protocol/delete:\001*'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['get']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['get']._serialized_options = b'\202\323\344\223\0020\"+/alert-manager/v1/notification-protocol/get:\001*'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['list']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['list']._serialized_options = b'\202\323\344\223\0021\",/alert-manager/v1/notification-protocol/list:\001*'
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['stat']._loaded_options = None
  _globals['_NOTIFICATIONPROTOCOL'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\0021\",/alert-manager/v1/notification-protocol/stat:\001*'
  _globals['_NOTIFICATIONPROTOCOLCREATEREQUEST']._serialized_start=251
  _globals['_NOTIFICATIONPROTOCOLCREATEREQUEST']._serialized_end=397
  _globals['_NOTIFICATIONPROTOCOLUPDATEREQUEST']._serialized_start=399
  _globals['_NOTIFICATIONPROTOCOLUPDATEREQUEST']._serialized_end=508
  _globals['_NOTIFICATIONPROTOCOLUPDATEPLUGINREQUEST']._serialized_start=511
  _globals['_NOTIFICATIONPROTOCOLUPDATEPLUGINREQUEST']._serialized_end=838
  _globals['_NOTIFICATIONPROTOCOLUPDATEPLUGINREQUEST_NOTIFICATIONPROTOCOLUPGRADEMODE']._serialized_start=760
  _globals['_NOTIFICATIONPROTOCOLUPDATEPLUGINREQUEST_NOTIFICATIONPROTOCOLUPGRADEMODE']._serialized_end=838
  _globals['_NOTIFICATIONPROTOCOLREQUEST']._serialized_start=840
  _globals['_NOTIFICATIONPROTOCOLREQUEST']._serialized_end=890
  _globals['_NOTIFICATIONPROTOCOLUPDATESECRETDATAREQUEST']._serialized_start=892
  _globals['_NOTIFICATIONPROTOCOLUPDATESECRETDATAREQUEST']._serialized_end=1004
  _globals['_NOTIFICATIONPROTOCOLSEARCHQUERY']._serialized_start=1007
  _globals['_NOTIFICATIONPROTOCOLSEARCHQUERY']._serialized_end=1305
  _globals['_NOTIFICATIONPROTOCOLSEARCHQUERY_NOTIFICATIONPROTOCOLSTATE']._serialized_start=1226
  _globals['_NOTIFICATIONPROTOCOLSEARCHQUERY_NOTIFICATIONPROTOCOLSTATE']._serialized_end=1305
  _globals['_NOTIFICATIONPROTOCOLSTATQUERY']._serialized_start=1307
  _globals['_NOTIFICATIONPROTOCOLSTATQUERY']._serialized_end=1392
  _globals['_NOTIFICATIONPROTOCOLINFO']._serialized_start=1395
  _globals['_NOTIFICATIONPROTOCOLINFO']._serialized_end=1768
  _globals['_NOTIFICATIONPROTOCOLINFO_NOTIFICATIONPROTOCOLSTATE']._serialized_start=1226
  _globals['_NOTIFICATIONPROTOCOLINFO_NOTIFICATIONPROTOCOLSTATE']._serialized_end=1305
  _globals['_NOTIFICATIONPROTOCOLSINFO']._serialized_start=1770
  _globals['_NOTIFICATIONPROTOCOLSINFO']._serialized_end=1892
  _globals['_NOTIFICATIONPROTOCOL']._serialized_start=1895
  _globals['_NOTIFICATIONPROTOCOL']._serialized_end=3795
# @@protoc_insertion_point(module_scope)
