"""Basic AutoGen functionality verification for Story 1.1"""

import autogen
from typing import Tuple


def test_basic_agent_creation() -> None:
    """Verify basic AutoGen agent creation works"""
    print("🔧 Testing basic AutoGen agent creation...")

    # Create a simple assistant agent
    assistant = autogen.AssistantAgent(
        name="test_assistant",
        system_message="You are a helpful assistant for testing AutoGen functionality.",
        llm_config=False,  # No LLM for basic testing
    )

    # Create a user proxy agent
    user_proxy = autogen.UserProxyAgent(
        name="test_user",
        human_input_mode="NEVER",
        code_execution_config=False,
        system_message="You are a user proxy for testing purposes.",
    )

    print("  ✅ AssistantAgent created successfully")
    print("  ✅ UserProxyAgent created successfully")

    # Assert instead of return
    assert assistant.name == "test_assistant"
    assert user_proxy.name == "test_user"


def test_basic_groupchat() -> None:
    """Verify basic GroupChat functionality"""
    print("🔧 Testing basic GroupChat functionality...")

    # Create agents first
    assistant = autogen.AssistantAgent(
        name="test_assistant",
        system_message="You are a helpful assistant for testing AutoGen functionality.",
        llm_config=False,
    )

    user_proxy = autogen.UserProxyAgent(
        name="test_user",
        human_input_mode="NEVER",
        code_execution_config=False,
        system_message="You are a user proxy for testing purposes.",
    )

    # Create GroupChat
    groupchat = autogen.GroupChat(
        agents=[assistant, user_proxy],
        messages=[],
        max_round=1,
        speaker_selection_method="round_robin",
    )

    # Create GroupChat manager
    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config=False,
        system_message="You are a group chat manager for testing purposes.",
    )

    print("  ✅ GroupChat created successfully")
    print("  ✅ GroupChatManager created successfully")

    # Assert instead of return
    assert len(groupchat.agents) == 2
    assert groupchat.max_round == 1
    assert isinstance(manager, autogen.GroupChatManager)


def verify_autogen_integration() -> bool:
    """Comprehensive AutoGen integration verification

    Returns:
        True if all tests pass, False otherwise
    """
    try:
        # Test basic agent creation
        test_basic_agent_creation()

        # Test GroupChat functionality  
        test_basic_groupchat()

        print("🎯 All AutoGen integration tests passed!")
        return True

    except Exception as e:
        print(f"❌ AutoGen integration test failed: {e}")
        return False


if __name__ == "__main__":
    success = verify_autogen_integration()
    if success:
        print("\n✅ Story 1.1 AutoGen Integration: COMPLETE")
    else:
        print("\n❌ Story 1.1 AutoGen Integration: FAILED")
        exit(1)
