# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _AlibabaCloud


class _Storage(_AlibabaCloud):
    _type = "storage"
    _icon_dir = "resources/alibabacloud/storage"


class CloudStorageGateway(_Storage):
    _icon = "cloud-storage-gateway.png"


class FileStorageHdfs(_Storage):
    _icon = "file-storage-hdfs.png"


class FileStorageNas(_Storage):
    _icon = "file-storage-nas.png"


class HybridBackupRecovery(_Storage):
    _icon = "hybrid-backup-recovery.png"


class HybridCloudDisasterRecovery(_Storage):
    _icon = "hybrid-cloud-disaster-recovery.png"


class Imm(_Storage):
    _icon = "imm.png"


class ObjectStorageService(_Storage):
    _icon = "object-storage-service.png"


class ObjectTableStore(_Storage):
    _icon = "object-table-store.png"


# Aliases

HDFS = FileStorageHdfs
NAS = FileStorageNas
HBR = HybridBackupRecovery
HDR = HybridCloudDisasterRecovery
OSS = ObjectStorageService
OTS = ObjectTableStore
