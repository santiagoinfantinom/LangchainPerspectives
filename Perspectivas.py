perspectives = ['Cowboy','Witch','Policeman','Professor','Clown','King','Psychologist','Alcoholic','Mom']

story = open("CrimeAndPunishment.txt","r")

questions = [
    "What is the central theme of the novel?",
    "Who is the protagonist and how do they develop throughout the story?",
    "What are the main conflicts and how are they resolved?",
    "How does the setting influence the plot?",
    "What symbolism can be identified in the novel?",
    "How do the relationships between characters affect the plot development?",
    "What role do secondary characters play in the story?",
    "How do the main characters change throughout the novel?",
    "What literary techniques does the author use to tell the story?",
    "How are good and evil represented in the novel?",
    "What moral dilemmas are presented and how do the characters face them?",
    "How is the climax of the story developed?",
    "What type of narrator does the novel have and how does this affect the story's perspective?",
    "Is there any surprising plot twist?",
    "How is the novel resolved and is the ending satisfactory?",
    "What social themes are explored in the novel?",
    "How is dialogue used to reveal information about the characters?",
    "What importance do symbolic objects or places have in the novel?",
    "How is the passage of time handled within the narrative?",
    "What emotions does the author seek to evoke in the reader?",
    "Is there a lesson or message that the author wants to convey?",
    "How does this novel compare to other works by the same author?",
    "What social criticisms can be inferred from the reading?",
    "How could the novel be interpreted from different theoretical perspectives (feminist, Marxist, psychoanalytic, etc.)?",
    "What questions does the novel leave unanswered?",
    "How does the novel relate to the historical context in which it was written?",
    "What aspects of the novel are innovative or unique within its genre?",
    "How does the novel contribute to the literary genre to which it belongs?",
    "What impact could the novel have on the modern reader?",
    "What alternative interpretations could be given to the plot or characters?"
]

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
model = ChatOpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio", temperature=0, model="mistralai_mistral-7b-instruct-v0.2")

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

answers = []

for perspective in perspectives:
    for question in questions:
        template = """
        Imagine you read Crime and Punishment from F.Dostojevski.
        Answer each one of the {questions}, like you were a {perspectives}.
        Do not add extra information.

        """
        answers.append(template)

print(answers)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model | parser







