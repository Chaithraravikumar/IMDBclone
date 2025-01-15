from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (WatchList, WatchList_detailFV, WatchListAV, WatchListDetailAV, StreamplatformAV, 
                                        StreamplatformDetailAV, ReviewList, ReviewDetail, ReviewListCV, ReviewDetailCV, 
                                        ReviewParticular, ReviewCreateCV, StreamplatformViewset, StreamplatformModelviewset,
                                        UserReview, WatchListFilter, WatchListPage)
# from watchlist_app.views import watchlist, movie_detail

router = DefaultRouter()
router.register(r'stream', StreamplatformModelviewset, basename='stream')

urlpatterns = [
    path('function-based/movie_list/',WatchList),
    path('function-based/<int:pk>/',WatchList_detailFV),
    
    
    path('', include(router.urls)),
    
    # path('stramplatform_list/',StreamplatformAV.as_view(),name= 'stream-list'),
    # path('stramplatform_details/<int:pk>', StreamplatformDetailAV.as_view(), name = 'stream-detail'),
    
    path('class-based/movie_list/',WatchListAV.as_view(),name= 'movie-list'),
    path('class-based/<int:pk>', WatchListDetailAV.as_view(), name = 'movie-detail'),
    path('movie_list/',WatchListFilter.as_view(),name= 'movie-list-filter'),
    path('movie_list_page/',WatchListPage.as_view(),name= 'movie-list-pagination'),
    
    path('mixin-review-list/',ReviewList.as_view(), name = 'review-listmixin'),
    path('mixin-review_details/<int:pk>/',ReviewDetail.as_view(), name = 'review-detailmixin'),
    
    path('concrete-view-review-list/',ReviewListCV.as_view(), name = 'review-listcv'),
    path('concrete-view-review-list/<int:pk>/review/',ReviewParticular.as_view(), name = 'review-listcv'), # Review for particular movie based on movie ID
    path('concrete-view-review_details/<int:pk>/reviewcreate/',ReviewCreateCV.as_view(), name = 'review-detailcv'),  # Create Review for particular movie based on movie ID
    path('concrete-view-review_details/<int:pk>/',ReviewDetailCV.as_view(), name = 'review-detailcv'),  # Get, put, delete, path particular review
    
    # path('review-detail/<str:username>/',UserReview.as_view(),name = 'review-username') # Below parameter will be handeled on its own
    path('review-detail/',UserReview.as_view(),name = 'review-username')
    
]

# urlpatterns = [
#     path('movie_list/',watchlist),
#     path('<int:pk>',movie_detail),
# ]