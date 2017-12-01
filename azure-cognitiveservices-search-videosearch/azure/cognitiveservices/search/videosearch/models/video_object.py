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

from .media_object import MediaObject


class VideoObject(MediaObject):
    """Defines a video object that is relevant to the query.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param _type: Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar image:
    :vartype image:
     ~azure.cognitiveservices.search.videosearch.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name:
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider:
     list[~azure.cognitiveservices.search.videosearch.models.Thing]
    :ivar text:
    :vartype text: str
    :ivar content_url: Original URL to retrieve the source (file) for the
     media object (e.g the source URL for the image).
    :vartype content_url: str
    :ivar host_page_url: URL of the page that hosts the media object.
    :vartype host_page_url: str
    :ivar width: The width of the source media object, in pixels.
    :vartype width: int
    :ivar height: The height of the source media object, in pixels.
    :vartype height: int
    :ivar motion_thumbnail_url:
    :vartype motion_thumbnail_url: str
    :ivar motion_thumbnail_id:
    :vartype motion_thumbnail_id: str
    :ivar embed_html:
    :vartype embed_html: str
    :ivar allow_https_embed:
    :vartype allow_https_embed: bool
    :ivar view_count:
    :vartype view_count: int
    :ivar thumbnail:
    :vartype thumbnail:
     ~azure.cognitiveservices.search.videosearch.models.ImageObject
    :ivar video_id:
    :vartype video_id: str
    :ivar allow_mobile_embed:
    :vartype allow_mobile_embed: bool
    :ivar is_superfresh:
    :vartype is_superfresh: bool
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'text': {'readonly': True},
        'content_url': {'readonly': True},
        'host_page_url': {'readonly': True},
        'width': {'readonly': True},
        'height': {'readonly': True},
        'motion_thumbnail_url': {'readonly': True},
        'motion_thumbnail_id': {'readonly': True},
        'embed_html': {'readonly': True},
        'allow_https_embed': {'readonly': True},
        'view_count': {'readonly': True},
        'thumbnail': {'readonly': True},
        'video_id': {'readonly': True},
        'allow_mobile_embed': {'readonly': True},
        'is_superfresh': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'text': {'key': 'text', 'type': 'str'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
        'host_page_url': {'key': 'hostPageUrl', 'type': 'str'},
        'width': {'key': 'width', 'type': 'int'},
        'height': {'key': 'height', 'type': 'int'},
        'motion_thumbnail_url': {'key': 'motionThumbnailUrl', 'type': 'str'},
        'motion_thumbnail_id': {'key': 'motionThumbnailId', 'type': 'str'},
        'embed_html': {'key': 'embedHtml', 'type': 'str'},
        'allow_https_embed': {'key': 'allowHttpsEmbed', 'type': 'bool'},
        'view_count': {'key': 'viewCount', 'type': 'int'},
        'thumbnail': {'key': 'thumbnail', 'type': 'ImageObject'},
        'video_id': {'key': 'videoId', 'type': 'str'},
        'allow_mobile_embed': {'key': 'allowMobileEmbed', 'type': 'bool'},
        'is_superfresh': {'key': 'isSuperfresh', 'type': 'bool'},
    }

    def __init__(self):
        super(VideoObject, self).__init__()
        self.motion_thumbnail_url = None
        self.motion_thumbnail_id = None
        self.embed_html = None
        self.allow_https_embed = None
        self.view_count = None
        self.thumbnail = None
        self.video_id = None
        self.allow_mobile_embed = None
        self.is_superfresh = None
        self._type = 'VideoObject'