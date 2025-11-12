### the script to using AI (LLM) helper 

from huggingface_hub import InferenceClient
from IPython.display import display, Markdown
import ipywidgets as widgets
import os


## basic parameters for LLM generation, via HuggingFace Inference API

llm_models = {
    'Llama-3.1': 'meta-llama/Llama-3.1-8B-Instruct',    # https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
    'Mistral-7B': 'mistralai/Mistral-7B-Instruct-v0.2'   # https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
}

config = {
    'max_tokens': 2000,
    'temperature': 0.7,
}

class AIHelper():
    def __init__(self, model_name: str='Mistral-7B', display_response: bool=True):

        self.client = InferenceClient(token=os.getenv("HF_TOKEN"))
        self.model_name = model_name
        self.config = config
        self.llm_models = llm_models

        self.chat_history = []
        self.guideline = []
        self.attached_data = []
        self.display_response = display_response

        print(f"Initialized AIHelper with model: {self.model_name}")

    def add_guideline(self, guideline: str):
        """Add a guideline to the chat."""
        self.guideline.append(guideline)
        print("Guideline added.")

    def attach_data(self, attached_data: str):
        """Add data to the chat."""
        self.attached_data.append(attached_data)
        print("Data added.")

    def ask(self, prompt: str, display_response=None, with_guideline=True, with_data=True, with_history=True) -> str:
        """Generate text using the specified LLM model."""

        # deal with display parameter
        if display_response is None:  display_response = self.display_response

        messages = []

        system_msg = ''

        # create data string from guideline
        if with_guideline and len(self.guideline) > 0:
            system_msg += "[Guideline Start]\n"
            system_msg += "\n\n".join(self.guideline)
            system_msg += "\n[Guideline End]"

        if with_data and len(self.attached_data) > 0:
            data_blocks = []
            for df in self.attached_data:
                data_blocks.append(f"[Data Start]\n{df.to_csv(index=False)}\n[Data End]")
            system_msg += "\n\n".join(data_blocks)

        ## add system message if exists
        if system_msg:
            messages.append({"role": "system", "content": system_msg})

        # prepare full prompt with chat history
        if with_history:
            messages.extend(self.chat_history)

        # append to chat history
        self.chat_history.append({"role": "user", "content": prompt})

        messages.append({"role": "user", "content": prompt})

        # Use chat_completion
        self.latest_messages = messages
        response = self.client.chat_completion(
            model=self.llm_models[self.model_name],
            messages=messages,
            max_tokens=self.config['max_tokens'],
            temperature=self.config['temperature']
        )

        # store prompt/response in history
        self.chat_history.append({"role": "assistant", "content": response.choices[0].message.content})

        if display_response:
            display(Markdown(response.choices[0].message.content))
        else:
            return response.choices[0].message.content
        
        
    def chat_widget(self):

        text_in = widgets.Textarea(placeholder="Ask anything...", layout={'height': '100px', 'width': '100%'})
        button = widgets.Button(description=f"Ask {self.model_name}", button_style="success")
        checkbox_guideline = widgets.Checkbox(value=True, description='Use Guideline')
        checkbox_data = widgets.Checkbox(value=True, description='Use Attached Data')
        output = widgets.Output()

        def on_ask(b):
            with output:
                output.clear_output()
                prompt = text_in.value
                if not prompt.strip():
                    return
                display(Markdown(f"**Q:** {prompt}"))
                
                # Use the ask method with checkbox values
                response = self.ask(
                    prompt=prompt,
                    display_response=False,
                    with_guideline=checkbox_guideline.value,
                    with_data=checkbox_data.value,
                    with_history=True
                )
                display(Markdown(f"**A:** {response}"))
                text_in.value = ""  # Clear the input box after asking

        button.on_click(on_ask)

        display(widgets.HBox([checkbox_guideline, checkbox_data]))
        display(text_in, button, output)



### below: the script to using AI (LLM) helper with Google Gemini 2.5 + Google Search tool
from google import genai
from google.genai import types
from IPython.display import display, Markdown


# The GoogleSearch() object tells the model it has access to the web.
grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

# Place the tool inside the GenerateContentConfig object.
config_google = types.GenerateContentConfig(
    temperature=0.3,          # lower = more focused
    top_p=0.9,
    top_k=40,
    candidate_count=1,
    max_output_tokens=2000,     # adjust (e.g. 150–400)
    tools=[grounding_tool]
)


class AIHelper_Google():
    def __init__(self, model: str='gemini-2.5-flash', path_env: str='', display_response: bool=True):

        self.client = genai.Client() 
        self.model = model
        self.config = config_google


        self.history = []
        self.display_response = display_response

    def ask(self, prompt: str, display_response=None) -> str:
        """Generate text using the specified LLM model."""

        # deal with display parameter
        if display_response is None:  display_response = self.display_response
        
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=self.config
        )

        # store prompt/response in history
        self.history.append((prompt, response.text))

        if display_response:
            display(Markdown(response.text))
        else:
            return response.text