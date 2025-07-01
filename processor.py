# processor.py-数据展开与排序处理

import pandas as pd
from typing import List
from models import Course
from config import WEEKDAY_MAP, WEEKDAY_ORDER


def expand_courses_to_rows(courses: List[Course]):
    rows = []

    for course in courses:
        regular_lesson = course.regular_lesson
        for day in regular_lesson.weekday:
            date_cn = WEEKDAY_MAP.get(day, day)
            rows.append({
                "日期": date_cn,
                "姓名": course.name,
                "课程类型": "正课",
                "时间": f"{regular_lesson.start_time}-{regular_lesson.end_time}",
                "备注": regular_lesson.remark or ""
            })

        anti_forget_session = course.anti_forget_session
        if anti_forget_session:
            for day in anti_forget_session.weekday:
                date_cn = WEEKDAY_MAP.get(day, day)
                rows.append({
                    "日期": date_cn,
                    "姓名": course.name,
                    "课程类型": "抗遗忘",
                    "时间": anti_forget_session.start_time,
                    "备注": anti_forget_session.remark or ""
                })

    return rows


def sort_dataframe(df):
    def extract_start_time(row):
        if row['课程类型'] == '正课':
            return pd.to_datetime(row['时间'].split('-')[0], format='%H:%M')
        else:
            return pd.to_datetime(row['时间'], format='%H:%M')

    df['开始时间排序'] = df.apply(extract_start_time, axis=1)
    df['星期序号'] = df['日期'].map(WEEKDAY_ORDER).fillna(len(WEEKDAY_ORDER)).astype(int)
    df = df.sort_values(by=['星期序号', '开始时间排序']).drop(columns=['星期序号', '开始时间排序'])
    return df