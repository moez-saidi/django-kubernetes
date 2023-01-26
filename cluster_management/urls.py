from django.urls import path

from cluster_management.views import (
    ListAllDeploymentAPIView,
    ListAllPodAPIView,
    ListNamespacedDeploymentAPIView,
    ListNamespacedPodAPIView,
)

urlpatterns = [
    path('pods', ListAllPodAPIView.as_view(), name='list_pod'),
    path('deployments', ListAllDeploymentAPIView.as_view(), name='list_deployment'),
    path('<str:namespace>/pods', ListNamespacedPodAPIView.as_view(), name='list_pod_by_namespace'),
    path(
        '<str:namespace>/deployments',
        ListNamespacedDeploymentAPIView.as_view(),
        name='list_deployment_by_namespace',
    ),
]
