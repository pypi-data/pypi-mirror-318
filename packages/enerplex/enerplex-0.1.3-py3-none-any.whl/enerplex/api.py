import requests
import os

from .utils import logger, download_file
from .interface import *
from datetime import datetime, timedelta
from pathlib import Path

_AUTH_TOKEN: str = None
_AUTH_EXPIRES_IN: datetime = None

class APIError(Exception):
    """
    ### Exception raised for errors returned by the API.

    Attributes:
        res (ErrorResponse): The response object containing error details.
    """
    def __init__(self, res: ErrorResponse):
        logger.critical(res.errorMessage + "\033[1;33m" + f"(api version {res.api_version})")
        super().__init__(res.errorMessage)
        self.res = res

def _interfere_errors(res: ApiResponse) -> ApiResponse:
    """
    ### Checks if the API response contains errors and raises an exception if it does.

    Args:
        res (ApiResponse): The API response object to check.

    Returns:
        ApiResponse: The original response if no errors are found.

    Raises:
        APIError: If the response indicates a failure.
    """
    if not res.successful or len(res.errorMessage) != 0:
        raise APIError(res)

    return res

def _get_auth_token(force_refresh: bool = False) -> str:
    """
    ### Retrieves an authentication token for the API.

    Args:
        force_refresh (bool): If True, forces the retrieval of a new token even if the current token is valid.

    Returns:
        str: A valid authentication token.
    """
    global _AUTH_TOKEN
    global _AUTH_EXPIRES_IN

    if _AUTH_TOKEN and (_AUTH_EXPIRES_IN - datetime.today()).seconds > 0 and not force_refresh:
        return _AUTH_TOKEN

    raw_res = requests.post(f"{os.environ.get('ENERPLEX_API_URL')}/auth/login", data={
        "name": os.environ.get("ENERPLEX_API_USER"),
        "password": os.environ.get("ENERPLEX_API_USER_PASSWORD")
    })

    print(raw_res.content)

    if not raw_res.ok:
        raise ConnectionError(raw_res.content)

    # Parse to login response
    res: LoginResponse = _interfere_errors(LoginResponse(**raw_res.json()))

    expires_in_days = int(res.expiresIn.split("d")[0])

    _AUTH_TOKEN = res.token
    _AUTH_EXPIRES_IN = datetime.now() + timedelta(days=expires_in_days)

    return res.token

def get_target_proteins() -> list[DBTargetProtein]:
    """
    ### Retrieves all target proteins stored in the database.

    Returns:
        list[DBTargetProtein]: A list of target protein objects.
    """
    headers = {"Authorization": _get_auth_token()}
    res = _interfere_errors(DataResponse(**requests.get(f"{os.environ.get('ENERPLEX_API_URL')}/data/target-proteins", headers=headers).json()))
    return [DBTargetProtein(**o) for o in res.data]

def get_ligands(protein_identifier: Union[DBTargetProtein, int, str] = None) -> list[DBProteinLigandComplex]:
    """
    ### Retrieves all stored ligands in the database. Optionally filters ligands for a specific target protein.

    Args:
        protein_identifier (Union[DBTargetProtein, int, str], optional): Specifies a target protein by object, ID, or unique name.

    Returns:
        list[DBProteinLigandComplex]: A list of ligand complex objects.
    """
    headers = {"Authorization": _get_auth_token()}
    url = f"{os.environ.get('ENERPLEX_API_URL')}/data/ligands"

    if protein_identifier:
        if isinstance(protein_identifier, str):
            url += f"?target_protein_name={protein_identifier}"
        elif isinstance(protein_identifier, int):
            url += f"?target_protein_id={protein_identifier}"
        elif isinstance(protein_identifier, DBTargetProtein):
            url += f"?target_protein_id={protein_identifier.id}"
        else:
            raise TypeError(f"Type of complex must be one of DBTargetProtein, int or string, not '{type(protein_identifier)}'.")

    res = _interfere_errors(DataResponse(**requests.get(url, headers=headers).json()))
    return [DBProteinLigandComplex(**o) for o in res.data]

def get_embeddings() -> list[DBTargetProtein]:
    """
    ### Retrieves all embeddings stored in the database.

    Returns:
        list[DBTargetProtein]: A list of embedding objects.
    """
    headers = {"Authorization": _get_auth_token()}
    res = _interfere_errors(DataResponse(**requests.get(f"{os.environ.get('ENERPLEX_API_URL')}/data/embeddings", headers=headers).json()))
    return [DBProteinLigandComplexEmbedding(**o) for o in res.data]

def download_target_protein_file(target: DBTargetProtein, path: Path, exists_ok: bool = True) -> None:
    """
    ### Downloads the file for a specific target protein.

    Args:
        target (DBTargetProtein): The target protein object.
        path (Path): The file path to save the downloaded file.
        exists_ok (bool): If False, raises an error if the file already exists.
    """
    headers = {"Authorization": _get_auth_token()}
    download_file(
        f"{os.environ.get('ENERPLEX_API_URL')}/data/target-protein/{target.id}/file",
        headers,
        path=path,
        exist_ok=exists_ok
    )

def download_ligand_file(target: DBProteinLigandComplex, path: Path, exists_ok: bool = True) -> None:
    """
    ### Downloads the file for a specific ligand complex.

    Args:
        target (DBProteinLigandComplex): The ligand complex object.
        path (Path): The file path to save the downloaded file.
        exists_ok (bool): If False, raises an error if the file already exists.
    """
    headers = {"Authorization": _get_auth_token()}
    download_file(
        f"{os.environ.get('ENERPLEX_API_URL')}/data/ligand/{target.id}/file",
        headers,
        path=path,
        exist_ok=exists_ok
    )

def download_embedding_file(target: DBProteinLigandComplexEmbedding, path: Path, exists_ok: bool = True) -> None:
    """
    ### Downloads the file for a specific embedding.

    Args:
        target (DBProteinLigandComplexEmbedding): The embedding object.
        path (Path): The file path to save the downloaded file.
        exists_ok (bool): If False, raises an error if the file already exists.
    """
    headers = {"Authorization": _get_auth_token()}
    download_file(
        f"{os.environ.get('ENERPLEX_API_URL')}/data/embedding/{target.id}/file",
        headers,
        path=path,
        exist_ok=exists_ok
    )

def upload_ligand(
    target_name: str,
    score: float,
    scoring_function: str,
    ligand_structure_file_path: Path
) -> DBProteinLigandComplex:
    """
    ### Uploads a ligand structure file to the database.

    Args:
        target_name (str): The name of the target protein.
        score (float): The docking score of the ligand.
        scoring_function (str): The scoring function used.
        ligand_structure_file_path (Path): The file path of the ligand structure file.

    Returns:
        DBProteinLigandComplex: The uploaded ligand complex object.

    Raises:
        FileNotFoundError: If the specified ligand structure file does not exist.
    """
    headers = {"Authorization": _get_auth_token()}
    data = {
        "target_name": target_name,
        "score": score,
        "scoring_function": scoring_function
    }
    files = {"ligand": open(ligand_structure_file_path, "rb")}

    if not os.path.exists(ligand_structure_file_path):
        raise FileNotFoundError(f"Ligand file {ligand_structure_file_path} not found!")

    res = _interfere_errors(DataResponse(**requests.post(f"{os.environ.get('ENERPLEX_API_URL')}/data/ligand", data=data, files=files, headers=headers).json()))
    return DBProteinLigandComplex(**res.data)
