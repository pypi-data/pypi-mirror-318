from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Optional
from models.agent import Agent
from services.agent_service import AgentService
from services.deployment_service import DeploymentService
from services.auth_service import get_current_user

router = APIRouter()
agent_service = AgentService()
deployment_service = DeploymentService()

@router.post("/agents")
async def create_agent(
    agent_data: Dict,
    current_user = Depends(get_current_user)
):
    try:
        agent = await agent_service.create_agent(
            name=agent_data["name"],
            description=agent_data["description"],
            model_configuration=agent_data["model_configuration"],
            creator_id=current_user.id
        )
        return agent
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/agents/{agent_id}/deploy")
async def deploy_agent(
    agent_id: str,
    deployment_data: Dict,
    current_user = Depends(get_current_user)
):
    agent = await Agent.get(agent_id)
    if not agent or agent.creator_id != current_user.id:
        raise HTTPException(status_code=404, detail="Agent not found")

    try:
        deployment_result = await deployment_service.deploy_agent(
            agent=agent,
            domain=deployment_data["domain"]
        )
        return deployment_result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/agents/{agent_id}/chat")
async def chat_with_agent(
    agent_id: str,
    chat_data: Dict,
    current_user = Depends(get_current_user)
):
    try:
        response = await agent_service.get_response(
            agent_id=agent_id,
            prompt=chat_data["prompt"],
            context=chat_data.get("context")
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))