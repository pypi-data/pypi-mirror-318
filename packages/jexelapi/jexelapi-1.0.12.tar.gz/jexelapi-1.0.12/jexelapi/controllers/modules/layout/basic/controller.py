from .db_model import {{ class_name }}_tbl
from sqlalchemy.orm import Session

def {{ table_name }}_representation(item:{{ class_name }}_tbl, db:Session):
    item_dict = item.__dict__
    return item_dict