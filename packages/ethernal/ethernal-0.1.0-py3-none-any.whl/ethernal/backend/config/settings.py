from pydantic import BaseSettings


class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"
    openai_api_key: str
    ethereum_rpc_url: str
    token_contract_address: str
    token_contract_abi: list
    admin_address: str
    admin_private_key: str
    chain_id: int = 1
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    redis_url: str = "redis://localhost"
    kubernetes_config: str = "~/.kube/config"
    domain_suffix: str = "ethernal.ai"

    solana_rpc_url: str = ""
    solana_network: str = ""
    admin_private_key: list[int]
    token_program_id: str = ""


    class Config:
        env_file = ".env"