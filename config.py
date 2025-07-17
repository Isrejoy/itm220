# Path to the SQLite database file
DB_PATH = "minecraft_mod.sqlite"

# Table name to interact with
TABLE_NAME = "mcmod"

# Columns to manage (excluding ID)
COLUMNS = {
    "mcmod_id": "INT(10)",
    "mcmod_name": "VARCHAR(45)",
    "create_date": "DATE",
    "author_id": "INT(10)"
}
