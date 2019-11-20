pgbackup
========

CLI for taking backup of remote PostgreSQL database either locally or to Amazon S3


Preparing the development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository : ``git clone git@github.com:m4mayank/pgbackup``
3. ``cd`` into the repository.
4. Fetch development dependancies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in the full database URL, storage driver, and the destination.

S3 Example w/ bucket name:

::

    $ pgackup postgres:mayank@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

::

    $ pgackup postgres:mayank@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

if Virtualenv is not active then:

::

    $ pipenv run make
