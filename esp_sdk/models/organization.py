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


class Organization(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, created_at=None, name=None, require_mfa=None, updated_at=None, subscription=None, subscription_id=None, custom_signatures=None, custom_signature_ids=None, external_accounts=None, external_account_ids=None, sub_organizations=None, sub_organization_ids=None, teams=None, team_ids=None, users=None, user_ids=None, compliance_standards=None, compliance_standard_ids=None, integrations=None, integration_ids=None):
        """
        Organization - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'created_at': 'datetime',
            'name': 'str',
            'require_mfa': 'bool',
            'updated_at': 'datetime',
            'subscription': 'Subscription',
            'subscription_id': 'int',
            'custom_signatures': 'list[CustomSignature]',
            'custom_signature_ids': 'list[int]',
            'external_accounts': 'list[ExternalAccount]',
            'external_account_ids': 'list[int]',
            'sub_organizations': 'list[SubOrganization]',
            'sub_organization_ids': 'list[int]',
            'teams': 'list[Team]',
            'team_ids': 'list[int]',
            'users': 'list[User]',
            'user_ids': 'list[int]',
            'compliance_standards': 'list[ComplianceStandard]',
            'compliance_standard_ids': 'list[int]',
            'integrations': 'list[Integration]',
            'integration_ids': 'list[int]'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'name': 'name',
            'require_mfa': 'require_mfa',
            'updated_at': 'updated_at',
            'subscription': 'subscription',
            'subscription_id': 'subscription_id',
            'custom_signatures': 'custom_signatures',
            'custom_signature_ids': 'custom_signature_ids',
            'external_accounts': 'external_accounts',
            'external_account_ids': 'external_account_ids',
            'sub_organizations': 'sub_organizations',
            'sub_organization_ids': 'sub_organization_ids',
            'teams': 'teams',
            'team_ids': 'team_ids',
            'users': 'users',
            'user_ids': 'user_ids',
            'compliance_standards': 'compliance_standards',
            'compliance_standard_ids': 'compliance_standard_ids',
            'integrations': 'integrations',
            'integration_ids': 'integration_ids'
        }

        self._id = id
        self._created_at = created_at
        self._name = name
        self._require_mfa = require_mfa
        self._updated_at = updated_at
        self._subscription = subscription
        self._subscription_id = subscription_id
        self._custom_signatures = custom_signatures
        self._custom_signature_ids = custom_signature_ids
        self._external_accounts = external_accounts
        self._external_account_ids = external_account_ids
        self._sub_organizations = sub_organizations
        self._sub_organization_ids = sub_organization_ids
        self._teams = teams
        self._team_ids = team_ids
        self._users = users
        self._user_ids = user_ids
        self._compliance_standards = compliance_standards
        self._compliance_standard_ids = compliance_standard_ids
        self._integrations = integrations
        self._integration_ids = integration_ids

    @property
    def id(self):
        """
        Gets the id of this Organization.
        Unique ID

        :return: The id of this Organization.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Organization.
        Unique ID

        :param id: The id of this Organization.
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Organization.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this Organization.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Organization.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this Organization.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """
        Gets the name of this Organization.
        Name of the organization

        :return: The name of this Organization.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Organization.
        Name of the organization

        :param name: The name of this Organization.
        :type: str
        """

        self._name = name

    @property
    def require_mfa(self):
        """
        Gets the require_mfa of this Organization.
        Whether or not users for this organization are required to enable Multi Factor Authentication

        :return: The require_mfa of this Organization.
        :rtype: bool
        """
        return self._require_mfa

    @require_mfa.setter
    def require_mfa(self, require_mfa):
        """
        Sets the require_mfa of this Organization.
        Whether or not users for this organization are required to enable Multi Factor Authentication

        :param require_mfa: The require_mfa of this Organization.
        :type: bool
        """

        self._require_mfa = require_mfa

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Organization.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this Organization.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Organization.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this Organization.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def subscription(self):
        """
        Gets the subscription of this Organization.
        Associated Subscription

        :return: The subscription of this Organization.
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this Organization.
        Associated Subscription

        :param subscription: The subscription of this Organization.
        :type: Subscription
        """

        self._subscription = subscription

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this Organization.
        Associated Subscription ID

        :return: The subscription_id of this Organization.
        :rtype: int
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this Organization.
        Associated Subscription ID

        :param subscription_id: The subscription_id of this Organization.
        :type: int
        """

        self._subscription_id = subscription_id

    @property
    def custom_signatures(self):
        """
        Gets the custom_signatures of this Organization.
        Associated Custom Signatures

        :return: The custom_signatures of this Organization.
        :rtype: list[CustomSignature]
        """
        return self._custom_signatures

    @custom_signatures.setter
    def custom_signatures(self, custom_signatures):
        """
        Sets the custom_signatures of this Organization.
        Associated Custom Signatures

        :param custom_signatures: The custom_signatures of this Organization.
        :type: list[CustomSignature]
        """

        self._custom_signatures = custom_signatures

    @property
    def custom_signature_ids(self):
        """
        Gets the custom_signature_ids of this Organization.
        Associated Custom Signatures IDs

        :return: The custom_signature_ids of this Organization.
        :rtype: list[int]
        """
        return self._custom_signature_ids

    @custom_signature_ids.setter
    def custom_signature_ids(self, custom_signature_ids):
        """
        Sets the custom_signature_ids of this Organization.
        Associated Custom Signatures IDs

        :param custom_signature_ids: The custom_signature_ids of this Organization.
        :type: list[int]
        """

        self._custom_signature_ids = custom_signature_ids

    @property
    def external_accounts(self):
        """
        Gets the external_accounts of this Organization.
        Associated External Accounts

        :return: The external_accounts of this Organization.
        :rtype: list[ExternalAccount]
        """
        return self._external_accounts

    @external_accounts.setter
    def external_accounts(self, external_accounts):
        """
        Sets the external_accounts of this Organization.
        Associated External Accounts

        :param external_accounts: The external_accounts of this Organization.
        :type: list[ExternalAccount]
        """

        self._external_accounts = external_accounts

    @property
    def external_account_ids(self):
        """
        Gets the external_account_ids of this Organization.
        Associated External Accounts IDs

        :return: The external_account_ids of this Organization.
        :rtype: list[int]
        """
        return self._external_account_ids

    @external_account_ids.setter
    def external_account_ids(self, external_account_ids):
        """
        Sets the external_account_ids of this Organization.
        Associated External Accounts IDs

        :param external_account_ids: The external_account_ids of this Organization.
        :type: list[int]
        """

        self._external_account_ids = external_account_ids

    @property
    def sub_organizations(self):
        """
        Gets the sub_organizations of this Organization.
        Associated Sub Organizations

        :return: The sub_organizations of this Organization.
        :rtype: list[SubOrganization]
        """
        return self._sub_organizations

    @sub_organizations.setter
    def sub_organizations(self, sub_organizations):
        """
        Sets the sub_organizations of this Organization.
        Associated Sub Organizations

        :param sub_organizations: The sub_organizations of this Organization.
        :type: list[SubOrganization]
        """

        self._sub_organizations = sub_organizations

    @property
    def sub_organization_ids(self):
        """
        Gets the sub_organization_ids of this Organization.
        Associated Sub Organizations IDs

        :return: The sub_organization_ids of this Organization.
        :rtype: list[int]
        """
        return self._sub_organization_ids

    @sub_organization_ids.setter
    def sub_organization_ids(self, sub_organization_ids):
        """
        Sets the sub_organization_ids of this Organization.
        Associated Sub Organizations IDs

        :param sub_organization_ids: The sub_organization_ids of this Organization.
        :type: list[int]
        """

        self._sub_organization_ids = sub_organization_ids

    @property
    def teams(self):
        """
        Gets the teams of this Organization.
        Associated Teams

        :return: The teams of this Organization.
        :rtype: list[Team]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """
        Sets the teams of this Organization.
        Associated Teams

        :param teams: The teams of this Organization.
        :type: list[Team]
        """

        self._teams = teams

    @property
    def team_ids(self):
        """
        Gets the team_ids of this Organization.
        Associated Teams IDs

        :return: The team_ids of this Organization.
        :rtype: list[int]
        """
        return self._team_ids

    @team_ids.setter
    def team_ids(self, team_ids):
        """
        Sets the team_ids of this Organization.
        Associated Teams IDs

        :param team_ids: The team_ids of this Organization.
        :type: list[int]
        """

        self._team_ids = team_ids

    @property
    def users(self):
        """
        Gets the users of this Organization.
        Associated Users

        :return: The users of this Organization.
        :rtype: list[User]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this Organization.
        Associated Users

        :param users: The users of this Organization.
        :type: list[User]
        """

        self._users = users

    @property
    def user_ids(self):
        """
        Gets the user_ids of this Organization.
        Associated Users IDs

        :return: The user_ids of this Organization.
        :rtype: list[int]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """
        Sets the user_ids of this Organization.
        Associated Users IDs

        :param user_ids: The user_ids of this Organization.
        :type: list[int]
        """

        self._user_ids = user_ids

    @property
    def compliance_standards(self):
        """
        Gets the compliance_standards of this Organization.
        Associated Compliance Standards

        :return: The compliance_standards of this Organization.
        :rtype: list[ComplianceStandard]
        """
        return self._compliance_standards

    @compliance_standards.setter
    def compliance_standards(self, compliance_standards):
        """
        Sets the compliance_standards of this Organization.
        Associated Compliance Standards

        :param compliance_standards: The compliance_standards of this Organization.
        :type: list[ComplianceStandard]
        """

        self._compliance_standards = compliance_standards

    @property
    def compliance_standard_ids(self):
        """
        Gets the compliance_standard_ids of this Organization.
        Associated Compliance Standards IDs

        :return: The compliance_standard_ids of this Organization.
        :rtype: list[int]
        """
        return self._compliance_standard_ids

    @compliance_standard_ids.setter
    def compliance_standard_ids(self, compliance_standard_ids):
        """
        Sets the compliance_standard_ids of this Organization.
        Associated Compliance Standards IDs

        :param compliance_standard_ids: The compliance_standard_ids of this Organization.
        :type: list[int]
        """

        self._compliance_standard_ids = compliance_standard_ids

    @property
    def integrations(self):
        """
        Gets the integrations of this Organization.
        Associated Integrations

        :return: The integrations of this Organization.
        :rtype: list[Integration]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """
        Sets the integrations of this Organization.
        Associated Integrations

        :param integrations: The integrations of this Organization.
        :type: list[Integration]
        """

        self._integrations = integrations

    @property
    def integration_ids(self):
        """
        Gets the integration_ids of this Organization.
        Associated Integrations IDs

        :return: The integration_ids of this Organization.
        :rtype: list[int]
        """
        return self._integration_ids

    @integration_ids.setter
    def integration_ids(self, integration_ids):
        """
        Sets the integration_ids of this Organization.
        Associated Integrations IDs

        :param integration_ids: The integration_ids of this Organization.
        :type: list[int]
        """

        self._integration_ids = integration_ids

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
        if not isinstance(other, Organization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
