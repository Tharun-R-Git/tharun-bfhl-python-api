#  Python API Challenge

Implements POST /bfhl per the spec:
- is_success, user_id (`{full_name_ddmmyyyy}` lowercase), email, roll_number
- odd_numbers (strings), even_numbers (strings)
- alphabets (tokens fully uppercased)
- special_characters (tokens that are neither pure ints nor pure alphabets)
- sum of numeric tokens as a string
- concat_string: reverse of all alphabetic characters (from all tokens) with alternating caps (Upper, lower, ...)

## Run locally

1) Install deps:
   pip install -r scripts/requirements.txt

2) Start server:
   python scripts/api/main.py
   # or
   uvicorn scripts.api.main:app --host 0.0.0.0 --port 8000 --reload

