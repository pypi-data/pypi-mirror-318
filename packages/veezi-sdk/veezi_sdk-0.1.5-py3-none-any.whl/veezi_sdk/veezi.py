from typing import List, Optional

import requests
from pydantic import BaseModel, Field
from pydantic_core import from_json

VEEZI_API_URL = "https://api.eu.veezi.com"


class Staff(BaseModel):
    id: str = Field(alias="Id")
    first_name: str = Field(alias="FirstName")
    last_name: str = Field(alias="LastName")
    role: str = Field(alias="Role")


class Film(BaseModel):
    id: str = Field(alias="Id")
    title: str = Field(alias="Title")
    short_name: str = Field(alias="ShortName")
    synopsis: str = Field(alias="Synopsis")
    genre: str = Field(alias="Genre")
    signage_text: str = Field(alias="SignageText")
    distributor: str = Field(alias="Distributor")
    opening_date: str = Field(alias="OpeningDate")
    rating: Optional[str] = Field(alias="Rating")
    status: str = Field(alias="Status")
    content: Optional[str] = Field(alias="Content")
    duration: int = Field(alias="Duration")
    display_sequence: int = Field(alias="DisplaySequence")
    national_code: Optional[str] = Field(alias="NationalCode")
    format: str = Field(alias="Format")
    is_restricted: bool = Field(alias="IsRestricted")
    people: List[Staff] = Field(alias="People")
    audio_language: Optional[str] = Field(alias="AudioLanguage")
    government_film_title: Optional[str] = Field(alias="GovernmentFilmTitle")
    film_poster_url: str = Field(alias="FilmPosterUrl")
    film_poster_thumbnail_url: str = Field(alias="FilmPosterThumbnailUrl")
    backdrop_image_url: str = Field(alias="BackdropImageUrl")
    film_trailer_url: Optional[str] = Field(alias="FilmTrailerUrl")


def _request(endpoint: str, api_token: str) -> requests.Response:
    headers = {"VeeziAccessToken": api_token}
    return requests.get(f"{VEEZI_API_URL}/{endpoint}", headers=headers)


# v1/session + {id}
def session(api_token: str):
    pass


# v1/websession
def web_session(api_token: str):
    pass


def films(api_token: str) -> List[Film]:
    response = _request("v4/film", api_token)
    films = [Film.model_validate(film) for film in from_json(response.content)]

    return films


def films_by_id(api_token: str, id: str) -> Film:
    response = _request(f"v4/film/{id}", api_token)
    film = Film.model_validate(response.content)

    return film


# v1/filmpackage + {id}
def film_packages(api_token: str):
    pass


# v1/screen + {id}
def screen(api_token: str):
    pass


# v1/site
def site(api_token: str):
    pass


# v1/attribute + {id}
def attribute(api_token: str):
    pass
