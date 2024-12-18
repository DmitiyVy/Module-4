def test_function():
    print('Hello world!')
    def inner_function():
        print("Я в области видимости функции test_function")
    return inner_function()

test_function()
# inner_function() Вызов функции вне функции test_function невозможен, так как это имя содержится в локальном
# пространстве функции, и невозможно обращаться к локальным именам из глобального пространства. Обращаться к
# именам только из внутренних пространств