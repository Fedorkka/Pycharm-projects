from cx_Freeze import setup, Executable

setup(
    name = "Устный Счет",
    version = "0.2",
    description = "Пасхалка от Федорки a.k. BigDady",
    executables = [Executable("ust.py")])
