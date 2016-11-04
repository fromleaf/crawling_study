# -*- coding: utf-8 -*-

import datetime

from pymongo import MongoClient


def init(url, port):
    client = MongoClient(url, port)
    db = client.testDatabase

    return db


def create(data, db):
    db.testCollection.insert_one(data)


def read(db):
    return db.testCollection.find_one()


def update(data, db):
    db.testCollection.update_one(data, {'$set': {'d': datetime.datetime.now()}})
    return db.testCollection.find_one()


def delete(data, db):
    db.testCollection.delete_one(data)
    return db.testCollection.find_one()