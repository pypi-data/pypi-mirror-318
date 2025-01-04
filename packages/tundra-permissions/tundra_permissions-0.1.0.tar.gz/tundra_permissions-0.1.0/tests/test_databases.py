from src.tundra.Databases_module import Databases_Module
import pytest
import logging


def test_database_module_add_entities(databases_object1):
    databases = Databases_Module()
    databases.add_entities(databases_object1)
    assert databases.spesification == {
        "database1": {"shared": "yes", "owner": "loader_qlik"},
        "database2": {"shared": "no", "owner": "loader_qlik"},
    }


def test_database_module_add_entities_multiple(
    databases_object1, databases_object2, databases_object
):
    databases = Databases_Module()
    databases.add_entities(databases_object1)
    databases.add_entities(databases_object2)
    assert databases.spesification == databases_object.spesification


def test_database_module_get_database(databases_object):
    assert databases_object.get_entities("database1") == {
        "shared": "yes",
        "owner": "loader_qlik",
    }
    assert databases_object.get_entities("database2") == {
        "shared": "no",
        "owner": "loader_qlik",
    }


def test_database_module_get_database_not_found(databases_object, caplog):
    caplog.set_level(logging.WARNING)
    databases_object.get_entities("database4")
    assert "Database not found" in caplog.text


def test_database_is_database(databases_object):
    assert databases_object.is_entity("database1") == True


def test_database_is_database_not_found(databases_object):
    assert databases_object.is_entity("database4") == False


def test_database_describe(databases_object):
    databases_description = databases_object.describe()
    assert databases_description.count == 3
    assert databases_description.entities == ["database1", "database2", "database3"]


def test_database_describe_empty():
    databases = Databases_Module()
    databases_description = databases.describe()
    assert databases_description.count == 0
    assert databases_description.entities == []


def test_database_get_dependencies(databases_object):
    assert databases_object.get_dependencies("owner") == ["loader_qlik"]
