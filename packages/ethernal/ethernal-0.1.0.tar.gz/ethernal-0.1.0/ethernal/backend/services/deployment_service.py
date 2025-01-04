import docker
from kubernetes import client, config
from typing import Dict
from models.agent import Agent


class DeploymentService:
    def __init__(self):
        self.docker_client = docker.from_env()
        config.load_incluster_config()
        self.k8s_apps_v1 = client.AppsV1Api()
        self.k8s_core_v1 = client.CoreV1Api()

    async def deploy_agent(self, agent: Agent, domain: str) -> Dict:
        deployment_name = f"ethernal-{agent.id}"

        # Create deployment
        deployment = client.V1Deployment(
            metadata=client.V1ObjectMeta(name=deployment_name),
            spec=client.V1DeploymentSpec(
                replicas=1,
                selector=client.V1LabelSelector(
                    match_labels={"app": deployment_name}
                ),
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(
                        labels={"app": deployment_name}
                    ),
                    spec=client.V1PodSpec(
                        containers=[
                            client.V1Container(
                                name=deployment_name,
                                image="ethernal/agent:latest",
                                ports=[client.V1ContainerPort(container_port=8000)],
                                env=[
                                    client.V1EnvVar(
                                        name="AGENT_ID",
                                        value=agent.id
                                    ),
                                    client.V1EnvVar(
                                        name="DOMAIN",
                                        value=domain
                                    )
                                ]
                            )
                        ]
                    )
                )
            )
        )

        self.k8s_apps_v1.create_namespaced_deployment(
            namespace="default",
            body=deployment
        )

        # Create service
        service = client.V1Service(
            metadata=client.V1ObjectMeta(name=deployment_name),
            spec=client.V1ServiceSpec(
                selector={"app": deployment_name},
                ports=[client.V1ServicePort(port=80, target_port=8000)]
            )
        )

        self.k8s_core_v1.create_namespaced_service(
            namespace="default",
            body=service
        )

        # Configure ingress
        ingress_config = self._create_ingress_config(
            deployment_name,
            domain
        )

        return {
            "status": "deployed",
            "domain": domain,
            "deployment_name": deployment_name
        }

    def _create_ingress_config(self, deployment_name: str, domain: str):
        ingress = client.NetworkingV1beta1Ingress(
            metadata=client.V1ObjectMeta(
                name=deployment_name,
                annotations={
                    "kubernetes.io/ingress.class": "nginx",
                    "cert-manager.io/cluster-issuer": "letsencrypt-prod"
                }
            ),
            spec=client.NetworkingV1beta1IngressSpec(
                rules=[
                    client.NetworkingV1beta1IngressRule(
                        host=domain,
                        http=client.NetworkingV1beta1HTTPIngressRuleValue(
                            paths=[
                                client.NetworkingV1beta1HTTPIngressPath(
                                    path="/",
                                    backend=client.NetworkingV1beta1IngressBackend(
                                        service_name=deployment_name,
                                        service_port=80
                                    )
                                )
                            ]
                        )
                    )
                ],
                tls=[
                    client.NetworkingV1beta1IngressTLS(
                        hosts=[domain],
                        secret_name=f"{deployment_name}-tls"
                    )
                ]
            )
        )
        return ingress