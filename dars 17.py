class Rect:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def __setattr__(self, key, value):
        if key in ("widh","height"):
            if isinstance(key,int):
                # object.__setattr__(self,key,value)
                self.__dict__[key]=value
            else:
                raise TypeError
        else:
            raise AttributeError

    def info(self):
        return f"Rect object width:{self.width}, height:{self.width}"
rect1=Rect(width=15,height=12)
print(rect1.info())