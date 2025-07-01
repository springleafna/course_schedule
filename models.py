# models.py-定义实体类

from typing import Optional

class RegularLesson:
    def __init__(
        self,
        weekday: str,
        start_time: str,
        end_time: str,
        remark: Optional[str] = None
    ):
        self.weekday = weekday
        self.start_time = start_time
        self.end_time = end_time
        self.remark = remark


class AntiForgetSession:
    def __init__(
        self,
        weekday: str,
        start_time: str,
        remark: Optional[str] = None
    ):
        self.weekday = weekday
        self.start_time = start_time
        self.remark = remark


class Course:
    def __init__(
        self,
        name: str,
        regular_lesson: RegularLesson,
        anti_forget_session: Optional[AntiForgetSession] = None,
        remark: Optional[str] = None
    ):
        self.name = name
        self.regular_lesson = regular_lesson
        self.anti_forget_session = anti_forget_session
        self.remark = remark