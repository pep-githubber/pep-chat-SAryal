from datetime import datetime
from google.appengine.api import memcache
from google.appengine.ext import ndb
import random

_LAST_GET_KEY_PREFIX = 'lastget'
_LAST_POST_KEY = 'lastpost'


class Remark(ndb.Model):

  user = ndb.StringProperty(required=True) # ID of the user who sent this.
  text = ndb.StringProperty(required=True) # The text the user entered.

  timestamp = ndb.DateTimeProperty(auto_now_add=True, required=True)

def Hex_Checker(self, hex_value):
    if len(hex_value) < 2:
        return "0" + hex_value
    else:
        return hex_value

def Randomly_Color(self):
    color_value = lambda: random.randint(0, 255)
    hex_red = self.Hex_Checker(hex(color_value())[2:])
    hex_green = self.Hex_Checker(hex(color_value())[2:])
    hex_blue = self.Hex_Checker(hex(color_value())[2:])
    return "#{0}{1}{2}".format(hex_red, hex_green, hex_blue) 

print Randomly_Color()
def ReadRemarks(user_id):
  start_time = memcache.get(_MakeLastGetKey(user_id))

  LogLastGet(user_id)

  # TODO(pep-students) Make messages appear a random color.
  remark_infos = [
      (remark.user, remark.text, self.Randomly_Color())
      for remark
      in Remark.query(
          Remark.timestamp >= start_time).order(Remark.timestamp).fetch()]
  return remark_infos


def PostRemark(user, text):
  Remark(user=user, text=text).put()


def _MakeLastGetKey(user_id):
  return ';'.join([_LAST_GET_KEY_PREFIX, user_id])


def LogLastGet(user_id):
  memcache.set(_MakeLastGetKey(user_id), datetime.now())
