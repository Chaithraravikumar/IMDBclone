# from django.shortcuts import render
# from watchlist_app.models import watch
# from django.http import JsonResponse


# def watchlist(request):
#     movies = watch.objects.all()
#     data = {
#         'movies' : list(movies.values())
#     }
#     return JsonResponse(data)
#     print(movies)
    
# def movie_detail(request,pk):
#     movies = watch.objects.get(pk=pk)
#     data = {
#         'name' : movies.name,
#         'description' : movies.description,
#         'active': movies.active,
#         'created_at': movies.created_at
#     }
#     return JsonResponse(data)