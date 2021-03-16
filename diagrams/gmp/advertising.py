
from . import _GMP

class _Advertising(_GMP):
    _type = "advertising"
    _icon_dir = "resources/gmp/advertising"

class GoogleAds(_Advertising):
    _icon = "google-ads.png"

class GoogleSearchAds360(_Advertising):
    _icon = "google-search-ads-360.png"

class GoogleDisplayVideo360(_Advertising):
    _icon = "google-display-video-360.png"

class GoogleCampaignManager(_Advertising):
    _icon = "google-campaign-manager.png"


# Aliases
Adwords = GoogleAds
SA360 = GoogleSearchAds360
DV360 = GoogleDisplayVideo360
CM = GoogleCampaignManager