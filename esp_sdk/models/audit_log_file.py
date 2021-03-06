# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class AuditLogFile(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, file_name=None, format=None, created_at=None, updated_at=None, url=None, organization=None, organization_id=None, user=None, user_id=None):
        """
        AuditLogFile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'file_name': 'str',
            'format': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'url': 'str',
            'organization': 'Organization',
            'organization_id': 'int',
            'user': 'User',
            'user_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'file_name': 'file_name',
            'format': 'format',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'url': 'url',
            'organization': 'organization',
            'organization_id': 'organization_id',
            'user': 'user',
            'user_id': 'user_id'
        }

        self._id = id
        self._file_name = file_name
        self._format = format
        self._created_at = created_at
        self._updated_at = updated_at
        self._url = url
        self._organization = organization
        self._organization_id = organization_id
        self._user = user
        self._user_id = user_id

    @property
    def id(self):
        """
        Gets the id of this AuditLogFile.
        Unique ID

        :return: The id of this AuditLogFile.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuditLogFile.
        Unique ID

        :param id: The id of this AuditLogFile.
        :type: int
        """

        self._id = id

    @property
    def file_name(self):
        """
        Gets the file_name of this AuditLogFile.
        File Name

        :return: The file_name of this AuditLogFile.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this AuditLogFile.
        File Name

        :param file_name: The file_name of this AuditLogFile.
        :type: str
        """

        self._file_name = file_name

    @property
    def format(self):
        """
        Gets the format of this AuditLogFile.
        Format of the file

        :return: The format of this AuditLogFile.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this AuditLogFile.
        Format of the file

        :param format: The format of this AuditLogFile.
        :type: str
        """

        self._format = format

    @property
    def created_at(self):
        """
        Gets the created_at of this AuditLogFile.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this AuditLogFile.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this AuditLogFile.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this AuditLogFile.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this AuditLogFile.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this AuditLogFile.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this AuditLogFile.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this AuditLogFile.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """
        Gets the url of this AuditLogFile.
        The expiring URL to download this file from

        :return: The url of this AuditLogFile.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this AuditLogFile.
        The expiring URL to download this file from

        :param url: The url of this AuditLogFile.
        :type: str
        """

        self._url = url

    @property
    def organization(self):
        """
        Gets the organization of this AuditLogFile.
        Associated Organization

        :return: The organization of this AuditLogFile.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this AuditLogFile.
        Associated Organization

        :param organization: The organization of this AuditLogFile.
        :type: Organization
        """

        self._organization = organization

    @property
    def organization_id(self):
        """
        Gets the organization_id of this AuditLogFile.
        Associated Organization ID

        :return: The organization_id of this AuditLogFile.
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this AuditLogFile.
        Associated Organization ID

        :param organization_id: The organization_id of this AuditLogFile.
        :type: int
        """

        self._organization_id = organization_id

    @property
    def user(self):
        """
        Gets the user of this AuditLogFile.
        Associated User

        :return: The user of this AuditLogFile.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this AuditLogFile.
        Associated User

        :param user: The user of this AuditLogFile.
        :type: User
        """

        self._user = user

    @property
    def user_id(self):
        """
        Gets the user_id of this AuditLogFile.
        Associated User ID

        :return: The user_id of this AuditLogFile.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AuditLogFile.
        Associated User ID

        :param user_id: The user_id of this AuditLogFile.
        :type: int
        """

        self._user_id = user_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AuditLogFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
