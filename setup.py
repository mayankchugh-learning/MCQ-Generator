from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.0',
    author='Mayank Chugh',
    author_email='mayankchugh.learning@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)