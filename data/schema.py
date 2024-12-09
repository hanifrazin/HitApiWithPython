class Schema:
    schema_get_specific_item = {
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

    schema_list_item = {
        "type": "array",  # Data utama adalah array
        "items": {  # Elemen array
            "type": "object",  # Setiap elemen harus berupa objek
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "description": {"type": "string"},
                "quantity": {"type": "integer"}
            },
            "required": ["id", "name", "description", "quantity"],  # Properti wajib
            "additionalProperties": False  # Tidak boleh ada properti lain
        }
    }