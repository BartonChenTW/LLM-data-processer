
from typing import List, Dict, Any
import os
from pydantic import BaseModel, Field

from langchain_core.exceptions import OutputParserException

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

class InfoExtractor():
    def __init__(self, api_provider: str='google', model: str='gemini-2.5-flash', path_env: str=''):

        self.DataSchema = None  # Placeholder for the Pydantic model
        
        if api_provider == 'google':
            llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.0
        )
        else:
            raise ValueError(f"Unsupported API provider: {api_provider}")
        
        self.llm = llm


    def load_data_schema(self, schema_data: Dict[str, Any]) -> BaseModel:
        """
        Dynamically creates a Pydantic model based on the provided schema data.
        """

        # Dynamically build the fields dictionary
        fields = {}
        for field_name, field_info in schema_data['fields'].items():
            field_type = eval(field_info['field_type'])
            field_description = field_info['description']
            fields[field_name] = (field_type, Field(description=field_description))

        # Create the Pydantic model dynamically
        self.DataSchema = type(schema_data['tech_type'], (BaseModel,), {
            '__annotations__': {k: v[0] for k, v in fields.items()},
            **{k: v[1] for k, v in fields.items()},
            '__doc__': "Schema for a storage technology."
        })

        self.parser = JsonOutputParser(pydantic_object=self.DataSchema)
    

    def load_prompt_templates(self, base_prompt_dict: Dict[str, str], fix_prompt_dict: Dict[str, str]):
        """
        Load prompt templates from provided dictionaries.
        """
        # Create ChatPromptTemplate from dictionaries
        self.base_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", base_prompt_dict["system"]),
                ("human", base_prompt_dict["human"]),
            ]
        )

        self.fix_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", fix_prompt_dict["system"]),
                ("human", fix_prompt_dict["human"]),
            ]
        )


    def load_info_source(self, technology_name: str, info_source: str):
        """
        Load the information source to be used in prompts.
        """
        self.technology_name = technology_name
        self.info_source = info_source


    def validate_setup(self) -> bool:
        """
        Validates that all required components are set up before extraction.
        
        Returns:
            bool: True if all required components are configured.
        
        Raises:
            ValueError: If any required component is missing.
        """
        errors = []
        
        if self.DataSchema is None:
            errors.append("DataSchema not loaded. Call load_data_schema() first.")
        
        if not hasattr(self, 'parser') or self.parser is None:
            errors.append("Parser not initialized. Call load_data_schema() first.")
        
        if not hasattr(self, 'base_prompt') or self.base_prompt is None:
            errors.append("Base prompt not loaded. Call load_prompt_templates() first.")
        
        if not hasattr(self, 'fix_prompt') or self.fix_prompt is None:
            errors.append("Fix prompt not loaded. Call load_prompt_templates() first.")
        
        if not hasattr(self, 'technology_name') or not self.technology_name:
            errors.append("Technology name not set. Call load_info_source() first.")
        
        if not hasattr(self, 'info_source') or not self.info_source:
            errors.append("Info source not set. Call load_info_source() first.")
        
        if errors:
            raise ValueError("Setup validation failed:\n" + "\n".join(f"- {err}" for err in errors))
        
        return True
   

    def extract_tech_info(self, max_retries:int=3) -> BaseModel:
        """
        Attempts to get a valid Pydantic object from the LLM, retrying up to 
        max_retries times if the JSON parsing fails.
        """

        # check if all condition are met before extract information
        if not self.validate_setup():
            return None

        print(f"Attempting to generate technology description for: **{self.technology_name}**")
        
        # 1. First Attempt - Use the base generation chain
        base_chain = self.base_prompt | self.llm 
        
        # Get the LLM's initial response (potentially malformed JSON string)
        initial_response = base_chain.invoke({
            "technology_name": self.technology_name, 
            "info_source": self.info_source,
            "format_instructions": self.parser.get_format_instructions()
        })
        json_output = initial_response.content

        print(f"Initial JSON Output:\n{json_output}")

        
        # 2. Start the Retry Loop
        for attempt in range(max_retries):
            try:
                # Attempt to parse the JSON using the Pydantic parser
                print(f"\n✅ Attempt {attempt + 1}: Parsing successful!")
                return self.parser.parse(json_output)
            
            except OutputParserException as e:
                # If parsing fails, proceed to fixing mechanism
                if attempt >= max_retries - 1:
                    # Last attempt failed, raise error
                    raise OutputParserException(f"Failed to parse output after {max_retries} retries.")
                
                print(f"❌ Attempt {attempt + 1}: Parsing failed (Error: {e}). Retrying with fix prompt...")
                
                # Use the fixing prompt and LLM to repair the output
                fix_chain = self.fix_prompt | self.llm
                
                fix_response = fix_chain.invoke({
                    "technology_name": self.technology_name, 
                    "format_instructions": self.parser.get_format_instructions(),
                    "malformed_output": json_output 
                })
                
                # Update json_output with the new, hopefully fixed, JSON content
                json_output = fix_response.content

                print(f"Fixed JSON Output:\n{json_output}")
        
        # Should not be reached if max_retries is hit, but included for completeness
        raise OutputParserException(f"Failed to parse output after {max_retries} retries. Last output: {json_output}")