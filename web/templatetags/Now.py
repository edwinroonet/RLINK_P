from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag
def Now():
  """
    Returns the value datetime now.
  """
  date = datetime.now().strftime("%Y.%m.%d")
  ddd = str(datetime.now().weekday())
  if ddd == "0":
    ddd = "월"
  elif ddd == "1":
    ddd = "화"
  elif ddd == "2":
    ddd = "수"
  elif ddd == "3":
    ddd = "목"
  elif ddd == "4":
    ddd = "금"
  elif ddd == "5":
    ddd = "토"
  elif ddd == "6":
    ddd = "일"
  return date + " (" + ddd + ")"
