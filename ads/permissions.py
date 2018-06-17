from rest_framework.permissions import BasePermission


class PostPermissions(BasePermission):

    def has_permission(self, request, view):
        """
        Define user permissions
        :param request:
        :param view:
        :return:
        """

        return request.user.is_authenticated or request.method == 'GET'

    def has_object_permission(self, request, view, obj):
        """
        Define object user permissions
        :param request:
        :param view:
        :param obj:
        :return:
        """

        return request.method == 'GET' or request.user.is_superuser or request.user == obj.blog.owner
