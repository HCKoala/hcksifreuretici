from cx_Freeze import setup,Executable


setup(
    name="HCK|Şifre Üretici",
    version="0.1",
    description="deneme",
    executables=[Executable("pin.py")]
    )
