#!/usr/bin/env python3
"""Lists all documents in python"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection:
    :return:
    """
    return mongo_collection.find()
