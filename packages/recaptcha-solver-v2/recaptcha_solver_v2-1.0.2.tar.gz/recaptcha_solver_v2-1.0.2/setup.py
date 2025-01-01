from setuptools import setup, find_packages

with open("README.md") as f:
    description = f.read()

setup(
    name='recaptcha_solver_v2',
    version='1.0.2', 
    description='A Python module to solve reCAPTCHA using audio challenges.',
    author='Mohsin',
    author_email='mohsingemoh789@yomail.edu.pl',
    url='',  # Update this with your repo URL
    packages=find_packages(),
    install_requires=[
        'pydub',
        'speechrecognition',
        'drissionpage'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
)
