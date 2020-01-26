from ..models import Department


def run(*args):
    departaments = Department.objecs.all()
    departaments.delete()
