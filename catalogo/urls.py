from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JuegoViewSet, DesarrolladorViewSet, PlataformaViewSet, GeneroViewSet, ReseñaViewSet

router = DefaultRouter()
router.register(r'juegos', JuegoViewSet)
router.register(r'desarrolladores', DesarrolladorViewSet)
router.register(r'plataformas', PlataformaViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'reseñas', ReseñaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
