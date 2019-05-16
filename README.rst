Electrum-OMNI Lightweight Bitcoin & OMNI client
=================================================

::

  Licence: MIT Licence
  Author: Thomas Voegtlin
  Language: Python (>= 3.6)


.. image:: https://travis-ci.org/spesmilo/electrum.svg?branch=master
    :target: https://travis-ci.org/spesmilo/electrum
    :alt: Build Status
.. image:: https://coveralls.io/repos/github/spesmilo/electrum/badge.svg?branch=master
    :target: https://coveralls.io/github/spesmilo/electrum?branch=master
    :alt: Test coverage statistics
.. image:: https://d322cqt584bo4o.cloudfront.net/electrum/localized.svg
    :target: https://crowdin.com/project/electrum
    :alt: Help translate Electrum online



Getting started
===============
To use this wallet you need have access to the OMNI node. After new wallet initalisation electrum node access credentials
should be added to wallet settings (Preferences->OMNI->Daemon Url). Example: http://username:password@IP:port/.
This is a pure python application. If you want to use the
Qt interface, install the Qt dependencies::

    sudo apt-get install python3-pyqt5

As Python 3.6 (or greater) is required for Electrum-OMNI, then PIP is already installed with Python by default. 
If your faced any troubles with PIP, please follow https://www.makeuseof.com/tag/install-pip-for-python/

To install electrum-omni on your PC first check out the code from GitHub::

    git clone git://github.com/xbis/electrum-omni.git
    cd electrum-omni

Run install::

    python3 -m pip install .[fast]

This will download and install the Python dependencies used by
Electrum.
The 'fast' extra contains some optional dependencies that we think
are often useful but they are not strictly needed.

Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    protoc --proto_path=electrum --python_out=electrum electrum/paymentrequest.proto

To run Electrum from its root directory, just do::

    ./run_electrum





