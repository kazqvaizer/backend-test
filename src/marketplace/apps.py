from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MarketplaceConfig(AppConfig):
    name = "marketplace"
    verbose_name = _("Marketplace")
