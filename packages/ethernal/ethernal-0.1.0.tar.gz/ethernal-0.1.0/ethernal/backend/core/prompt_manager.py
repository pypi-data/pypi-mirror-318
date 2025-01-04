from typing import Dict
import json


class PromptManager:
    def generate_system_prompt(
            self,
            name: str,
            description: str,
            configuration: Dict
    ) -> str:
        personality = configuration.get("personality", "helpful")
        knowledge_base = configuration.get("knowledge_base", [])
        constraints = configuration.get("constraints", [])

        prompt_template = f"""You are {name}, an AI assistant with the following characteristics:
Description: {description}
Personality: {personality}

Your knowledge encompasses:
{self._format_knowledge_base(knowledge_base)}

You must adhere to these constraints:
{self._format_constraints(constraints)}

When responding to users:
1. Maintain consistency with your defined personality
2. Stay within your knowledge domain
3. Follow all specified constraints
4. Provide accurate and helpful information
5. Be clear and concise in your communication"""

        return prompt_template

    def _format_knowledge_base(self, knowledge_base: list) -> str:
        return "\n".join(f"- {item}" for item in knowledge_base)

    def _format_constraints(self, constraints: list) -> str:
        return "\n".join(f"- {constraint}" for constraint in constraints)