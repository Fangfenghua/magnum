#!/usr/bin/env python
"""
Copyright 2015 Reverb Technologies, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class V1beta3_Volume(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'emptyDir': 'v1beta3_EmptyDirVolumeSource',
            
            
            'gcePersistentDisk': 'v1beta3_GCEPersistentDiskVolumeSource',
            
            
            'gitRepo': 'v1beta3_GitRepoVolumeSource',
            
            
            'hostPath': 'v1beta3_HostPathVolumeSource',
            
            
            'iscsi': 'v1beta3_ISCSIVolumeSource',
            
            
            'name': 'str',
            
            
            'nfs': 'v1beta3_NFSVolumeSource',
            
            
            'secret': 'v1beta3_SecretVolumeSource'
            
        }

        self.attributeMap = {
            
            'emptyDir': 'emptyDir',
            
            'gcePersistentDisk': 'gcePersistentDisk',
            
            'gitRepo': 'gitRepo',
            
            'hostPath': 'hostPath',
            
            'iscsi': 'iscsi',
            
            'name': 'name',
            
            'nfs': 'nfs',
            
            'secret': 'secret'
            
        }       

        
        #temporary directory that shares a pod&#39;s lifetime
        
        self.emptyDir = None # v1beta3_EmptyDirVolumeSource
        
        #GCE disk resource attached to the host machine on demand
        
        self.gcePersistentDisk = None # v1beta3_GCEPersistentDiskVolumeSource
        
        #git repository at a particular revision
        
        self.gitRepo = None # v1beta3_GitRepoVolumeSource
        
        #pre-existing host file or directory; generally for privileged system daemons or other agents tied to the host
        
        self.hostPath = None # v1beta3_HostPathVolumeSource
        
        #iSCSI disk attached to host machine on demand
        
        self.iscsi = None # v1beta3_ISCSIVolumeSource
        
        #volume name; must be a DNS_LABEL and unique within the pod
        
        self.name = None # str
        
        #NFS volume that will be mounted in the host machine
        
        self.nfs = None # v1beta3_NFSVolumeSource
        
        #secret to populate volume
        
        self.secret = None # v1beta3_SecretVolumeSource
        
