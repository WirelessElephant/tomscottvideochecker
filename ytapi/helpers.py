import re

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from django.conf import settings

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Authorize the request and store authorization credentials.
def get_authenticated_service():
  return build(API_SERVICE_NAME, API_VERSION, developerKey=settings.YT_API_KEY)

def getVideoTitleCount():
  youtube = get_authenticated_service()
  response = youtube.videos().list(**{
      'id': 'BxV14h0kFs0',
      'part': 'snippet'
  }).execute()
  video_title = response['items'][0]['snippet']['title']
  return int(re.compile(r'This Video Has ([\d,]+) Views').search(video_title).groups()[0].replace(',', ''))

def getActualVideoCount():
  youtube = get_authenticated_service()
  response = youtube.videos().list(**{
      'id': 'BxV14h0kFs0',
      'part': 'statistics'
  }).execute()
  strCount = response['items'][0]['statistics']['viewCount']
  return int(strCount)
