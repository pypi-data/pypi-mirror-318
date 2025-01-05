# Zinny Web UI: A Simple Interface to Rate Films
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)

## What's the skinny on the ciné?
Zinny Web UI provides a straightforward browser-based interface for rating films using surveys from [zinny-surveys](https://github.com/RyLaney/zinny-surveys). It connects to the Zinny API to manage surveys, ratings, and more.

## Quickstart
1. Clone the repository.
2. Install the dependencies (see [SETUP.md](https://github.com/RyLaney/zinny-webui/blob/main/SETUP.md)).
3. Start the server:
   `python zinny-webui.py`
4. Access the interface at:
   `http://127.0.0.1:7219`


## Installation Details

see [SETUP.md](SETUP.md)


## Contributing
We welcome contributions! If you'd like to report an issue, suggest a feature, or contribute code, please check the [CONTRIBUTING.md](https://github.com/RyLaney/zinny-webui/blob/main/CONTRIBUTING.md) file for guidelines.


## Acknowledgements
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) for the API framework.
- [PyInstaller](https://www.pyinstaller.org/) for building executables.
- [Platypus](https://github.com/sveinbjornt/Platypus) for creating macOS app bundles.
- Special thanks to [IMDb](https://www.imdb.com) for being the standard reference for movie and TV data. While no IMDb data is used directly, title information may coincide with their dataset.
- Development sponsored by [Teus Media](https://teus.media).
