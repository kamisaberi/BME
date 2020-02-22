class Tables:
    backends = {
        "tables": {
            "hotels": {
                "title": "hotels",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "rooms": {
                "title": "rooms",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "applications": {
                "title": "applications",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "restaurants": {
                "title": "restaurants",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "news": {
                "title": "news",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "messages": {
                "title": "messages",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "comments": {
                "title": "comments",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "complaints": {
                "title": "complaints",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "ratings": {
                "title": "ratings",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "medias": {
                "title": "medias",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "reserves": {
                "title": "reserves",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            "users": {
                "title": "users",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`username` varchar(200) NOT NULL",
                    "`password` varchar(200) NOT NULL"
                ],
                "has_property_table": False,
                "has_setting_table": False
            },
            "customers": {
                "title": "customers",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`username` varchar(200) NOT NULL",
                    "`password` varchar(200) NOT NULL"
                ],
                "has_property_table": False,
                "has_setting_table": False
            },
            "schedules": {
                "title": "schedules",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL",
                    "`type` varchar(200) NOT NULL",
                    "`value` varchar(200) NOT NULL"
                ],
                "has_property_table": False,
                "has_setting_table": False
            },
            "triggers": {
                "title": "triggers",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL",
                    "`type` varchar(200) NOT NULL",
                    "`value` varchar(200) NOT NULL"
                ],
                "has_property_table": False,
                "has_setting_table": False
            }
        },

        "relations": [
            {
                "tables": [
                    "hotels",
                    "rooms"
                ],
                "template": "general_relation",
                "extra_fields": [
                    "`price` int(10) NOT NULL"
                ]
            }
        ]
    }
    middleware = {
        "tables": [
            {
                "title": "routes",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL",
                    "`value` varchar(200) NOT NULL"
                ],
                "has_property_table": False,
                "has_setting_table": False
            },
            {
                "title": "websites",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            {
                "title": "galleries",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            {
                "title": "slides",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            {
                "title": "pages",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL"
                ],
                "has_property_table": True,
                "has_setting_table": True
            },
            {
                "title": "fillings",
                "fields": [
                    "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                    "`title` varchar(200) NOT NULL",
                    "`value` varchar(200) NOT NULL"
                ],
                "has_property_table": False,
                "has_setting_table": False
            }
        ],
        "relations": [
            {
                "tables": [
                    "hotels",
                    "rooms"
                ],
                "template": "general_relation",
                "extra_fields": [
                    "`price` int(10) NOT NULL"
                ]
            }
        ]
    }
