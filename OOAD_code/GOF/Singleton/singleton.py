class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


def main():
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)

if __name__ == "__main__":
    main()
