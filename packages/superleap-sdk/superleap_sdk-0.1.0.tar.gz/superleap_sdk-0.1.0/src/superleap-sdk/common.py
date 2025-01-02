from enum import Enum

class Environment(Enum):
    """Supported environments for the Superleap client"""
    PRODUCTION = "prod"
    STAGING = "staging"
    DEVELOPMENT = "dev"
    LOCAL= "local"



# """Supported endpoints for the Superleap client"""
POLL_AUDIT_DATA = "/api/v1/org/audit_data/"
COMMIT_AUDIT_DATA_POINTER = "/api/v1/org/audit_data/pointer/commit/"

