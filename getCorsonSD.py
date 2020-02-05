from bs4 import BeautifulSoup
from corsonSD import simple_get
from corsonSD import log_error


def get_parcel():
  
  """
  Downloads the page where the list of parcel numbers is found 
  and return a list of strings, one per parcel
  """
  
  url = 'http://guidepost.schneidercorp.com/Search.aspx'
  response = simple_get(url)
  
  if response is not None:
    html = BeautifulSoup(response, 'html.parser')
    parcels = set()
    for li in html.select('li'):
      for parcel in li.text.split('\n'):
        if len(parcel) > 0:
          parcels.add(parcel.strip())
        return list(parcels)