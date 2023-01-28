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


class GenericK8sAPIView(APIView):
    @staticmethod
    def cluster_function(**kwargs):
        raise NotImplementedError("Subclasses should implement cluster_function")

    @forbiden_exception_handler
    def get(self, request, **kwargs):
        return Response(self.__class__.cluster_function(**kwargs))


class ListAllPodAPIView(GenericK8sAPIView):
    """
    View to list all pods in all namespaces.
    """

    @staticmethod
    def cluster_function(**kwargs):
        return get_pods()


class ListNamespacedPodAPIView(GenericK8sAPIView):
    """
    View to list  pods in a namespace.
    """

    @staticmethod
    def cluster_function(**kwargs):
        return get_pods_by_namespace(namespace=kwargs['namespace'])


class ListAllDeploymentAPIView(GenericK8sAPIView):
    """
    View to list all deployments in all namespaces.
    """

    @staticmethod
    def cluster_function(**kwargs):
        return get_deployments()


class ListNamespacedDeploymentAPIView(GenericK8sAPIView):
    """
    View to list deployments in a namespace.
    """

    @staticmethod
    def cluster_function(**kwargs):
        return get_deployments_by_namespace(namespace=kwargs['namespace'])
