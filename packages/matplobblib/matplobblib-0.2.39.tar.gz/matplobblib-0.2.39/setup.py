from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()



setup(
    name='matplobblib',
    version='0.2.39',
    packages=find_packages(),
    description='Just a library for some subjects',
    author='Ackrome',
    author_email='ivansergeyevicht@gmail.com',
    url='https://github.com/Ackrome/matplobblib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    package_data={
        "matplobblib.tvims.theory.pdfs": ["MS-11-12/*.png"],  # Include PNGs
    }
)
