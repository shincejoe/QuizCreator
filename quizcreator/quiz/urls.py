from django.urls import include, path
from rest_framework.routers import DefaultRouter

from quiz.views.quiz_configure import QuizConfigure

router = DefaultRouter()
router.register('quiz-configure', QuizConfigure, basename='quiz-configure')

urlpatterns = [
    path('', include(router.urls))
]
