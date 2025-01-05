from setuptools import setup, find_packages

setup(
    name='GenZBot',
    version='0.6',
    author='Anurupa Karmakar',
    author_email='anurupakarmakar.dgp18@gmail.com',
    packages=find_packages(), 
    package_data={'': ['Images_list/*']},
    include_package_data=True,
    description='Chatbot making packing',
)