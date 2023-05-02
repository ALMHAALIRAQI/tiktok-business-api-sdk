# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class OpenApiv13bcadvertisercreateBillingInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address': 'str',
        'tax_map': 'str'
    }

    attribute_map = {
        'address': 'address',
        'tax_map': 'tax_map'
    }

    def __init__(self, address=None, tax_map=None):  # noqa: E501
        """OpenApiv13bcadvertisercreateBillingInfo - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._tax_map = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if tax_map is not None:
            self.tax_map = tax_map

    @property
    def address(self):
        """Gets the address of this OpenApiv13bcadvertisercreateBillingInfo.  # noqa: E501

        Billing address, no more than 512 characters in length  # noqa: E501

        :return: The address of this OpenApiv13bcadvertisercreateBillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this OpenApiv13bcadvertisercreateBillingInfo.

        Billing address, no more than 512 characters in length  # noqa: E501

        :param address: The address of this OpenApiv13bcadvertisercreateBillingInfo.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def tax_map(self):
        """Gets the tax_map of this OpenApiv13bcadvertisercreateBillingInfo.  # noqa: E501

        Billing and invoicing tax number. Different countries use different tax number fields. The tax number field `vat` is used for European countries, for instance, France.The tax number field `tax_id` is used for Brazil (required), Mexico (required), United Arab Emirates, Egypt, Saudi Arabia, Israel, Turkey, Canada, and the United States.The tax number field `abn` is used for Australia and New Zealand.  # noqa: E501

        :return: The tax_map of this OpenApiv13bcadvertisercreateBillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._tax_map

    @tax_map.setter
    def tax_map(self, tax_map):
        """Sets the tax_map of this OpenApiv13bcadvertisercreateBillingInfo.

        Billing and invoicing tax number. Different countries use different tax number fields. The tax number field `vat` is used for European countries, for instance, France.The tax number field `tax_id` is used for Brazil (required), Mexico (required), United Arab Emirates, Egypt, Saudi Arabia, Israel, Turkey, Canada, and the United States.The tax number field `abn` is used for Australia and New Zealand.  # noqa: E501

        :param tax_map: The tax_map of this OpenApiv13bcadvertisercreateBillingInfo.  # noqa: E501
        :type: str
        """

        self._tax_map = tax_map

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(OpenApiv13bcadvertisercreateBillingInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OpenApiv13bcadvertisercreateBillingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other