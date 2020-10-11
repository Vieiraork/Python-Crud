# Python-CRUD ![Python CI](https://github.com/WilliamVie/Python-Crud/workflows/Python%20CI/badge.svg) [![license-badge]][license]
My first CRUD application using Python 3.

## Languages
![python-language-badge] ![sqlite-language-badge]

## About
This is my first CRUD application using OOP. If you willing to help us, must follow steps below:
1. Verify if the database file exists on project (this is automatically checked by [`connection::setup()`][ref-1] method)
1. Execute the batch file [`python_executor.bat`][ref-2] or via terminal type `python main.py`
1. We are using Python 3.8.2 and native SQLite version

Thanks for testing :smirk:

### Contributors
- William ~ [@WilliamVie][william-ref]
- Nádio ~ [@Devwarlt][nadio-ref]

[william-ref]: https://github.com/WilliamVie
[nadio-ref]: https://github.com/Devwarlt

[python-language-badge]: https://img.shields.io/badge/Python-3.8.3-blue?logo=python&style=plastic
[sqlite-language-badge]: https://img.shields.io/badge/SQLite-3-blue?logo=sqlite&style=plastic

[license-badge]: https://img.shields.io/badge/MIT-gray?style=plastic
[license]: /LICENSE

[ref-1]: /src/connection.py#L7
[ref-2]: /src/python_executor.bat
