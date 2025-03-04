#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

Base = declarative_base()\
    if os.getenv('HBNB_TYPE_STORAGE') == 'db' else object


class BaseModel:

    id = Column(String(60), unique=True, nullable=False, primary_key=True)\
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ""
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())\
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())\
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None

    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')\
                if 'updated_at' in kwargs.keys() else datetime.now()
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')\
                if 'created_at' in kwargs.keys() else datetime.now()
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            for item in kwargs.items():
                setattr(self, item[0], item[1])

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in list(dictionary.keys()):
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """
        delete the current instance
        """
        from models import storage
        storage.delete(self)
