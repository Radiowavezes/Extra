def arg_rules(type_:str, max_length: int, contains: list):
    def wrapping(func):
        def actions(uname):
            if (
                isinstance(uname, type_) and
                len(uname) <= max_length and
                all(item for item in contains if item in uname)
                ):
                return func(uname)
            else:
                return False
        return actions
    return wrapping

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('Ann'))
