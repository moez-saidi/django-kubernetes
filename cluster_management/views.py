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
    k8s_function = None

    @forbiden_exception_handler
    def get(self, request, **kwargs):
        return Response(self.k8s_function())


class ListAllPodAPIView(GenericK8sAPIView):
    """
    View to list all pods in all namespaces.
    """

    k8s_function = get_pods


class ListNamespacedPodAPIView(GenericK8sAPIView):
    """
    View to list  pods in a namespace.
    """

    k8s_function = get_pods_by_namespace


class ListAllDeploymentAPIView(GenericK8sAPIView):
    """
    View to list all deployments in all namespaces.
    """

    k8s_function = get_deployments


class ListNamespacedDeploymentAPIView(GenericK8sAPIView):
    """
    View to list deployments in a namespace.
    """

    k8s_function = get_deployments_by_namespace
