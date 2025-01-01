from __future__ import annotations

import re
import logging
import aisuite as ai

from enum import Enum
from copy import deepcopy
from typing import List, Callable
from faker import Faker
from .Interaction import Interaction
from .AgentInteractionManager import AgentInteractionManager
from .Config import Config
from .utils import cache_w_checkpoint_manager


class DefaultValue(Enum):
    NOT_PROVIDED = "NOT_PROVIDED"


faker = Faker()
config = Config()
llm_client = ai.Client({**config.aisuite})


class Agent:
    """
    A class representing an autonomous agent in the environment.

    The Agent class is the core component of the Agentarium system, representing
    an individual entity capable of:
    - Maintaining its own identity and characteristics
    - Interacting with other agents through messages
    - Making autonomous decisions based on its state and interactions
    - Generating responses using natural language models

    Each agent has a unique identifier and a set of characteristics that define
    its personality and behavior. These characteristics can be either provided
    during initialization or generated automatically.

    Attributes:
        agent_id (str): Unique identifier for the agent
        agent_informations (dict): Dictionary containing agent characteristics
            including name, age, gender, occupation, location, and bio
        _interaction_manager (AgentInteractionManager): Singleton instance managing
            all agent interactions
    """

    _interaction_manager = AgentInteractionManager()
    _allow_init = False

    _default_generate_agent_prompt = """You're goal is to generate the bio of a fictional person.
Make this bio as realistic and as detailed as possible.
You may be given information about the person to generate a bio for, if so, use that information to generate a bio.
If you are not given any information about the person, generate a bio for a random person.

You must generate the bio in the following format:
Bio: [Bio of the person]
"""

    _default_actions = {
        "THINK": {
            "format": "[THINK][CONTENT]",
            "prompt": "Think about something.",
            "example": "[THINK][It's such a beautiful day!]",
        },
        "TALK": {
            "format": "[TALK][AGENT_ID][CONTENT]",
            "prompt": "Talk to the agent with the given ID. Note that you must the agent ID, not the agent name.",
            "example": "[TALK][123][Hello!]",
        },
    }

    _default_act_prompt = """
Informations about yourself:
{agent_informations}

Your interactions:
{interactions}

Given the above information, think about what you should do next.

The following are the possible actions you can take:
{actions}

Write in the following format:
<THINK>
{{YOUR_THOUGHTS}}
</THINK>

<ACTION>
[{{One of the following actions: {list_of_actions}}}]
</ACTION>
"""

    def __init__(self, **kwargs):
        """
        Initialize an agent with given or generated characteristics.
        This method should not be called directly - use create_agent() instead.
        """

        if not Agent._allow_init:
            raise RuntimeError("Agent instances should be created using Agent.create_agent()")

        if "agent_id" in kwargs:
            self.agent_id = kwargs.pop("agent_id")

        self.agent_id = self.agent_id if self.agent_id!= DefaultValue.NOT_PROVIDED else faker.uuid4()
        self.agent_informations: dict = kwargs or {}

        if "gender" not in kwargs or kwargs["gender"] == DefaultValue.NOT_PROVIDED:
            self.agent_informations["gender"] = faker.random_element(elements=["male", "female"])

        if "name" not in kwargs or kwargs["name"] == DefaultValue.NOT_PROVIDED:
            self.agent_informations["name"] = getattr(faker, f"name_{self.agent_informations['gender']}")()

        if "age" not in kwargs or kwargs["age"] == DefaultValue.NOT_PROVIDED:
            self.agent_informations["age"] = faker.random_int(18, 80)

        if "occupation" not in kwargs or kwargs["occupation"] == DefaultValue.NOT_PROVIDED:
            self.agent_informations["occupation"] = faker.job()

        if "location" not in kwargs or kwargs["location"] == DefaultValue.NOT_PROVIDED:
            self.agent_informations["location"] = faker.city()

        if "bio" not in kwargs or kwargs["bio"] == DefaultValue.NOT_PROVIDED:
            self.agent_informations["bio"] = Agent._generate_agent_bio(self.agent_informations)

        self._interaction_manager.register_agent(self)
        self._act_prompt = deepcopy(Agent._default_act_prompt)

        self._actions = deepcopy(Agent._default_actions)
        self._actions["TALK"]["function"] = self._talk_action_function
        self._actions["THINK"]["function"] = self._think_action_function

        self.storage = {}  # Useful for storing data between actions. Note: not used by the agentarium system.

    @staticmethod
    @cache_w_checkpoint_manager
    def create_agent(
        agent_id: str = DefaultValue.NOT_PROVIDED,
        gender: str = DefaultValue.NOT_PROVIDED,
        name: str = DefaultValue.NOT_PROVIDED,
        age: int = DefaultValue.NOT_PROVIDED,
        occupation: str = DefaultValue.NOT_PROVIDED,
        location: str = DefaultValue.NOT_PROVIDED,
        bio: str = DefaultValue.NOT_PROVIDED,
        **kwargs,
    ) -> Agent:
        """
        Initialize an agent with given or generated characteristics.

        Creates a new agent instance with a unique identifier and a set of
        characteristics. If specific characteristics are not provided, they
        are automatically generated to create a complete and realistic agent
        profile.

        The following characteristics are handled:
        - Gender (male/female)
        - Name (appropriate for the gender)
        - Age (between 18 and 80)
        - Occupation (randomly selected job)
        - Location (randomly selected city)
        - Bio (generated based on other characteristics)

        Args:
            **kwargs: Dictionary of agent characteristics to use instead of
                generating them. Any characteristic not provided will be
                automatically generated.
        """
        try:
            Agent._allow_init = True
            return Agent(agent_id=agent_id, gender=gender, name=name, age=age, occupation=occupation, location=location, bio=bio, **kwargs)
        finally:
            Agent._allow_init = False

    @property
    def name(self) -> str:
        """
        Get the agent's name.

        Returns:
            str: The name of the agent.
        """
        return self.agent_informations["name"]

    @staticmethod
    def _generate_prompt_to_generate_bio(**kwargs) -> str:
        """
        Generate a prompt for creating an agent's biography.

        Creates a prompt that will be used by the language model to generate
        a realistic biography for the agent. If characteristics are provided,
        they are incorporated into the prompt to ensure the generated bio
        is consistent with the agent's existing traits.

        Args:
            **kwargs: Dictionary of agent characteristics to incorporate
                into the biography generation prompt.

        Returns:
            str: A formatted prompt string for biography generation.
        """
        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if not kwargs:
            return Agent._default_generate_agent_prompt

        prompt = Agent._default_generate_agent_prompt
        prompt += "\nInformation about the person to generate a bio for:"

        for key, value in kwargs.items():
            prompt += f"\n{key}: {value}"

        return prompt

    @staticmethod
    def _generate_agent_bio(agent_informations: dict) -> str:
        """
        Generate a biography for an agent using a language model.

        Uses the OpenAI API to generate a realistic and detailed biography
        based on the agent's characteristics. The biography is generated
        to be consistent with any existing information about the agent.

        Args:
            agent_informations (dict): Dictionary of agent characteristics
                to use in generating the biography.

        Returns:
            str: A generated biography for the agent.
        """
        prompt = Agent._generate_prompt_to_generate_bio(**agent_informations)

        response = llm_client.chat.completions.create(
            model=f"{config.llm_provider}:{config.llm_model}",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
        )

        return response.choices[0].message.content

    @cache_w_checkpoint_manager
    def act(self) -> str:
        """
        Generate and execute the agent's next action.

        Uses the language model to determine and perform the agent's next
        action based on their characteristics and interaction history.
        The agent can either think to themselves or talk to another agent.

        Returns:
            str: The complete response from the language model, including
                the agent's thoughts and chosen action.

        Raises:
            RuntimeError: If the action format is invalid or if the target
                agent for a TALK action is not found.
        """

        # [THINK][CONTENT]: Think about something. (i.e [THINK][It's such a beautiful day!])
        # [TALK][AGENT_ID][CONTENT]: Talk to the agent with the given ID. Note that you must the agent ID, not the agent name. (i.e [TALK][123][Hello!])
        # [CHATGPT][CONTENT]: Use ChatGPT. (i.e [CHATGPT][Hello!])

        prompt = self._act_prompt.format(
            agent_informations=self.agent_informations,
            interactions=self.get_interactions(),
            actions="\n".join([f"{action['format']}: {action['prompt']} (i.e {action['example']})" for action in self._actions.values()]),
            list_of_actions=list(self._actions.keys()),
        )

        response = llm_client.chat.completions.create(
            model=f"{config.llm_provider}:{config.llm_model}",
            messages=[
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
        )

        actions = re.search(r"<ACTION>(.*?)</ACTION>", response.choices[0].message.content, re.DOTALL).group(1).strip().split("]")
        actions = [action.replace("[", "").replace("]", "").strip() for action in actions]

        if actions[0] in self._actions:
            return self._actions[actions[0]]["function"](*actions[1:])

        raise RuntimeError(f"Invalid action: '{actions[0]}'. Received output: {response.choices[0].message.content}")

    def dump(self) -> dict:
        """
        Dump the agent's state to a dictionary.
        """

        return {
            "agent_id": self.agent_id,
            "agent_informations": self.agent_informations,
            "interactions": [interaction.dump() for interaction in self._interaction_manager._agent_private_interactions[self.agent_id]],
        }

    def __str__(self) -> str:
        """
        Get a string representation of the agent.

        Returns:
            str: A formatted string containing all the agent's characteristics.
        """
        return "\n".join([f"{key.capitalize()}: {value}" for key, value in self.agent_informations.items()])

    def __repr__(self) -> str:
        """
        Get a string representation of the agent, same as __str__.

        Returns:
            str: A formatted string containing all the agent's characteristics.
        """
        return Agent.__str__(self)

    def get_interactions(self) -> List[Interaction]:
        """
        Retrieve all interactions involving this agent.

        Returns:
            List[Interaction]: A list of all interactions where this agent
                was either the sender or receiver.
        """
        return self._interaction_manager.get_agent_interactions(self)

    def _talk_action_function(self, *params) -> None:
        """
        Send a message to another agent.
        """
        if len(params) < 2:
            raise RuntimeError(f"Received a TALK action with less than 2 arguments: {params}")

        if (receiver := self._interaction_manager.get_agent(params[0])) is None:
            raise RuntimeError(f"Received a TALK action with an invalid agent ID: {params[0]}. {params=}")

        return self.talk_to(receiver, params[1])

    @cache_w_checkpoint_manager
    def talk_to(self, receiver: Agent, message: str) -> None:
        """
        Send a message to another agent.

        Records an interaction where this agent sends a message to another agent.

        Args:
            receiver (Agent): The agent to send the message to.
            message (str): The content of the message to send.
        """

        self._interaction_manager.record_interaction(self, receiver, message)

        return {
            "action": "TALK",
            "sender": self.agent_id,
            "receiver": receiver.agent_id,
            "message": message,
        }

    def _think_action_function(self, *params) -> None:
        """
        Think about a message.
        """
        if len(params) < 1:
            raise RuntimeError(f"Received a THINK action with less than 1 argument: {params}")

        return self.think(params[0])

    @cache_w_checkpoint_manager
    def think(self, message: str) -> None:
        """
        Think about a message.

        Records an interaction where this agent thinks about a message.

        Args:
            message (str): The content of the message to think about.
        """

        self._interaction_manager.record_interaction(self, self, message)

        return {
            "action": "THINK",
            "sender": self.agent_id,
            "receiver": self.agent_id,
            "message": message,
        }

    def add_new_action(self, action_descriptor: dict[str, str], action_function: Callable[[Agent, str], str | dict]) -> None:
        """
        Add a new action to the agent's capabilities.

        This method allows extending an agent's behavior by adding custom actions. Each action consists of:
        1. A descriptor that tells the agent how to use the action
        2. A function that implements the action's behavior

        Args:
            action_descriptor (dict[str, str]): A dictionary describing the action with these required keys:
                - "format": Format string showing action syntax. Must start with [ACTION_NAME] in caps,
                           followed by parameter placeholders in brackets. Example: "[CHATGPT][message]"
                - "prompt": Human-readable description of what the action does
                - "example": Concrete example showing how to use the action
            action_function (Callable[[Agent, str], str | dict]): Function implementing the action.
                - First parameter must be the agent instance
                - Remaining parameters should match the format string
                - Can return either a string or a dictionary
                - If returning a dict, the 'action' key is reserved and will be overwritten
                - If returning a non-dict value, it will be stored under the 'output' key

        Raises:
            RuntimeError: If the action_descriptor is missing required keys or if the action
                         name conflicts with an existing action

        Example:
            ```python
            # Adding a ChatGPT integration action
            agent.add_new_action(
                action_descriptor={
                    "format": "[CHATGPT][Your message here]",
                    "prompt": "Use ChatGPT to have a conversation or ask questions.",
                    "example": "[CHATGPT][What's the weather like today?]"
                },
                action_function=use_chatgpt
            )

            # The action function could look like:
            def use_chatgpt(agent: Agent, message: str) -> dict:
                response = call_chatgpt_api(message)
                return {
                    "message": message,
                    "response": response
                }  # Will be automatically formatted to include "action": "CHATGPT"
            ```

        Notes:
            - The action name is extracted from the first bracket pair in the format string
            - The action function's output will be automatically standardized to include the action name
            - Any 'action' key in the function's output dictionary will be overwritten
        """

        if "format" not in action_descriptor:
            raise RuntimeError(f"Invalid action: {action_descriptor}, missing 'format'")

        name = action_descriptor["format"].split("[")[1].split("]")[0]

        if len(name) < 1:
            raise RuntimeError(f"Invalid action format: {action_descriptor['format']}, first name must be a single word")

        if name in self._actions:
            raise RuntimeError(f"Action {action_descriptor} already exists")

        if "prompt" not in action_descriptor:
            raise RuntimeError(f"Invalid action: {action_descriptor}, missing 'prompt'")

        if "example" not in action_descriptor:
            raise RuntimeError(f"Invalid action: {action_descriptor}, missing 'example'")

        def standardize_action_output(fun):
            """
            Standardizes the output format of action functions.

            This decorator ensures that all action functions return a dictionary with a
            consistent format, containing at minimum an 'action' key with the action name.
            If the original function returns a dictionary, its contents are preserved
            (except for the 'action' key which may be overwritten). If it returns a
            non-dictionary value, it is stored under the 'output' key.

            Args:
                fun (Callable): The action function to decorate.

            Returns:
                Callable: A wrapped function that standardizes the output format.
            """

            def wrapper(*args, **kwargs):
                fn_output = fun(self, *args, **kwargs)

                output = fn_output if type(fn_output) == dict else {"output": fn_output}

                if "action" in output:
                    logging.warning((
                        f"The action '{name}' returned an output with an 'action' key. "
                        "This is not allowed, it will be overwritten."
                    ))

                output["action"] = name

                return output

            return wrapper

        self._actions[name] = action_descriptor
        self._actions[name]["function"] = standardize_action_output(action_function)

    def reset(self) -> None:
        """
        Reset the agent's state.
        """
        self._interaction_manager.reset_agent(self)
        self.storage = {}


if __name__ == "__main__":

    interaction = Interaction(
        sender=Agent(name="Alice", bio="Alice is a software engineer."),
        receiver=Agent(name="Bob", bio="Bob is a data scientist."),
        message="Hello Bob! I heard you're working on some interesting data science projects."
    )

    print(interaction)
