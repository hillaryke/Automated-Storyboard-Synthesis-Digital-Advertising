import os
from autogen import ConversableAgent
import os
os.chdir("../")

from src.image_composition import compose_ad_frame  # Import the composition function
from misc import Settings

config_list = [
    {
        "model": "gpt-4o", 
    }
]

class AdStoryboardGenerator:
    """
    A class for generating ad storyboards using AutoGen agents and image composition.
    """

    def __init__(self, assets_path):
        """
        Initializes the AdStoryboardGenerator with the assets path.
        """
        self.assets_path = assets_path
        self._initialize_agents()
        self.message = Settings.IMAGE_COMPOSITION_AGENT_MESSAGE

    def _initialize_agents(self):
        """
        Initializes the assistant and user proxy agents.
        """
        llm_config_assistant = Settings.LLM_CONFIG_ASSISTANT

        # Create the assistant agent
        self.assistant = ConversableAgent(
            name="Assistant",
            system_message="You are a helpful AI assistant. "
            "You can compose ad assets to make an AD Frame for StoryBoard. "
            "Return 'TERMINATE' when the task is done.",
            llm_config=llm_config_assistant,
        )
    
        # Create the user proxy agent
        self.user_proxy = ConversableAgent(
            name="User",
            llm_config=False,
            is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
            human_input_mode="NEVER",
            max_consecutive_auto_reply=3,
            function_map={
                "compose_ad_frame": self.compose_ad_frame  # Maps the compose_ad_frame function
            }
        )

    def generate_frame(self):
        """
        Generates the ad frame using the assistant and user proxy agents.
        """
        chat_result = self.user_proxy.initiate_chat(self.assistant, message=self.message, max_turns=2)
        

# Example usage:
if __name__ == "__main__":
    generator = AdStoryboardGenerator('/home/hillary_kipkemoi/Automated-Storyboard-Synthesis-Digital-Advertising/data/Assets/0a22f881b77f00220f2034c21a18b854/')
    generator.generate_frame()
