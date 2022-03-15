# from django.http import HttpResponse
#
#
# def allowed_groups(groups=[]):
#     def decorator(view_func):
#         def wrapper(request, *args, **kwargs):
#             user = request.user
#             if user.is_superuser:
#                 return view_func(request, *args, **kwargs)
#             if not user.is_authenticated:
#                 return HttpResponse('You must be signed in!')
#             if not user.groups.exists():
#                 return HttpResponse(f'You must be in one of the groups {", ".join(groups)}!')
#
#             user_group_names = [g.name for g in user.groups.all()]
#             result = set(user_group_names).intersection(groups)
#             if groups and not result:
#                 return HttpResponse(f'You must be in one of the groups {", ".join(groups)}!')
#             return view_func(request, *args, **kwargs)
#
#         return wrapper
#
#     return decorator


from django.http import HttpResponse


def check_user_able_to_see_page(*groups):
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=groups).exists():
                return function(request, *args, **kwargs)
            return HttpResponse('Unauthorized', status=401)

        return wrapper

    return decorator
