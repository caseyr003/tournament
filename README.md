# Tournament

This project is a a Python module that uses the PostgreSQL database to keep
track of players and matches in a Swiss style game tournament.

## Built With

* [Python 2.7](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/download/)

## Prerequisites

You will need the following things properly installed on your computer:

* [Git](http://git-scm.com/)
* [Python 2.7](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/download/)
* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads)

## Installation

* run `git clone https://github.com/caseyr003/tournament.git`
* change into the project directory
* change into the vagrant directory
* run `vagrant up`
* run `vagrant ssh`

You should now be logged into your Vagrant Virtual Machine

## Running

To run the project on your Vagrant Virtual Machine follow the following steps:

* `cd /vagrant/tournament`
* `psql -f tournament.sql`
* `python tournament_test.py`

This will run the test file for the tournament project.

## License

This project is licensed under the MIT License
