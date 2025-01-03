from enum import Enum


class Technology(str, Enum):
  SCSEQ = "scseq"


class Species(str, Enum):
  HUMAN = "human"


AUTH_TOKEN_HEADER = "bioturing-auth-token"
AUTH_EMAIL_HEADER = "bioturing-auth-email"
BIOTURING_API_USER = "api-user@bioturing.com"
REQUEST_TIME_OUT = 3600
