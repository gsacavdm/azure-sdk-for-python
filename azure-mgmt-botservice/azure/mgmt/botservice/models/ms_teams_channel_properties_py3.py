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


class MsTeamsChannelProperties(Model):
    """The parameters to provide for the Microsoft Teams channel.

    All required parameters must be populated in order to send to Azure.

    :param enable_messaging: Enable messaging for Microsoft Teams channel
    :type enable_messaging: bool
    :param enable_media_cards: Enable media cards for Microsoft Teams channel
    :type enable_media_cards: bool
    :param enable_video: Enable video for Microsoft Teams channel
    :type enable_video: bool
    :param enable_calling: Enable calling for Microsoft Teams channel
    :type enable_calling: bool
    :param call_mode: Enable messaging for Microsoft Teams channel
    :type call_mode: str
    :param is_enabled: Required. Whether this channel is enabled for the bot
    :type is_enabled: bool
    """

    _validation = {
        'is_enabled': {'required': True},
    }

    _attribute_map = {
        'enable_messaging': {'key': 'enableMessaging', 'type': 'bool'},
        'enable_media_cards': {'key': 'enableMediaCards', 'type': 'bool'},
        'enable_video': {'key': 'enableVideo', 'type': 'bool'},
        'enable_calling': {'key': 'enableCalling', 'type': 'bool'},
        'call_mode': {'key': 'callMode', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
    }

    def __init__(self, *, is_enabled: bool, enable_messaging: bool=None, enable_media_cards: bool=None, enable_video: bool=None, enable_calling: bool=None, call_mode: str=None, **kwargs) -> None:
        super(MsTeamsChannelProperties, self).__init__(**kwargs)
        self.enable_messaging = enable_messaging
        self.enable_media_cards = enable_media_cards
        self.enable_video = enable_video
        self.enable_calling = enable_calling
        self.call_mode = call_mode
        self.is_enabled = is_enabled