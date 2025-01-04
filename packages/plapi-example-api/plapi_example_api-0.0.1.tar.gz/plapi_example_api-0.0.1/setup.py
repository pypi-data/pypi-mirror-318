from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='plapi-example-api',  # Unikalna nazwa pakietu na PyPI
    version='0.0.1',  # Wersja pakietu
    author='Jakub Pawłowski',  # Twoje imię i nazwisko
    author_email='plapi.org@gmail.com',  # Twój adres e-mail
    description='A simple example package that prints Hello, World!',  # Krótki opis
    long_description=long_description,  # Szczegółowy opis (z pliku README.md)
    long_description_content_type="text/markdown",  # Typ zawartości długiego opisu
    url="https://github.com/plapi-org/example-api",  # URL do repozytorium projektu
    project_urls={  # Dodatkowe linki
        "Bug Tracker": "https://github.com/plapi-org/example-api/issues",
    },
    packages=find_packages(),  # Automatyczne wykrywanie podpakietów
    install_requires=[],  # Wymagane zależności, np. ["numpy>=1.21.0"]
    classifiers=[
        'Development Status :: 4 - Beta',  # Status rozwoju: Alpha, Beta, Production/Stable
        'Programming Language :: Python :: 3',  # Obsługiwane wersje Pythona
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',  # Licencja
        'Operating System :: OS Independent',  # Obsługiwane systemy operacyjne
        'Intended Audience :: Developers',  # Docelowa grupa odbiorców
        'Topic :: Software Development :: Libraries :: Python Modules',  # Tematyka pakietu
    ],
    python_requires='>=3.6',  # Minimalna wersja Pythona
    keywords="example hello world package",  # Słowa kluczowe
)
