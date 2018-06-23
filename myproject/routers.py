from rest_framework import routers
from myapp.views import ContactViewSet
router = routers.SimpleRouter()

router.register(r'', ContactViewSet)
