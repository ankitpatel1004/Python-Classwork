class student:
    __id = 10
    __name = "ankit"

    def set_id(self,id):
        self.__id = id
    
    def get_id(self):
        return self.__id

    def set_name (self,name):
        self.__name = name

    def get_name(self):
        return self.__name

st =student()
st.set_id(20)
st.set_name("bhavik")
print(st.get_id())
print(st.get_name())

