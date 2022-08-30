#!/usr/bin/python3
"""The Base Class Module for AirBnB Console"""
import uuid
import datetime from datetime


class BaseModel:
  """nitializing the constructor"""
  
  def __init__(self):
    self.id = str(uuid.uuid4())
    self.created_at = datetime.now() 
    self.updated_at = datetime.now()
    
  def __str__(self):
    """string representation"""
    return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
  def save(self):
    self.updated_at = datetime.now()
  
  def todict(self):
    for key, value in self.__dict__.items():
      if isinstance(value, datetime):
        result[key] = value.isoformat()
      else:
        result[key] = value
    result['__class__'] = self.__class__.__name__
    return result 