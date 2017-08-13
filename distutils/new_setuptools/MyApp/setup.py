from setuptools import setup, find_packages

setup(  
        name="myapp",
        version="1.0",
        description="Example using setuptools",
        author="James Fraser",
        author_email="wulfgar.pro@gmail.com",
        url="https://www.wulfgar.pro",
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'go = myapp.myapp:main'
                ]
            }
)
