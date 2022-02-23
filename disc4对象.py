class Student:

    max_slip_days = 3  # this is a class variable

    def __init__(self, name, staff):
        self.name = name  # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_slip_days(self, student, days):
        student.max_slip_days = days  #创造一个与类变量同名的实例变量


#q1
callahan = Professor("Callahan")
elle = Student("Elle", callahan)
#ans: Added Elle

#q2
elle.visit_office_hours(callahan)
#ans:understanding == 1
#Thanks,Callahan

#q3
elle.visit_office_hours(Professor("Paulette"))
#ans:understanding == 2
#Thanks,Paulette

#q4
elle.understanding
#ans:2

#q5
[name for name in callahan.students]
#ans: Callahan  Paulette ,this is a error
#right ans: ['Eile']

#q6
x = Student("Vivian", Professor("Stromwell")).name
#ans: Added Vivian
#understanding == 3

#q7
x
#ans:Vivian

#q8
[name for name in callahan.students]
#ans: Callahan  Paulette,Stromwell
#right ans: ['Eile']

#q9
elle.max_slip_days
#ans: 3

#q10
callahan.grant_more_slip_days(elle, 7)
elle.max_slip_days
#ans:7

#q11
print(Student.max_slip_days)
#ans:7


class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0


"""
我们想创建一个Keyboard类,它接受任意数量的buttons并将这些buttons存储在字典中。 
字典中的键表示Keyboard上位置的整数,值将是相应的buttons。 
根据每个描述填写Keyboard类中的方法,使用文档测试作为Keyboard行为的参考。
"""


class Keyboard:
    """Keyboard接受任意数量的buttons,并且有一个位置字典作为键,值作为buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        i = 0
        for arg in args:
            self.buttons[arg.pos] = arg

    def press(self, info):
        """获取按下button的位置,并返回该button的输出."""
        if info in self.buttons:
            self.buttons[info].times_pressed += 1
            return self.buttons[info].key
        return ''

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        str1 = ''
        for _ in typing_input:
            str1 += self.buttons[_].key
            self.buttons[_].times_pressed += 1
        return str1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
