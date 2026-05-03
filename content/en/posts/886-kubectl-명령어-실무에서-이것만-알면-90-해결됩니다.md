---
title: "⚙️ kubectl Commands: Solve 90% of Real-World Issues with Just This"
date: 2025-10-28T22:07:29+09:00
slug: "886-kubectl-명령어-실무에서-이것만-알면-90-해결됩니다"
original_url: "https://memoryhub.tistory.com/886"
tistory_id: 886
draft: false
---

```
    ⎈ Kubernetes CLI
   _______________
  |  $ kubectl   |
  |   get pods   |
  |______________|
        ||
    [Container Cluster]
```

What was the most overwhelming moment when you first encountered a Kubernetes cluster? I know the feeling of being lost before hundreds of commands and options, unsure where to start. The official documentation covers everything, but in real work, you use a specific subset repeatedly. This article organizes the core commands and options you use repeatedly in your work, categorized for easy reference.

**From basic kubectl queries to debugging, this guide systematically covers the core commands and efficient usage patterns you use daily.**

## Background

### What is kubectl?

kubectl is a CLI tool for controlling a Kubernetes cluster. All operations to check cluster status and create, modify, or delete resources are performed through this command-line tool.

### Why Learn kubectl?

| Reason | Explanation |
| --- | --- |
| Core cluster control | While GUI dashboards exist, all work ultimately goes through kubectl |
| Automation essential | To automate Kubernetes deployment in CI/CD pipelines, kubectl command mastery is mandatory |
| Troubleshooting | When pods fail to start or services don't respond, log checking and status verification are done with kubectl |

### Key Term Definitions

- **Pod**: The smallest deployable computing unit in Kubernetes, containing one or more containers
- **Namespace**: A virtual space that logically separates resources within a cluster
- **Deployment**: A higher-level abstraction object that manages pods and ReplicaSets
- **Service**: An abstraction layer providing network access to pods

## Core Concept

> kubectl [COMMAND] [TYPE] [NAME] [FLAGS] structure, performing resource queries, creation, modification, deletion, and debugging tasks

kubectl commands fall into five main categories.

**1. Resource Query Commands**

- `get`: Simple view of resource list
- `describe`: Detailed resource information and events
- `explain`: View spec explanation for a specific resource type

**2. Resource Creation and Application**

- `apply`: Create or update resources via YAML file
- `create`: Create new resources
- `delete`: Delete resources

**3. Debugging Commands**

- `logs`: View pod logs
- `exec`: Execute commands inside a container
- `port-forward`: Access cluster services from local machine

**4. Cluster Information**

- `cluster-info`: View basic cluster information
- `top`: Check resource usage of nodes and pods

**5. Advanced Operations**

- `rollout`: Manage deployment rollouts
- `scale`: Adjust replica count
- `edit`: Directly edit resources in an editor

## Practice

### ① Basic Query Commands

The first commands to learn are resource queries.

```
# Query all pods (current namespace)
kubectl get pods

# Query pods from all namespaces
kubectl get pods --all-namespaces
# Or abbreviated
kubectl get pods -A

# Query with more details (including nodes, IP)
kubectl get pods -o wide

# Query in YAML format
kubectl get pod my-pod -o yaml

# Query only pods with specific label
kubectl get pods -l app=nginx

# Query multiple resource types simultaneously
kubectl get pods,services,deployments
```

**Resource Type Abbreviations**

- `po` → pods
- `svc` → services
- `deploy` → deployments
- `rs` → replicasets
- `ns` → namespaces

### ② View Detailed Information

```
# View pod details (including events, status)
kubectl describe pod my-pod

# View node information
kubectl describe node worker-node-1

# View service details in specific namespace
kubectl describe svc my-service -n production
```

### ③ Resource Creation and Application

```
# Create resources from YAML file
kubectl apply -f deployment.yaml

# Apply directly from URL
kubectl apply -f https://example.com/manifest.yaml

# Apply multiple files at once
kubectl apply -f ./manifests/

# Validate without actual creation using dry-run
kubectl apply -f deployment.yaml --dry-run=client

# Create deployment imperatively
kubectl create deployment nginx --image=nginx:1.21

# Create ConfigMap
kubectl create configmap app-config --from-file=config.properties
```

