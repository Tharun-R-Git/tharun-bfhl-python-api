from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import re


app = FastAPI(title="API CHALLENGE")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


FULL_NAME = "r tharun"          
DOB_DDMMYYYY = "06012005"       
EMAIL = "tharunofficial2022@gmail.com"
ROLL_NUMBER = "22BCE0634"

USER_ID = f"{FULL_NAME}_{DOB_DDMMYYYY}"

INT_PATTERN = re.compile(r"^-?\d+$")


class InputPayload(BaseModel):
    data: List[str] = Field(..., description="Process Input")


def is_integer_string(s: str) -> bool:
    return bool(INT_PATTERN.match(s))


def build_concat_string_alpha(chars_in_order: List[str]) -> str:
    rev = list(reversed(chars_in_order))
    out = []
    for i, ch in enumerate(rev):
        out.append(ch.upper() if i % 2 == 0 else ch.lower())
    return "".join(out)


@app.post("/bfhl", tags=["bfhl"])
def bfhl(payload: InputPayload) -> Dict[str, Any]:
    try:
        even_numbers: List[str] = []
        odd_numbers: List[str] = []
        alphabets: List[str] = []
        special_characters: List[str] = []
        alpha_chars_flat: List[str] = []
        total = 0

        for token in payload.data:
            if is_integer_string(token):
                n = int(token)
                total += n
                if n % 2 == 0:
                    even_numbers.append(str(token))  # ensure string
                else:
                    odd_numbers.append(str(token))
                continue

            if token.isalpha():
                alphabets.append(token.upper())
                for ch in token:
                    if ch.isalpha():
                        alpha_chars_flat.append(ch)
                continue

            special_characters.append(token)
            for ch in token:
                if ch.isalpha():
                    alpha_chars_flat.append(ch)

        return {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total),
            "concat_string": build_concat_string_alpha(alpha_chars_flat),
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "is_success": False,
                "error": "Bad Request",
                "message": str(e),
            },
        )


