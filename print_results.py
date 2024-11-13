import json
from prettytable import PrettyTable

def print_results_as_table(data, column_names):
    table = PrettyTable()
    table.field_names = column_names
    table.align = "l"
    for name in column_names:
        table.max_width[name] = 50

    for row in data:
        conversion_row = []
        for item in row:
            if isinstance(item, set):
                conversion_item = ', '.join(item)
            elif isinstance(item, str):
                try:
                    json_data = json.loads(item)
                    if isinstance(json_data, list):
                        conversion_item = ', '.join(json_data)
                    else:
                        conversion_item = item
                except json.JSONDecodeError:
                    conversion_item = item
            else:
                conversion_item = item
            conversion_row.append(conversion_item)
        table.add_row(conversion_row)
    print(table)