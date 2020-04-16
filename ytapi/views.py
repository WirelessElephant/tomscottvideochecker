# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ytapi.helpers import getVideoTitleCount, getActualVideoCount

def home(request):
  titleCount = getVideoTitleCount()
  actualCount = getActualVideoCount()
  if titleCount == actualCount:
      descText = 'is accurate.'
  else:
      descText = 'is not accurate.'

  return render(request, 'ytapi/index.html', context={
      'descriptorText': descText,
      'titleCount': titleCount,
      'actualCount': actualCount
  })
