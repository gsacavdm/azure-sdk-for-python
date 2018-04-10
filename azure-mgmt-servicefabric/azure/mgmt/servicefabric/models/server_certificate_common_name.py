# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServerCertificateCommonName(Model):
    """Describes the server certificate details using common name.

    :param certificate_common_name: The common name of the server certificate.
    :type certificate_common_name: str
    :param certificate_issuer_thumbprint: The issuer thumbprint of the server
     certificate.
    :type certificate_issuer_thumbprint: str
    """

    _validation = {
        'certificate_common_name': {'required': True},
        'certificate_issuer_thumbprint': {'required': True},
    }

    _attribute_map = {
        'certificate_common_name': {'key': 'certificateCommonName', 'type': 'str'},
        'certificate_issuer_thumbprint': {'key': 'certificateIssuerThumbprint', 'type': 'str'},
    }

    def __init__(self, certificate_common_name, certificate_issuer_thumbprint):
        super(ServerCertificateCommonName, self).__init__()
        self.certificate_common_name = certificate_common_name
        self.certificate_issuer_thumbprint = certificate_issuer_thumbprint
