# @! create test cases using pytest for included code include=./src/langgraph_store_dynamodb/dynamodbStore.py , this will use actual dynamodb instance

import pytest
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from langgraph_store_dynamodb import DynamoDBStore

@pytest.fixture(scope='module')
def dynamodb_store():
    # Setup DynamoDBStore with a test table
    store = DynamoDBStore(table_name='test_table')
    yield store
    # Teardown logic if needed


def test_put_and_get_item(dynamodb_store):
    namespace = ('test',)
    key = 'item1'
    value = {'data': 'value1'}
    dynamodb_store.put(namespace, key, value)
    item = dynamodb_store.get(namespace, key)
    assert item is not None
    assert item.value == value


def test_delete_item(dynamodb_store):
    namespace = ('test',)
    key = 'item2'
    value = {'data': 'value2'}
    dynamodb_store.put(namespace, key, value)
    dynamodb_store.delete(namespace, key)
    item = dynamodb_store.get(namespace, key)
    assert item is None


def test_search_items(dynamodb_store):
    namespace = ('test',)
    key1 = 'item3'
    key2 = 'item4'
    value = {'data': 'value3'}
    dynamodb_store.put(namespace, key1, value)
    dynamodb_store.put(namespace, key2, value)
    items = dynamodb_store.search(namespace)
    assert len(items) >= 2
