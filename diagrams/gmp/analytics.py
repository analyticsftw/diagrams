
from . import _GMP

class _Analytics(_GMP):
    _type = "analytics"
    _icon_dir = "resources/gmp/analytics"


class GoogleUniversalAnalytics(_Analytics):
    _icon = "google-analytics-universal.png"

class GoogleAnalytics4(_Analytics):
    _icon = "google-analytics-4.png"

class GoogleTagManager(_Analytics):
    _icon = "google-tag-manager.png"

class GoogleDataStudio(_Analytics):
    _icon = "google-datastudio.png"

class GoogleOptimize(_Analytics):
    _icon = "google-optimize.png"

class GoogleAdsDataHub(_Analytics):
    _icon = "google-ads-data-hub.png"

# Aliases
GA3 = GoogleUniversalAnalytics
GA4 = GoogleAnalytics4
GDS = GoogleDataStudio
GTM = GoogleTagManager
ADH = GoogleAdsDataHub