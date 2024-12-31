# coding: utf-8

"""
    Vector Similarity Demo

    The test functionality and Query testing  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@hyper-space.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DeleteByQueryResponse(object):
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
        'took': 'int',
        'deleted': 'int'
    }

    attribute_map = {
        'took': 'took',
        'deleted': 'deleted'
    }

    def __init__(self, took=None, deleted=None):  # noqa: E501
        """DeleteByQueryResponse - a model defined in Swagger"""  # noqa: E501
        self._took = None
        self._deleted = None
        self.discriminator = None
        if took is not None:
            self.took = took
        if deleted is not None:
            self.deleted = deleted

    @property
    def took(self):
        """Gets the took of this DeleteByQueryResponse.  # noqa: E501

        The number of milliseconds from start to end of the whole operation.  # noqa: E501

        :return: The took of this DeleteByQueryResponse.  # noqa: E501
        :rtype: int
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this DeleteByQueryResponse.

        The number of milliseconds from start to end of the whole operation.  # noqa: E501

        :param took: The took of this DeleteByQueryResponse.  # noqa: E501
        :type: int
        """

        self._took = took

    @property
    def deleted(self):
        """Gets the deleted of this DeleteByQueryResponse.  # noqa: E501

        The number of documents that were successfully deleted.  # noqa: E501

        :return: The deleted of this DeleteByQueryResponse.  # noqa: E501
        :rtype: int
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DeleteByQueryResponse.

        The number of documents that were successfully deleted.  # noqa: E501

        :param deleted: The deleted of this DeleteByQueryResponse.  # noqa: E501
        :type: int
        """

        self._deleted = deleted

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
        if issubclass(DeleteByQueryResponse, dict):
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
        if not isinstance(other, DeleteByQueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
