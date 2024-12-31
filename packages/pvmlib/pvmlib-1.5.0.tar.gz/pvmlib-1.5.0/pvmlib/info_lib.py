class LibraryInfo:
    version_lib = 'v1.5.0'
    name = 'pvmlib'
    author = "Jesus Lizarraga"
    author_email = "jesus.lizarragav@coppel.com"
    description = "Python library for PVM"
    python_requires = '>=3.12'
    env = 'development'
    
    install_requires = [
        "pydantic>=1.8.2,<2.0.0",
        "pytz>=2021.1",
        "circuitbreaker>=1.3.2",
        "tenacity>=8.0.1",
        "fastapi>=0.68.0",
        "motor>=2.4.0",
        "uvicorn>=0.15.0",
        "urllib3>=1.26.5,<2.0.0",
        "charset_normalizer>=2.0.0,<3.0.0"
    ]