from setuptools import setup, find_packages

setup(
    name="care-sms",
    version="1.0.0",
    description="A Django package for sending SMS using multiple backends.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DraKen0009/care-sms",
    author="Prafful Sharma",
    author_email="praffulsharma1230@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "django>=3.2",
    ],
    extras_require={
        "twilio": ["twilio>=7.0.0"],
        "boto3": ["boto3>=1.17.0"],
        "messagebird": ["messagebird>=1.5.0"],
        "all": ["twilio>=7.0.0", "boto3>=1.17.0", "messagebird>=1.5.0"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
