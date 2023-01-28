from kubernetes.client.exceptions import ApiException
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from cluster_management.kubernetes_utils.client import (
    get_deployments,
    get_deployments_by_namespace,
    get_pods,
    get_pods_by_namespace,
)


def forbiden_exception_handler(method):
    def inner(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except ApiException as api_exception:
            return Response(api_exception.__dict__, status=HTTP_400_BAD_REQUEST)

    return inner


class ListAllPodAPIView(APIView):
    """
    View to list all pods in all namespaces.
    """

    @forbiden_exception_handler
    def get(self, request, format=None):
        """
        Return a list of pods.
        """
        return Response(get_pods())


class ListNamespacedPodAPIView(APIView):
    """
    View to list  pods in a namespace.
    """

    @forbiden_exception_handler
    def get(self, request, namespace, format=None):
        """
        Return a list of pods by namespace.
        """
        return Response(get_pods_by_namespace(namespace))


class ListAllDeploymentAPIView(APIView):
    """
    View to list all deployments in all namespaces.
    """

    @forbiden_exception_handler
    def get(self, request, format=None):
        """
        Return a list of deployments.
        """
        return Response(get_deployments())


class ListNamespacedDeploymentAPIView(APIView):
    """
    View to list  deployments in a namespace.
    """

    @forbiden_exception_handler
    def get(self, request, namespace, format=None):
        """
        Return a list of deployments by namespace.
        """
        return Response(get_deployments_by_namespace(namespace))
