#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
"""
base_model
has class BaseModel defining all
common atributes and methods for other classes
"""
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
import uuid
from os import getenv
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"
if getenv("HBNB_TYPE_STORAGE") == "db":
    

    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """public instance attributes:
       id, created_at, updated_at
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, nullable=False, 
                default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, 
                default=datetime.utcnow())
