from typing import Dict, Optional
import openai
from models.agent import Agent
from config.settings import Settings


class AIEngine:
    def __init__(self):
        self.settings = Settings()
        openai.api_key = self.settings.openai_api_key
        self.model_configs = {
            "gpt-4": {"max_tokens": 8192, "temperature": 0.7},
            "gpt-3.5-turbo": {"max_tokens": 4096, "temperature": 0.8}
        }

    async def generate_response(
            self,
            agent: Agent,
            prompt: str,
            context: Optional[Dict] = None
    ) -> str:
        model = agent.model_configuration.get("model", "gpt-3.5-turbo")

        messages = self._prepare_messages(agent, prompt, context)
        response = await openai.ChatCompletion.create(
            model=model,
            messages=messages,
            **self._get_model_config(model)
        )

        return response.choices[0].message.content

    def _prepare_messages(
            self,
            agent: Agent,
            prompt: str,
            context: Optional[Dict]
    ) -> List[Dict]:
        messages = [
            {"role": "system", "content": agent.system_prompt},
            {"role": "user", "content": prompt}
        ]

        if context:
            messages.insert(1, {
                "role": "system",
                "content": f"Context: {context}"
            })

        return messages

    def _get_model_config(self, model: str) -> Dict:
        return self.model_configs.get(model, self.model_configs["gpt-3.5-turbo"])