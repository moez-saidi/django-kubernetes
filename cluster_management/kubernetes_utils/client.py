from django.conf import settings
from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()
api = client.ApiClient()

default_namespace = settings.ENV.lower()


def convert_to_json(function):
    def wrapper(*args):
        return api.sanitize_for_serialization(function(*args))

    return wrapper


@convert_to_json
def get_deployments_by_namespace(namespace=default_namespace):
    return apps_v1.list_namespaced_deployment(namespace=namespace)


@convert_to_json
def get_deployments():
    return apps_v1.list_deployment_for_all_namespaces()


@convert_to_json
def get_pods_by_namespace(namespace=default_namespace):
    return v1.list_namespaced_pod(namespace=namespace)


@convert_to_json
def get_pods(namespace=default_namespace):
    return v1.list_namespaced_pod(namespace=namespace)