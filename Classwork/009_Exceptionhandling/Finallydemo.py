#finally function always print thay means koi msg aapva

def test():
    try:
        a = int(input("Enter the number : "))
        return a
    except Exception as e:
        return e
    finally:
        print("Hello..program ended")
print(test())
