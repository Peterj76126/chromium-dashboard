# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model_ import Model
from chromestatus_openapi import util


class ComponentSubscribersPossibleSubscribersInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, email=None):  # noqa: E501
        """ComponentSubscribersPossibleSubscribersInner - a model defined in OpenAPI

        :param id: The id of this ComponentSubscribersPossibleSubscribersInner.  # noqa: E501
        :type id: int
        :param name: The name of this ComponentSubscribersPossibleSubscribersInner.  # noqa: E501
        :type name: str
        :param email: The email of this ComponentSubscribersPossibleSubscribersInner.  # noqa: E501
        :type email: str
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'email': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'email': 'email'
        }

        self._id = id
        self._name = name
        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'ComponentSubscribersPossibleSubscribersInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ComponentSubscribers_possible_subscribers_inner of this ComponentSubscribersPossibleSubscribersInner.  # noqa: E501
        :rtype: ComponentSubscribersPossibleSubscribersInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ComponentSubscribersPossibleSubscribersInner.


        :return: The id of this ComponentSubscribersPossibleSubscribersInner.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentSubscribersPossibleSubscribersInner.


        :param id: The id of this ComponentSubscribersPossibleSubscribersInner.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ComponentSubscribersPossibleSubscribersInner.


        :return: The name of this ComponentSubscribersPossibleSubscribersInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentSubscribersPossibleSubscribersInner.


        :param name: The name of this ComponentSubscribersPossibleSubscribersInner.
        :type name: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this ComponentSubscribersPossibleSubscribersInner.


        :return: The email of this ComponentSubscribersPossibleSubscribersInner.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ComponentSubscribersPossibleSubscribersInner.


        :param email: The email of this ComponentSubscribersPossibleSubscribersInner.
        :type email: str
        """

        self._email = email