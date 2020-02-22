class Models:
    orm_types = [
        ["hasOne", "1-1"],
        ["belongsTo", "1-1 reverse ,1-n reverse "],
        ["hasMany", "1-n"],
        ["belongsToMany", "n-n , n-n reverse"]
    ]
    base = {
        "Hotel": {
            "main": [
                "id",
                "title"
            ],
            "has_properties": True,
            "has_settings": True,
            "relations": [
                {
                    "type": "hasMany",
                    "model": "Room"
                }
            ]
        },
        "Room": {
            "main": [
                "id",
                "title"
            ],
            "has_properties": True,
            "has_settings": True
        },
        "User": {
            "main": [
                "id",
                "username",
                "password"
            ],
            "has_properties": True,
            "has_settings": True
        }
    }

    relations = [
        {
            "models": [
                "Hotel",
                "Room"
            ],
            "type": "n-n",
            "main": [
            ]
        },
    ]
