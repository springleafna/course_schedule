# parser.py-解析 JSON 并生成实体对象

import json
import sys
from typing import List
from models import Course, RegularLesson, AntiForgetSession


def parse_json_input() -> List[Course]:
    print("请输入课程信息的 JSON 数据（支持多行粘贴），结束请先输入Enter，再输入Ctrl+D:\n")
    json_input = sys.stdin.read()

    try:
        data = json.loads(json_input)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"❌ JSON 解析失败，请检查格式：{e}")

    courses = []
    for item in data:
        regular_lesson_data = item.get("regular_lesson")
        if not regular_lesson_data:
            continue

        regular_lesson = RegularLesson(
            weekday=regular_lesson_data["weekday"],
            start_time=regular_lesson_data["start_time"],
            end_time=regular_lesson_data["end_time"],
            remark=regular_lesson_data.get("remark")
        )

        anti_forget_data = item.get("anti_forget_session")
        anti_forget_session = None
        if anti_forget_data and anti_forget_data is not None:
            anti_forget_session = AntiForgetSession(
                weekday=anti_forget_data["weekday"],
                start_time=anti_forget_data["start_time"],
                remark=anti_forget_data.get("remark")
            )

        course = Course(
            name=item["name"],
            regular_lesson=regular_lesson,
            anti_forget_session=anti_forget_session,
            remark=item.get("remark")
        )
        courses.append(course)

    return courses