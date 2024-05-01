from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)  # sensible defaults for new tasks

def test_defaults():
    '''using no parameters should invoke defaults'''
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

# to invoke pytest:
# pytest -v using_pytest.py

if __name__ == '__main__':
    tA = Task('Learn Testing', 'Deidre', False, 1)
    print(tA, type(tA))