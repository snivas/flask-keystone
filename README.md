Steps
=====
   1) Setup Keystone
   2) Install Flask, Keystone client
   3) Execute test to issue token

Setup Keystone
=================

    $ sudo docker pull stephenhsu/keystone:9.1.0
    $ sudo docker run -d -p 5000:5000 -p 35357:35357 --name mykeystone stephenhsu/keystone:9.1.0
    $ sudo docker exec -it mykeystone bash
        copy the /root/openrc

Install Flask, Keystone client
==============================
    $ pip install Flask
    $ pip install flask-keystone==0.2

or 

     $ pip install -r requirements.txt

Execute test to issue token
==============================

    $ bash -x test/get_tokens.sh
