from rest_framework import routers

from services.views import SubscriptionView

router = routers.DefaultRouter()
router.register(r"subscriptions", SubscriptionView),
urlpatterns = []

urlpatterns += router.urls

app_name = "services"
