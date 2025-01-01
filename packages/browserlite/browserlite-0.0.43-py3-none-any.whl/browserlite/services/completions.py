# ailite/model/main.py
from typing import Optional, Dict, List, Literal
from browserlite.oai import AIBrowserClient
__client = None

ModelType= Literal['chatgpt','huggingchat']

def get_client(gpu=False):
    global __client
    if __client is None:
        __client = AIBrowserClient()
    return __client


def completion(
    messages: Optional[List[Dict[str, str]]] | str = None,
    model: ModelType="chatgpt",
    system_prompt: str = "You are helpful Assistant",
    prompt: str = "",
    context: Optional[List[Dict[str, str]]] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
    stream: bool = False,
    stop: Optional[List[str]] = None,
    tools=None,
    **kwargs
):
    client = get_client(kwargs.pop('gpu',False))
    web_search = kwargs.pop('web_search',False)
    kwargs['web_search'] = web_search
    return_type = kwargs.pop('return_type',None)
    kwargs['return_type'] = return_type
    return client.chat.create(
        model=model,
        messages=messages,
        system_prompt=system_prompt,
        prompt=prompt,
        context=context,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=stream,
        stop=stop,
        tools=tools,
        **kwargs
    )



def genai(
    messages: Optional[List[Dict[str, str]]] | str = None,
    model: ModelType="chatgpt",
    system_prompt: str = "You are helpful Assistant",
    prompt: str = "",
    context: Optional[List[Dict[str, str]]] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
    stream: bool = False,
    stop: Optional[List[str]] = None,
    tools=None,
    **kwargs
):
    client = get_client(kwargs.pop('gpu',False))
    web_search = kwargs.pop('web_search',False)
    kwargs['web_search'] = web_search
    kwargs['return_type'] = 'str'
    return client.chat.create(
        model=model,
        messages=messages,
        system_prompt=system_prompt,
        prompt=prompt,
        context=context,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=stream,
        stop=stop,
        tools=tools,
        **kwargs
    )


def pp_completion(
    messages: Optional[List[Dict[str, str]]] | str = None,
    model: ModelType = "chatgpt",
    system_prompt: str = "You are helpful Assistant",
    prompt: str = "",
    context: Optional[List[Dict[str, str]]] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
    stream: bool = False,
    stop: Optional[List[str]] = None,
    tools=None,
    **kwargs
):
    client = get_client(kwargs.pop('gpu',False))
    res = client.chat.create(
        model=model,
        messages=messages,
        system_prompt=system_prompt,
        prompt=prompt,
        context=context,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True,
        stop=stop,
        tools=tools,
        **kwargs
    )
    for x in res:
        print(x.choices[0].delta.content, end="", flush=True)
