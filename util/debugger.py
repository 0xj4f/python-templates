from array import array
import imp
import requests

def request_model(item):
    print(f"request_model: {item}") 

    print(f"URL : {item.url}")
    print(f"Headers : {item.headers}")
    print(f"Status: {item.status_code}")
    print(f"Text: {item.text}")
    print(f"Reason : {item.reason}")
    print(f"Content: {item.content}")
    """ 
    These are the response model
    r.apparent_encoding      r.encoding               r.iter_content(          r.ok                     r.status_code
    r.close(                 r.headers                r.iter_lines(            r.raise_for_status(      r.text
    r.content                r.history                r.json(                  r.raw                    r.url
    r.cookies                r.is_permanent_redirect  r.links                  r.reason                 
    r.elapsed                r.is_redirect            r.next                   r.request   
    """
    return

def dictionary_verbose(item):
    print(f"Dictionary: {item}")
    print(f"Length: {len(item)}")
    print(f"Keys: \n{item.keys()}")
    print(f"Values: \n{item.values()}")
    return 


def array_verbose(item):
    print(f"Array length: {len(item)}")
    pass

def string_verbose(item):
    pass

def debugger(item):

    print(f"\n [+] Variable: {item}")
    print(type(item))
    if isinstance(item, requests.models.Response): request_model(item)
    if isinstance(item, dict): dictionary_verbose(item)
    if isinstance(item, str): string_verbose(item)
    if isinstance(item, array): array_verbose(item)