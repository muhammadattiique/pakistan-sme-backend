from database import engine
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(
        text(
            "ALTER TABLE businesses ADD COLUMN has_whatsapp BOOLEAN DEFAULT 0"
        )
    )
    conn.commit()

exit()