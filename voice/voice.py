"""TO-DO: Write a description of what this XBlock is."""

from importlib.resources import files

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String, Float
import pkg_resources


class MyXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    question_text = String(default="What is your opinion on this?", scope=Scope.settings)
        # Câu trả lời từ học viên
    student_answer = String(default="", scope=Scope.user_state)

    # Điểm số của học viên (do giáo viên chấm)
    student_score = Float(default=0.0, scope=Scope.user_state)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        return files(__package__).joinpath(path).read_text(encoding="utf-8")

    def studio_view(self, context=None):
        html = self.resource_string("static/html/teacher.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/voice.css"))
        frag.add_javascript(self.resource_string("static/js/src/voice.js"))
        frag.initialize_js('MyXBlock')
        return frag

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the MyXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/voice.html")
        # context = {
        #     'question': self.question_text,
        #     'student_answer': self.student_answer,
        #     'student_score': self.student_score
        # }
        # css = self.resource_string("static/css/voice.css")
        # return html % context + "<style>" + css.decode() + "</style>"
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/voice.css"))
        frag.add_javascript(self.resource_string("static/js/src/voice.js"))
        frag.initialize_js('MyXBlock')
        return frag
 
    @XBlock.json_handler
    def save_question(self, data, suffix=''):
        self.question_text="question"
        self.save()
        return {"status": "run"}
    def save_answer(self, answer):
        """
        Phương thức để lưu câu trả lời của học viên vào hệ thống.
        """
        self.student_answer = answer
        self.save()  # Lưu lại trạng thái

    def grade_answer(self, score):
        """
        Phương thức để giáo viên chấm điểm cho câu trả lời của học viên.
        """
        self.student_score = score
        self.save()  # Lưu lại điểm số
    def is_teacher(self):
        """
        Kiểm tra xem người dùng có phải là giáo viên không.
        """
        user = self.runtime.user
        if user and 'instructor' in user.roles:
            return True
        return False
    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MyXBlock",
             """<voice/>
             """),
            ("Multiple MyXBlock",
             """<vertical_demo>
                <voice/>
                <voice/>
                <voice/>
                </vertical_demo>
             """),
        ]
