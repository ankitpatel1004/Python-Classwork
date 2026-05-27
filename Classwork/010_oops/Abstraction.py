# abstraction ma abstract class no object nai bane

from  abc import ABC,abstractmethod

class Abs(ABC):

    @abstractmethod
    def test(self):
        pass

class AbsImpl(Abs):

    def test(self):
        print("test calling")

k = AbsImpl()
k.test()
# a = Abs()
