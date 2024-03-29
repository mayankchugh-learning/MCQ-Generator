import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenrator.utils import read_file,get_table_data
from langchain.callbacks import get_openai_callback
from src.mcqgenrator.mcqgenrator import generate_evaluate_chain
from src.mcqgenrator.logger import logging
#from langchain_community.llms import OpenAI
#from langchain_community.chat_models import ChatOpenAI
#from langchain_community.callbacks import get_openai_callback

projectPath = os.getenv("PATH_TO_PROJECT")

with open(projectPath+"Response.json","r") as file:
    RESPONSE_JSON=json.load(file)


def test_mcqgenrator():
  
    try:
        text=read_file("data.txt")
        #Count tokens and the cost of API call
        with get_openai_callback() as cb:
            response=generate_evaluate_chain(
                {
                "text": text,
                "number": mcq_count,
                "subject":subject,
                "tone": tone,
                "response_json": json.dumps(RESPONSE_JSON)
                 }
            )
        print(response)

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)

    else:
        print(f"Total Tokens:{cb.total_tokens}")
        print(f"Prompt Tokens:{cb.prompt_tokens}")
        print(f"Completion Tokens:{cb.completion_tokens}")
        print(f"Total Cost:{cb.total_cost}")