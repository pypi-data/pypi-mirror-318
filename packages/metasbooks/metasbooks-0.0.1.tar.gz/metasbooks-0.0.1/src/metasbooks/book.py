import locale
import html
from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel, field_validator, Field


class Book(BaseModel):
    ean: int
    titre: str
    auteur: str
    editeur: Optional[str] = None
    collection: Optional[str] = None
    format: Optional[str] = None
    presentation: Optional[str] = None
    publication_date: Optional[date] = Field(None, alias="date")
    nbpages: Optional[int] = None
    poids: Optional[float] = None
    largeur: Optional[float] = None
    hauteur: Optional[float] = None
    epaisseur: Optional[float] = None
    image_url: Optional[str] = None
    resume_final: Optional[str] = None
    note: Optional[str] = None
    num_serie: Optional[int] = None
    serie: Optional[str] = None
    classification: Optional[str] = None
    code_classification: Optional[str] = None
    prix: Optional[float] = None
    lectures_associes: Optional[str] = None
    a_propos_de_l_auteur: Optional[str] = None
    buzzer: Optional[int] = None

    @field_validator("publication_date", mode="before")
    def reformat_date(cls, v) -> Optional[date]:
        if not v.strip():
            return None
        locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
        try:
            parsed_date = datetime.strptime(v.strip(), "%d %B %Y")
            locale.setlocale(locale.LC_TIME, "")
            return parsed_date.date()
        except ValueError:
            # Reset locale
            locale.setlocale(locale.LC_TIME, "")
            return None

    @field_validator(
        *(
            "editeur",
            "collection",
            "format",
            "presentation",
            "image_url",
            "resume_final",
            "note",
            "serie",
            "classification",
            "code_classification",
        ),
        mode="before",
    )
    def reformat_nullable_str(cls, v) -> Optional[str]:
        if not v.strip():
            return None
        return html.unescape(v.strip())

    @field_validator(*("titre", "auteur"), mode="before")
    def reformat_str(cls, v) -> str:
        return html.unescape(v.strip())

    @field_validator(
        *("poids", "largeur", "hauteur", "epaisseur", "prix"), mode="before"
    )
    def reformat_float(cls, v) -> Optional[float]:
        if not v.strip():
            return None
        try:
            return float(v.replace(",", ".").strip())
        except ValueError:
            return None

    @field_validator(*("num_serie", "nbpages"), mode="before")
    def reformat_int(cls, v) -> Optional[int]:
        if not v.strip():
            return None
        try:
            return int(v.strip())
        except ValueError:
            return None

    def __repr__(self):
        return f"<Book(ean={self.ean}, titre='{self.titre}', auteur='{self.auteur}')>"
