# main.py

import pandas as pd
from parser import parse_json_input
from processor import expand_courses_to_rows, sort_dataframe
from exporter import export_to_excel


def main():
    try:
        courses = parse_json_input()
        rows = expand_courses_to_rows(courses)
        df = pd.DataFrame(rows)
        df = sort_dataframe(df)
        export_to_excel(df)
    except Exception as e:
        print(f"⚠️ 程序运行异常：{e}")


if __name__ == '__main__':
    main()
