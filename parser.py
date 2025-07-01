# parser.py-解析 JSON 并生成实体对象

import json
import sys
from typing import List
from models import Course, RegularLesson, AntiForgetSession
from ai import call_ai_api


def parse_json_input() -> List[Course]:
    print("请输入课程信息，结束请先输入Enter，再输入Ctrl+D:\n")
    course_message = sys.stdin.read()
    api_response = call_ai_api(course_message)

    # 检查API调用是否成功
    if not api_response.get("success"):
        error_info = api_response.get("error", {})
        raise RuntimeError(f"❌ AI API 调用失败: {error_info.get('message', '未知错误')}")

    # 获取API返回的结果文本
    result_text = api_response.get("result", "")

    try:
        data = json.loads(result_text)
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