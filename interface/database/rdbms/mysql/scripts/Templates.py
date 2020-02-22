import mysql.connector
import json
import inflect
import os

class Templates:
    tables = {
        "properties": {
            "title": "{0}_properties",
            "fields": [
                "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                "`title` varchar(255) NOT NULL",
                "`values` varchar(2000) NOT NULL DEFAULT ''",
                "`default_value` varchar(255) NOT NULL",
                "`input_type` varchar(255) NOT NULL",
                "`actions` varchar(2000) NOT NULL DEFAULT ''",
                "`locales` varchar(4000) NOT NULL DEFAULT ''",
                "`validation_rules` varchar(2000) NOT NULL DEFAULT ''",
                "`fillation_rules` varchar(2000) NOT NULL DEFAULT 'direct'",
                "`parent` int(10) UNSIGNED NOT NULL DEFAULT 0"
            ]
        },
        "settings": {
            "title": "{0}_settings",
            "fields": [
                "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                "`title` varchar(255) NOT NULL",
                "`values` varchar(2000) NOT NULL DEFAULT ''",
                "`default_value` varchar(255) NOT NULL",
                "`input_type` varchar(255) NOT NULL",
                "`actions` varchar(2000) NOT NULL DEFAULT NULL",
                "`locales` varchar(4000) NOT NULL DEFAULT ''",
                "`validation_rules` varchar(2000) NOT NULL DEFAULT ''",
                "`fillation_rules` varchar(2000) NOT NULL DEFAULT 'direct'",
                "`parent` int(10) UNSIGNED NOT NULL DEFAULT 0"
            ]
        },
        "assigned_properties": {
            "title": "{0}_assigned_properties",
            "fields": [
                "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                "`item` int(10) NOT NULL",
                "`property` int(10) NOT NULL",
                "`value` varchar(2000) NOT NULL DEFAULT ''"
            ]
        },
        "assigned_settings": {
            "title": "{0}_assigned_settings",
            "fields": [
                "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                "`item` int(10) NOT NULL",
                "`property` int(10) NOT NULL",
                "`value` varchar(2000) NOT NULL DEFAULT ''"
            ]
        },
        "general_relation": {
            "title": "{0}_{1}",
            "fields": [
                "`id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY",
                "`{0}` int(10) NOT NULL",
                "`{1}` int(10) NOT NULL"
            ]
        }
    }
