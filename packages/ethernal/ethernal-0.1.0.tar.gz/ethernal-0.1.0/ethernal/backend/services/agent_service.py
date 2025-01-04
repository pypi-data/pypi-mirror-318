from typing import Dict, Optional
from models.agent import Agent
from core.ai_engine import AIEngine
from core.blockchain import BlockchainManager
from core.prompt_manager import PromptManager


class AgentService:
    def __init__(self):
        self.ai_engine = AIEngine()
        self.blockchain = BlockchainManager()
        self.prompt_manager = PromptManager()

    async def create_agent(
            self,
            name: str,
            description: str,
            model_configuration: Dict,
            creator_id: str
    ) -> Agent:
        agent = Agent(
            name=name,
            description=description,
            model_configuration=model_configuration,
            creator_id=creator_id
        )

        # Create token for the agent
        token_address = await self.blockchain.create_token(
            agent.id,
            initial_supply=1000000
        )
        agent.token_address = token_address

        # Generate system prompt
        system_prompt = self.prompt_manager.generate_system_prompt(
            name=name,
            description=description,
            configuration=model_configuration
        )
        agent.system_prompt = system_prompt

        await agent.save()
        return agent

    async def get_response(
            self,
            agent_id: str,
            prompt: str,
            context: Optional[Dict] = None
    ) -> str:
        agent = await Agent.get(agent_id)
        if not agent:
            raise ValueError("Agent not found")

        response = await self.ai_engine.generate_response(
            agent=agent,
            prompt=prompt,
            context=context
        )

        return response

    async def update_agent(
            self,
            agent_id: str,
            updates: Dict
    ) -> Agent:
        agent = await Agent.get(agent_id)
        if not agent:
            raise ValueError("Agent not found")

        for key, value in updates.items():
            setattr(agent, key, value)

        if "model_configuration" in updates:
            system_prompt = self.prompt_manager.generate_system_prompt(
                name=agent.name,
                description=agent.description,
                configuration=agent.model_configuration
            )
            agent.system_prompt = system_prompt

        await agent.save()
        return agent