from uuid import UUID
from urllib.parse import urljoin
from typing import List, Union

from talk2data_sdk.database.database import DatabaseInfo, Database
from talk2data_sdk.logging import logger
from talk2data_sdk.constants import AUTH_TOKEN_HEADER, AUTH_EMAIL_HEADER, BIOTURING_API_USER
from talk2data_sdk.utils import requests


class Talk2DataConnector:
  """
  A class to connect to the Talk2Data server.
  """

  def __init__(
      self,
      base_url: str,
      token: str,
      *,
      http_user_name: str = None,
      http_password: str = None,
  ) -> None:
    self._base_url = base_url
    self._token = token
    if http_user_name is not None and http_password is not None:
      self._http_auth = (http_user_name, http_password)
    else:
      self._http_auth = None

  # ------------ #
  # Private APIs #
  # ------------ #

  def _get_url(self, route: str) -> str:
    assert not route.startswith("/")
    return urljoin(self._base_url, route)

  def _test_connection(self):
    self.post("api/v1/version/list", None)

  # ------------ #
  # Public APIs  #
  # ------------ #

  @property
  def base_url(self) -> str:
    """
    The base URL of the server.
    """
    return self._base_url

  @property
  def token(self) -> str:
    """
    The authentication token.
    """
    return self._token

  def post(
      self, route: str, data: dict, *, headers: dict = None
  ) -> Union[list, dict]:
    url = self._get_url(route)
    return requests.post(
        url,
        json=data,
        headers={
            AUTH_TOKEN_HEADER: self._token,
            AUTH_EMAIL_HEADER: BIOTURING_API_USER,
            **(headers or {}),
        },
        auth=self._http_auth,
    )

  def test_connection(self):
    """
    Test the connection to the base URL.
    """
    try:
      self._test_connection()
      logger.info("Connection to %s successful", self.base_url)
    except Exception as e:
      logger.error("Connection to %s failed", self.base_url)
      raise e

  def list_databases(self) -> List[DatabaseInfo]:
    """
    List all databases available to the user.
    """
    return [
        DatabaseInfo.model_validate(x)
        for x in self.post("api/v1/version/list", None)
    ]

  def get_database(self, database_id: str) -> Database:
    """
    Get a database by its ID.

    Parameters
    ----------
    database_id : `str`
      The ID of the database.

    Returns
    -------
    database : `Database`
      The database object.
    """
    databases = self.list_databases()
    database_id = UUID(database_id)
    if database_id not in [x.id for x in databases]:
      raise ValueError(f"Database not found: {database_id}")
    info = next(x for x in databases if x.id == database_id)
    return Database(self, info)
