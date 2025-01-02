import inspect
from pydantic import create_model, ValidationError
from docstring_parser import parse
import logging
from typing import Union

logging.basicConfig(level=logging.WARNING)

def execf(func):
    # Get the function's signature
    sig = inspect.signature(func)
    # Get the function's docstring
    doc = inspect.getdoc(func)
    if not doc:
        description = "No description provided."
    else:
        parsed_doc = parse(doc)
        description = parsed_doc.short_description or "No description provided."
    
    # Get the function's name
    name = func.__name__
    
    # Create a pydantic model based on the function's parameters
    fields = {}
    for param_name, param in sig.parameters.items():
        if param.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
            raise ValueError("Functions with *args or **kwargs are not supported.")
        
        annotation = param.annotation
        if annotation == inspect.Parameter.empty:
            logging.warning(f"Parameter '{param_name}' in function '{name}' lacks an annotation. Defaulting to str.")
            annotation = str  # Default to string if no annotation
        else:
            # Handle Union and Optional types
            if getattr(annotation, '__origin__', None) is Union and type(None) in annotation.__args__:
                annotation = annotation.__args__[0]
            # Convert complex types to str
            if not isinstance(annotation, type):
                annotation = str
        
        fields[param_name] = (annotation, ...)
    
    try:
        Model = create_model(f'{name}Params', **fields)
    except ValidationError as e:
        logging.error(f"Validation error creating model for function '{name}': {e}")
        raise
    
    # Extract the schema from the pydantic model
    schema = Model.model_json_schema()
    
    # Update properties with descriptions from docstring
    param_descriptions = {param.arg_name: param.description for param in parsed_doc.params if parsed_doc.params}
    for prop_name, prop in schema.get('properties', {}).items():
        if prop_name in param_descriptions:
            prop['description'] = param_descriptions[prop_name]
        # Remove 'title' key if present
        prop.pop('title', None)
    
    # Build the desired JSON structure
    json_struct = {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {
                "type": "object",
                "properties": schema.get('properties', {}),
                "required": [param for param in sig.parameters if sig.parameters[param].default == inspect.Parameter.empty]
            }
        }
    }
    
    # Validate the JSON structure against expected format
    # (Add validation logic here if necessary)
    
    return json_struct

    
