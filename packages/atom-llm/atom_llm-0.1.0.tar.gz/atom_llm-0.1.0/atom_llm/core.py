from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, field_validator
import inspect
from functools import wraps


def atom(llm, validator=None, is_async=False):
    def decorator(func):
        function_name = func.__name__
        docstring = func.__doc__
        signature = inspect.signature(func)

        output_modal = signature.return_annotation
        if output_modal is inspect.Signature.empty:
            raise ValueError(f"The function '{func.__name__}' must have a return type annotation.")

        prompts = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You will act as a Python function and return output in valid JSON matching the schema.",
                ),
                (
                    "user",
                    f"""
                    Function name: {function_name}
                    Docstring: {docstring}
                    Signature: {signature}

                    Use the docstring for understanding the function. Take inputs as described.
                    Return output in valid JSON matching the return type’s schema.
                    """,
                ),
                ("user", "Call the function with: {arguments}"),
            ]
        )

        structured_llm = llm.with_structured_output(output_modal)
        chain = prompts | structured_llm

        @wraps(func)
        def wrapper(*args, **kwargs):
            # map args to kwargs with signature
            bound_args = signature.bind(*args, **kwargs)
            bound_args.apply_defaults()

            inputs = bound_args.arguments
            response = chain.invoke({"arguments": str(inputs)})
            if validator:
                response = validator(inputs, response)
            return response

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            bound_args = signature.bind(*args, **kwargs)
            bound_args.apply_defaults()

            inputs = bound_args.arguments
            response = await chain.ainvoke({"arguments": str(inputs)})
            if validator:
                response = validator(inputs, response)
            return response

        return async_wrapper if is_async else wrapper

    return decorator
