from setuptools import setup, find_packages

setup(
    name="ai-html-parse",  # Уникальное имя вашего пакета
    version="0.1.0",  # Версия проекта
    author="Illya Lazarev",
    author_email="sbdt.israel@gmail.com",
    description="AI HTML Parser",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Python-shik/ai-html-parse",  # URL на репозиторий или сайт проекта
    packages=find_packages(),  # Автоматический поиск пакетов
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Требуемая версия Python
    #  зависимости requirements.txt
    install_requires=[
        "requests",
        "bs4"
    ],

)
