

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from courses.views import (CourseViewSet, DocumentDetail, DocumentList,
                           EmbedModelViewSet, LectureModelViewSet,
                           PdfCreateAPIView, PdfDestroyAPIView,
                           PdfDetailAPIView, PdfListAPIView,
                           PdfRetrieveUpdateAPIView, PdfUpdateAPIView)

router = DefaultRouter()

router.register('course', CourseViewSet, basename='course')
router.register('lecture', LectureModelViewSet, basename='lecture')
router.register('embed-lecture', EmbedModelViewSet, basename='embed-lecture')

urlpatterns = [
    # path('course-auth/', include('rest_framework.urls')), # for user's login and logout
    path('', include(router.urls)),  # for Router urls

    # for APIView
    path('document/', DocumentList.as_view()),
    path('document/<int:pk>/', DocumentDetail.as_view()),

    # for genericAPIView
    path('pdf-create/', PdfCreateAPIView.as_view(), name='pdf-create'),
    path('pdf-list/', PdfListAPIView.as_view(), name='pdf-list'),
    path('pdf-detail/<int:pk>/', PdfDetailAPIView.as_view(), name='pdf-detail'),
    path('pdf-update/<int:pk>/', PdfUpdateAPIView.as_view(), name='pdf-update'),
    # path('api/pdf-partial-update/<int:pk>/', PdfRetrieveUpdateAPIView.as_view(),
    #       name='pdf-partial-update'),
    path('pdf-delete/<int:pk>/', PdfDestroyAPIView.as_view(), name='pdf-delete'),
]
