class Val:
    def is_Val_name(self):
        if getattr(self,"name", None) is not None:
            if len(self.name)<2 or len(self.name)>23:
                if len(self.telefon)<9 or len(self.telefon)>13:
                    print(" erooooooorrrrrrr")
                raise  ValueError(" name must be 2 and 23 ")
            return True
        return False


