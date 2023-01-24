# django-kubernetes
django-kubernetes is a platform that will deploy containerized applications across multiple hosts. It provides basic mechanisms for deployment, maintenance, and scaling of applications using the power of kubernetes under the hood.

This is primarily an educational project that will demonstrate the ability to work with K8 both in CLI and with the python client.

For now, it will serve (deploy) static applications like AWS S3 buckets and nginx.

# SETUP

- Install dependencies
```bash
pip install -r requirements-dev.txt
```

- Activate precommit hook

```bash
pre-commit install
```

- Setup alias for k8s

```bash
echo -n "alias k=kubectl" >> ~/.bashrc
echo -n "complete -o default -F __start_kubectl k" >> ~/.bashrc
```

# DEPLOY [THE HARD WAY]

- Namespace
```bash
k create ns dev
```
- Configs

```bash
k apply -f k8s/environments/development/configmaps
```

- Secrets

Make sure to fill the files with data before
```bash
k apply -f k8s/environments/development/secrets
```

- Database

```bash
k create -f k8s/bases/postgres/pv.yaml
k create -f k8s/bases/postgres/pvc.yaml
k create -f k8s/bases/postgres/service.yaml
k create -f k8s/bases/postgres/deployment.yaml
```

- Backend

```bash

k create -f k8s/bases/backend/service.yaml
k create -f k8s/bases/backend/deployment.yaml
```


# RESULT

- Check on any ip of your local machines inside the cluster on port **31000**
- If you are in the controle-plane node just go to http://127.0.0.1:31000  