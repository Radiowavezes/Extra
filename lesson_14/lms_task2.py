def stop_words(words: list):
    def wrapping(func):
        def decorating(*args, **kwargs):
            result = []
            for word in (func(*args, **kwargs)[:-1]).split():
                if word in words:
                    result.append('*')
                else:
                    result.append(word)
            result[-1] += (func(*args, **kwargs)[-1])
            return ' '.join(result)
        return decorating
    return wrapping
                    
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('Ana'))
