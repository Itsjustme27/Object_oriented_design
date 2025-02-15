class USPlug:
    def connect(self):
        print("Connected using a US plug")


class Adapter:
    def __init__(self, plug):
        self.plug = plug

    def connect(self):
        print("adapter converts the plug type")
        self.plug.connect()


def main():
    us_plug = USPlug()
    adapter = Adapter(us_plug)
    adapter.connect()

if __name__ == "__main__":
    main()
