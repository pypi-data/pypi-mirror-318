import pytest
from src.tundra.Users_module import Users_Module
import logging


def test_user_add_users(user_object1):
    users = Users_Module()
    users.add_entities(user_object1)
    assert users.spesification == {
        "user1": {"can_login": "yes", "member_of": ["role1"]},
        "user2": {"can_login": "yes", "member_of": ["role2"]},
    }


def test_user_append_users(user_object1, user_object2, users_object):
    users = Users_Module()
    users.add_entities(user_object1)
    users.add_entities(user_object2)
    assert users.spesification == users_object.spesification


def test_users_get_user(users_object):
    assert users_object.get_entities("user1") == {
        "can_login": "yes",
        "member_of": ["role1"],
    }


def test_users_get_user_not_found(users_object, caplog):
    caplog.set_level(logging.WARNING)
    users_object.get_entities("user4")
    assert "User not found" in caplog.text


def test_users_is_user(users_object):
    assert users_object.is_entity("user1") == True


def test_users_is_user_not_found(users_object):
    assert users_object.is_entity("user4") == False


def test_users_describe(users_object):
    user_description = users_object.describe()
    assert user_description.count == 3
    assert set(user_description.entities) == set(["user1", "user2", "user3"])


def test_users_describe_empty():
    users = Users_Module()
    user_description = users.describe()
    assert user_description.count == 0
    assert user_description.entities == []


def test_users_get_dependencies(users_object):
    assert users_object.get_dependencies("member_of") == ["role1", "role2", "role3"]
