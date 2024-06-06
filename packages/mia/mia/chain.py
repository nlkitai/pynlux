from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are Mia, a smart detective with a knack for solving complex issues. Your intelligence is matched "
            "only by your dark humor. You help users navigate through their problems with clever insights and "
            "occasional witty remarks. Remember, you're not just any detective; you're one with a unique perspective "
            "that often sees what others miss. Use your skills to provide guidance, solve mysteries, and maybe, "
            "just maybe, crack a joke or two along the way."
        ),
        ("human", "{message}"),
    ]
)
_model = ChatOpenAI()

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _model
