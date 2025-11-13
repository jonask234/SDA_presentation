#!/usr/bin/env python3
"""
Examine Hsinchu City shapefile data
"""

try:
    from dbfread import DBF

    table = DBF('Hsinchu_City.dbf', encoding='utf-8')

    print("=" * 60)
    print("FIELD NAMES:")
    print("=" * 60)
    print(table.field_names)
    print()

    print("=" * 60)
    print("FIRST 5 RECORDS:")
    print("=" * 60)
    for i, record in enumerate(table):
        if i < 5:
            print(f"\nRecord {i+1}:")
            for key, value in record.items():
                print(f"  {key}: {value}")
        else:
            break

    # Count total records
    table2 = DBF('Hsinchu_City.dbf', encoding='utf-8')
    total = sum(1 for _ in table2)
    print(f"\n\nTotal records: {total}")

except ImportError:
    print("dbfread not installed. Installing...")
    import subprocess
    subprocess.run(['pip3', 'install', 'dbfread', '-q'])
    print("Please run the script again.")
except Exception as e:
    print(f"Error: {e}")
    print("\nTrying alternative encoding...")
    try:
        table = DBF('Hsinchu_City.dbf', encoding='big5')
        print("Field names:", table.field_names)
        for i, record in enumerate(table):
            if i < 3:
                print(f"\nRecord {i+1}:", record)
    except Exception as e2:
        print(f"Alternative encoding also failed: {e2}")
