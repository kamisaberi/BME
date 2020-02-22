class Commands:
    sqls = {
        "database.create": "CREATE DATABASE {database_name}",
        "table.create": "CREATE TABLE {table_name} ({fields})",
        "table.add.fields": "ALTER TABLE {table_name} ADD {fields}",
        "table.get.fields": "DESCRIBE {table_name}",
        "table.show.like": "SHOW TABLES LIKE '{table_name}'",
        "table.show.all": "SHOW TABLES",
        "table.insert.single": "INSERT INTO {table_name} ({fields}) VALUES ({values})",
        "table.update.with.where": "UPDATE {table_name} SET {fields_values} WHERE {where}",
        "table.select.simple": "SELECT {fields} FROM {table_name} ",
        "table.select.with.where": "SELECT {fields} FROM {table_name} WHERE {where}",
        "table.delete.with.where": "SELECT {fields} FROM {table_name} WHERE {where}",
        "table.properties.join.assigned": "SELECT {fields} FROM {assigned_table_name} INNER JOIN {properties_table} ON {assigned_table_name}.property ={properties_table}.id"
    }
