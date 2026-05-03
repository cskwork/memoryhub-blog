---
title: "Aider sendchat.py Code Explained"
date: 2024-06-18T22:17:20+09:00
slug: "303-Aider-sendchat-py-Code-Explained"
original_url: "https://memoryhub.tistory.com/303"
tistory_id: 303
draft: false
categories: ["데브 유틸"]
tags: ["Aider"]
---

```
# Importing necessary modules
import hashlib  # For generating hashes
import json  # For encoding data to JSON

import backoff  # For implementing exponential backoff
import httpx  # For making HTTP requests
import openai  # For interacting with the OpenAI API

# Importing custom modules from aider package
from aider.dump import dump  # For dumping data (unused in this snippet, hence ignored)
from aider.litellm import litellm  # Custom module for language model operations

# Setting up cache path and cache variable
CACHE_PATH = "~/.aider.send.cache.v1"
CACHE = None  # Cache is initially set to None

# Function to determine if the operation should give up retrying
def should_giveup(e):
    if not hasattr(e, "status_code"):  # Check if exception has status_code attribute
        return False

    # If the exception type is one of the following, do not give up
    if type(e) in (
        httpx.ConnectError,
        httpx.RemoteProtocolError,
        httpx.ReadTimeout,
    ):
        return False

    # Otherwise, give up if _should_retry method returns False
    return not litellm._should_retry(e.status_code)

# Decorator for retrying function calls with exponential backoff
@backoff.on_exception(
    backoff.expo,  # Exponential backoff
    (
        httpx.ConnectError,
        httpx.RemoteProtocolError,
        httpx.ReadTimeout,
        litellm.exceptions.APIConnectionError,
        litellm.exceptions.APIError,
        litellm.exceptions.RateLimitError,
        litellm.exceptions.ServiceUnavailableError,
        litellm.exceptions.Timeout,
    ),
    giveup=should_giveup,  # Custom function to decide when to stop retrying
    max_time=60,  # Maximum time to keep retrying
    on_backoff=lambda details: print(
        f"{details.get('exception','Exception')}\nRetry in {details['wait']:.1f} seconds."
    ),  # Print message during backoff
)
def send_with_retries(model_name, messages, functions, stream, temperature=0):
    # Prepare the arguments for the API call
    kwargs = dict(
        model=model_name,
        messages=messages,
        temperature=temperature,
        stream=stream,
    )
    if functions is not None:
        kwargs["functions"] = functions

    # Generate a key for caching by hashing the arguments
    key = json.dumps(kwargs, sort_keys=True).encode()
    hash_object = hashlib.sha1(key)

    # Check cache if caching is enabled and streaming is not requested
    if not stream and CACHE is not None and key in CACHE:
        return hash_object, CACHE[key]

    # Call the language model API
    res = litellm.completion(**kwargs)

    # Cache the response if caching is enabled and streaming is not requested
    if not stream and CACHE is not None:
        CACHE[key] = res

    return hash_object, res

# Simplified function to send messages with retries
def simple_send_with_retries(model_name, messages):
    try:
        _hash, response = send_with_retries(
            model_name=model_name,
            messages=messages,
            functions=None,
            stream=False,
        )
        # Return the content of the first message choice
        return response.choices[0].message.content
    except (AttributeError, openai.BadRequestError):
        return
```

### Summary of Key Components and Functions

1. **Imports and Configuration**:

   - Modules like `hashlib`, `json`, `backoff`, `httpx`, and `openai` are imported.
   - Custom modules from `aider` are also imported.
   - A cache path and cache variable are set up for potential use in caching API responses.
2. **`should_giveup` Function**:

   - Determines if retries should stop based on the type of exception and its status code.
3. **`send_with_retries` Function**:

   - This function is decorated with `backoff.on_exception` to handle retries with exponential backoff.
   - It prepares the API call arguments, generates a unique key for caching, checks the cache, and calls the language model API.
   - If caching is enabled and applicable, it stores the response in the cache.
4. **`simple_send_with_retries` Function**:

   - A simplified interface for sending messages with retries.
   - Calls `send_with_retries` and handles potential exceptions to return the content of the response.

The use of caching and exponential backoff ensures efficient and reliable API interactions, especially in cases of transient errors or rate limits. The functions are designed to handle retries gracefully and provide a simple interface for sending messages to a language model API.
