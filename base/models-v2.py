class Models_v2:
    orm_types = [
        ["hasOne", "1-1"],
        ["belongsTo", "1-1 reverse ,1-n reverse "],
        ["hasMany", "1-n"],
        ["belongsToMany", "n-n , n-n reverse"]
    ]
    base = {
        "Hotel": {
            "fields": {
                "id": {"type": "unsigned int", "key": True, "extra": ["ai", "not null"]},
                "title": {"type": "str", "key": False, "extra": ["not null"], "default": ""}
                # "rooms": {"type": "hasMany", "model": "Room"}
            },
            "has_properties": True,
            "has_settings": True,
            "relations": [
                {"type": "hasMany", "model": "Room"},
                {"type": "belongsToMany", "template": "properties"},
                {"type": "belongsToMany", "template": "settings"},
                {"type": "belongsToMany", "model": "Room"},
            ]
        },
        "Room": {
            "main": [
                "id",
                "title"
            ],
            "has_properties": True,
            "has_settings": True,
            "relations": [
                {"type": "belongsTo", "model": "Hotel"},
                {"type": "belongsToMany", "template": "properties"},
                {"type": "belongsToMany", "template": "settings"},
            ]

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

    templates = {
        "properties": {
            "title": "{0}_properties",
            "fields": {
                "id": {"type": "unsigned int", "key": True, "extra": ["ai", "not null"]},
                "title": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "values": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "default_value": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "input_type": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "actions": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "locales": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "validation_rules": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "filling_rules": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "parent": {"type": "unsigned int", "key": False, "extra": ["not null"], "default": "0"},
            },
        },
        "settings": {
            "title": "{0}_settings",
            "fields": {
                "id": {"type": "unsigned int", "key": True, "extra": ["ai", "not null"]},
                "title": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "values": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "default_value": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "input_type": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "actions": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "locales": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "validation_rules": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "filling_rules": {"type": "str", "key": False, "extra": ["not null"], "default": "''"},
                "parent": {"type": "unsigned int", "key": False, "extra": ["not null"], "default": "0"},
            },
        },
        "assigned_properties": {
            "title": "{0}_assigned_properties",
            "fields": {
                "id": {"type": "unsigned int", "key": True, "extra": ["ai", "not null"]},
                "item": {"type": "unsigned int", "key": False, "extra": ["not null"]},
                "property": {"type": "unsigned int", "key": False, "extra": ["not null"]},
                "values": {"type": "str", "key": False, "extra": ["not null"], "default": "''"}
            }
        },
        "assigned_settings": {
            "title": "{0}_assigned_settings",
            "fields": {
                "id": {"type": "unsigned int", "key": True, "extra": ["ai", "not null"]},
                "item": {"type": "unsigned int", "key": False, "extra": ["not null"]},
                "property": {"type": "unsigned int", "key": False, "extra": ["not null"]},
                "values": {"type": "str", "key": False, "extra": ["not null"], "default": "''"}
            }
        },
        "general_relation": {
            "title": "{0}_{1}",
            "fields": {
                "id": {"type": "unsigned int", "key": True, "extra": ["ai", "not null"]},
                "{0}": {"type": "unsigned int", "key": False, "extra": ["not null"]},
                "{1}": {"type": "unsigned int", "key": False, "extra": ["not null"]},
            }
        }

    }
