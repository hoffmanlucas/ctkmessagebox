from setuptools import setup, find_packages

setup(
    name="ctkmessagebox2",
    version="0.3.4",
    packages=find_packages(),  # Localiza todos os pacotes Python dentro do diretório
    include_package_data=True,  # Inclui arquivos como ícones (definidos em MANIFEST.in)
    description="The MessageBox package for CustomTkinter",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Lucas Hoffman",
    author_email="hoffmanlucas@gmail.com",
    url="https://github.com/hoffmanlucas/ctkmessagebox.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "customtkinter",
        "Pillow"
    ],

    project_urls={
        "Bug Tracker": "https://github.com/hoffmanlucas/ctkmessagebox/issues",
        "Source Code": "https://github.com/hoffmanlucas/ctkmessagebox",
    },
)
