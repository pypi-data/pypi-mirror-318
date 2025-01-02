from setuptools import setup, find_packages

setup(
    name="gcmark-vault",
    version="1.0.3",
    description="A secure CLI-based password manager.",
    long_description="""
    # GCMark Vault
    
    ### Description:
    A secure CLI-based password manager that uses the Argon2 hashing algorithm and Fernet symmetric encryption.
    
    ### How to use:
    After installing the package, just call vault in your terminal:
    ```vault```
    
    """,
    long_description_content_type="text/markdown",
    author="Gileade Castro & Mark McKinney",
    packages=find_packages(),
    install_requires=[
        "keyboard==0.13.5",
        "pyperclip==1.8.2",
        "inputimeout==1.0.4",
        "cryptography==44.0.0",
        "argon2-cffi==23.1.0",
        "secrets==1.0.2",
        "pyOpenSSL==24.3.0"
    ],
    entry_points={
        "console_scripts": [
            "vault=gcmark.cli:main",
        ],
    },
)
