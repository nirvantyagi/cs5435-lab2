from csv import reader

from app.models.breaches import (
    create_plaintext_breach_entry,
)

PLAINTEXT_BREACH_PATH = "app/scripts/breaches/plaintext_breach.csv"

def load_breaches(db):
    with open(PLAINTEXT_BREACH_PATH) as f:
        r = reader(f, delimiter=' ')
        header = next(r)
        assert(header[0] == 'username')
        for creds in r:
            create_plaintext_breach_entry(db, creds[0], creds[1])

    # TODO: Add logic for other types of breaches



