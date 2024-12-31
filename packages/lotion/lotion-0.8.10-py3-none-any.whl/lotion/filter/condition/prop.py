from enum import Enum


class Prop(Enum):
    RICH_TEXT = "rich_text"
    CHECKBOX = "checkbox"
    DATE = "date"
    FILES = "files"
    # FORMULA = "formula"
    MULTI_SELECT = "multi_select"
    NUMBER = "number"
    PEOPLE = "people"
    RELATION = "relation"
    # ROLLUP = "rollup"
    SELECT = "select"
    STATUS = "status"
    # TIMESTAMP = "timestamp"
    ID = "unique_id"
    CREATED_TIME = "created_time"
    LAST_EDITED_TIME = "last_edited_time"
