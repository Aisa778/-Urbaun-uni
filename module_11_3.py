
from pprint import pprint
about={}
class Domzadanie():
    def __init__(self):
        self.grig=145




def introspection_info(args):
    k=0
    for i in range(args):
        k+=i
    return k


number_info_2 = Domzadanie()
number_info = introspection_info(42)
print(number_info)
# print(int(number_info_2))
# print(introspection_info.__name__)


# ab_1=type(number_info)
# print(type(introspection_info))
# print(dir(number_info))

about = {'type':type(number_info), 'attributes':hasattr(number_info, 'k'), 'metod':dir(number_info) }
print(about)
print(getattr(number_info_2,'grig'))