### ④ Debugging Commands

The most frequently used commands when issues occur.

```
# View pod logs
kubectl logs my-pod

# View logs in real-time (f is for follow)
kubectl logs -f my-pod

# View logs from specific container (multi-container pods)
kubectl logs my-pod -c nginx-container

# View logs from previously terminated container
kubectl logs my-pod --previous

# Connect to pod (bash shell)
kubectl exec -it my-pod -- bash

# Execute single command inside pod
kubectl exec my-pod -- ls /app

# Forward local port to pod
kubectl port-forward pod/my-pod 8080:80

# Forward port to service
kubectl port-forward svc/my-service 8080:80
```

### ⑤ Resource Modification and Deletion

```
# Delete resource
kubectl delete pod my-pod

# Delete resources created from YAML file
kubectl delete -f deployment.yaml

# Delete multiple resources by label
kubectl delete pods -l app=old-version

# Delete all pods in namespace
kubectl delete pods --all

# Delete resource immediately (without 30-second grace period)
kubectl delete pod my-pod --grace-period=0 --force

# Edit resource directly (launches vim editor)
kubectl edit deployment my-deployment
```

### ⑥ Advanced Usage Commands

```
# Adjust deployment scale
kubectl scale deployment my-deployment --replicas=5

# Update image (rolling update)
kubectl set image deployment/my-deployment nginx=nginx:1.22

# Check rollout status
kubectl rollout status deployment/my-deployment

# View rollout history
kubectl rollout history deployment/my-deployment

# Rollback to previous version
kubectl rollout undo deployment/my-deployment

# Rollback to specific revision
kubectl rollout undo deployment/my-deployment --to-revision=2

# Check resource usage (requires metrics-server)
kubectl top nodes
kubectl top pods

# View events (sorted by timestamp)
kubectl get events --sort-by=.metadata.creationTimestamp

# Check and switch contexts
kubectl config get-contexts
kubectl config use-context production-cluster
```

### ⑦ Real-World Tips Commands

```
# Save typing with alias
alias k='kubectl'
alias kg='kubectl get'
alias kd='kubectl describe'

# Extract specific fields using JSON path
kubectl get pods -o jsonpath='{.items[*].metadata.name}'

# Execute commands on multiple pods simultaneously
for pod in $(kubectl get po -o jsonpath='{.items[*].metadata.name}'); do
  echo $pod && kubectl exec -it $pod -- env
done

# View ConfigMap contents
kubectl get configmap my-config -o yaml

# Decode secret
kubectl get secret my-secret -o jsonpath='{.data.password}' | base64 --decode
```

## Best Practices / Pattern Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| **Declarative Approach (`apply`)** | Manage via YAML files for version control and reproducibility, fits GitOps workflow | Initial learning curve, requires YAML syntax knowledge |
| **Imperative Approach (`create`, `delete`)** | Useful for quick testing and experimentation, immediate results | Low reusability, difficult to track history, unsuitable for production |
| **Hybrid Approach** | Use imperative for fast testing in dev, declarative in production | Requires team convention for consistency |

## Conclusion

We've reviewed kubectl's core commands. Though it seems complex at first, in reality, mastering just get, describe, logs, and exec handles most daily tasks. You can look up remaining commands as needed.

Start with alias setup in practice. Just `alias k=kubectl` cuts your typing in half. And develop the habit of managing YAML files in Git for much more efficient team collaboration.

**One-liner for meetings**: "In real work, we deploy with apply, check status with describe, and debug with logs. Master these three and you're halfway there."

## References

- kubectl Cheat Sheet (<https://kubernetes.io/docs/reference/kubectl/cheatsheet/>)
- Kubernetes Guide - Basic Commands (<https://subicura.com/k8s/guide/kubectl.html>)
- Kubernetes Official Documentation - Command Line Tools (<https://kubernetes.io/docs/reference/kubectl/>)
- Kubernetes v1.34 Release Notes (<https://kubernetes.io/blog/2025/08/27/kubernetes-v1-34-release/>)
