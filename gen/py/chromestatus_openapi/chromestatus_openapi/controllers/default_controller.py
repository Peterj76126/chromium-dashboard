import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from chromestatus_openapi.models.component_users_request import ComponentUsersRequest  # noqa: E501
from chromestatus_openapi.models.components_users_response import ComponentsUsersResponse  # noqa: E501
from chromestatus_openapi.models.review_latency import ReviewLatency  # noqa: E501
from chromestatus_openapi.models.spec_mentor import SpecMentor  # noqa: E501
from chromestatus_openapi import util


def add_user_to_component(component_id, user_id, component_users_request=None):  # noqa: E501
    """Add a user to a component

     # noqa: E501

    :param component_id: Component ID
    :type component_id: int
    :param user_id: User ID
    :type user_id: int
    :param component_users_request: 
    :type component_users_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        component_users_request = ComponentUsersRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def list_component_users():  # noqa: E501
    """List all components and possible users

     # noqa: E501


    :rtype: Union[ComponentsUsersResponse, Tuple[ComponentsUsersResponse, int], Tuple[ComponentsUsersResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_reviews_with_latency():  # noqa: E501
    """List recently reviewed features and their review latency

     # noqa: E501


    :rtype: Union[List[ReviewLatency], Tuple[List[ReviewLatency], int], Tuple[List[ReviewLatency], int, Dict[str, str]]
    """
    return 'do some magic!'


def list_spec_mentors(after=None):  # noqa: E501
    """List spec mentors and their activity

     # noqa: E501

    :param after: 
    :type after: str

    :rtype: Union[List[SpecMentor], Tuple[List[SpecMentor], int], Tuple[List[SpecMentor], int, Dict[str, str]]
    """
    after = util.deserialize_date(after)
    return 'do some magic!'


def remove_user_from_component(component_id, user_id, component_users_request=None):  # noqa: E501
    """Remove a user from a component

     # noqa: E501

    :param component_id: Component ID
    :type component_id: int
    :param user_id: User ID
    :type user_id: int
    :param component_users_request: 
    :type component_users_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        component_users_request = ComponentUsersRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
