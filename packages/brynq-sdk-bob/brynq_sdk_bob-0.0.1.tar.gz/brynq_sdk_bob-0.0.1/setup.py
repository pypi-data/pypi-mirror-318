from setuptools import setup


setup(
    name='brynq_sdk_bob',
    version='0.0.1',
    description='Bob wrapper from BrynQ',
    long_description='Bob wrapper from BrynQ',
    author='BrynQ',
    author_email='support@brynq.com',
    packages=["brynq_sdk.bob"],
    license='BrynQ License',
    install_requires=[
        'brynq-sdk-brynq>=1',
        'pandas>=2.2.0,<3.0.0',
    ],
    zip_safe=False,
)
