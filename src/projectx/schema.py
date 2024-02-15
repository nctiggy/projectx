SIM_GEN = {
    "type": "object",
    "properties": {
        "project_name": {
            "description": "Name of the project to create",
            "type": "string",
        },
        "requestor_email": {
            "description": "Email of the user to add to the project",
            "type": "string",
            "format": "email",
        },
    },
    "required": ["project_name", "requestor_email"],
    "additionalProperties": False,
}

SIM_CLEAN = {
    "type": "object",
    "properties": {
        "project_name": {
            "description": "Name of the project to create",
            "type": "string",
        }
    },
    "required": ["project_name"],
    "additionalProperties": False,
}

OPS_CREATE = {
    "type": "object",
    "properties": {
        "project_name": {
            "description": "Name of the project to create",
            "type": "string",
        },
        "requestor_email": {
            "description": "Email of the user to add to the project",
            "type": "string",
            "format": "email",
        },
    },
    "required": ["project_name", "requestor_email"],
    "additionalProperties": False,
}
