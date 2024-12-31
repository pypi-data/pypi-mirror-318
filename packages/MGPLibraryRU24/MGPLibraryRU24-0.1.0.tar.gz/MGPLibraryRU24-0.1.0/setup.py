from setuptools import setup, find_packages

setup(
    name="MGPLibraryRU24",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Укажите зависимости, если есть
    author="VSDragon1239",
    author_email="ваш.email@example.com",
    description="Описание вашей библиотеки",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ваш_репозиторий",  # Опционально
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
