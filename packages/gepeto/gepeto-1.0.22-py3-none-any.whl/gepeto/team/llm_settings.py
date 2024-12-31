import litellm
from litellm.integrations.custom_logger import CustomLogger
from litellm import completion, acompletion


from dotenv import load_dotenv
load_dotenv()

class MyCustomHandler(CustomLogger):
    def log_pre_api_call(self, model, messages, kwargs): 
        print(f"###Pre-API Call:")
        print(f"Model: {model}")
        print(f"Messages: {messages}")
        print(f"Kwargs: {kwargs}")
    
    def log_post_api_call(self, kwargs, response_obj, start_time, end_time): 
        print(f"###Post-API Call:")
        print(f"Kwargs: {kwargs}")
        print(f"Response: {response_obj}")
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
    
    def log_stream_event(self, kwargs, response_obj, start_time, end_time):
        print(f"On Stream")
        
    def log_success_event(self, kwargs, response_obj, start_time, end_time): 
        print(f"###On Success")
        print(f"Kwargs: {kwargs}")
        print(f"Response: {response_obj}")
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")

    def log_failure_event(self, kwargs, response_obj, start_time, end_time): 
        print(f"On Failure")
    
    #### ASYNC #### - for acompletion/aembeddings
    
    async def async_log_stream_event(self, kwargs, response_obj, start_time, end_time):
        print(f"On Async Streaming")

    async def async_log_success_event(self, kwargs, response_obj, start_time, end_time):
        print(f"On Async Success")

    async def async_log_failure_event(self, kwargs, response_obj, start_time, end_time):
        print(f"On Async Failure")

customHandler = MyCustomHandler()

litellm.callbacks = [customHandler]

## sync 
response = completion(model="gpt-4o", messages=[{ "role": "user", "content": "Hi 👋 - i'm openai"}])
print(response)


## async
import asyncio 

async def completion():
    response = await acompletion(model="gpt-3.5-turbo", messages=[{ "role": "user", "content": "Hi 👋 - i'm openai"}],
                              stream=True)
    async for chunk in response: 
        continue
# asyncio.run(completion())