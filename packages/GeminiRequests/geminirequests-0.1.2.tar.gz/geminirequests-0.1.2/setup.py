from setuptools import setup, find_packages

setup(
    name="GeminiRequests",  # Уникальное имя вашего пакета
    version="0.1.2",  # Версия проекта
    author="Illya Lazarev",
    author_email="sbdt.israel@gmail.com",
    description="Gemini AI module (using Gemini AI API through requests lib)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Python-shik/GeminiRequests",  # URL на репозиторий или сайт проекта
    packages=find_packages(),  # Автоматический поиск пакетов
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Требуемая версия Python
    #  зависимости requirements.txt
    install_requires=[
        "requests"
    ],

)
