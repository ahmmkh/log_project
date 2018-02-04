# Summery

this projec is a reporting tool for a database for  news website and report it in a plain text 

## installation

### Requirments

- python
- vagrant
- virtualbox
- psycopg2 `pip install psycopg2`
- [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)

### Setup

after you cloned the repo `git clone https://github.com/udacity/fullstack-nanodegree-vm fullstack`
you should `cd fullstack/vagrant` then `vagrant up` this will download an image of linux distro with all file included but you'll need to download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) ou will need to unzip this file after downloading it. The file inside is called  `newsdata.sql` . Put this file into the `vagrant` directory, which is shared with your virtual machine.
To load the data, `cd` into the vagrant directory and use the command `psql -d news -f newsdata.sql` and
  you will take the content of ths repo and add it to that folder and then run the code using `python log.py` this will generate report.txt file with reported data.
