class Token:
    value = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczMzczMzI4OSwianRpIjoiMTQxN2QwNGMtMjhjZC00ZTQyLWI4OTgtYzViMjZhNmVhMmRhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNzMzNzMzMjg5LCJleHAiOjE3MzM3MzY4ODl9.0RhdBkj1ROiQtNl0qo5Lv-leBVkeUVN_47Wl-ckIYlo"}

class Schema:
    schema_get_item = {
        "type": "object",
        "properties": {
            "description": {
                "type": "string"
            },
            "id": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            },
            "quantity": {
                "type": "integer"
            }
        },
        "required": [
            "description",
            "id",
            "name",
            "quantity"
        ]
    }