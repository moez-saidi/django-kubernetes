from rest_framework.response import Response
from rest_framework.views import APIView

from cluster_management.kubernetes_utils.client import (
    get_deployments,
    get_deployments_by_namespace,
    get_pods,
    get_pods_by_namespace,
)


class ListAllPodAPIView(APIView):
    """
    View to list all pods in all namespaces.
    """

    def get(self, request, format=None):
        """
        Return a list of pods.
        """
        return Response(get_pods())


class ListNamespacedPodAPIView(APIView):
    """
    View to list  pods in a namespace.
    """

    def get(self, request, namespace, format=None):
        """
        Return a list of pods by namespace.
        """
        return Response(get_pods_by_namespace(namespace))


class ListAllDeploymentAPIView(APIView):
    """
    View to list all deployments in all namespaces.
    """

    def get(self, request, format=None):
        """
        Return a list of deployments.
        """
        return Response(get_deployments())


class ListNamespacedDeploymentAPIView(APIView):
    """
    View to list  deployments in a namespace.
    """

    def get(self, request, namespace, format=None):
        """
        Return a list of deployments by namespace.
        """
        return Response(get_deployments_by_namespace(namespace))
