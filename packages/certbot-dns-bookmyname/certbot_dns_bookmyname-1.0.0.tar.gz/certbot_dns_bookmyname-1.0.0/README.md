# certbot-dns-bookmyname

[BookMyName](https://www.bookmyname.com/) DNS Authenticator plugin for Certbot.

This plugin automates the process of completing a `dns-01` challenge by creating,
and subsequently removing, TXT records using the BookMyName DynDNS API.

## Installation

For an installation from [PyPI](https://pypi.org/project/certbot-dns-bookmyname),
a `virtualenv` is advised.

```
pip install certbot-dns-bookmyname
```

## Credentials

Create a file like `/etc/letsencrypt/bookmyname.ini` and add your BookMyName
credentials.

```
dns_bookmyname_user = changeme
dns_bookmyname_password = changeme
```

Restrict the file access to user that run `certbot`, generally `root`.

```
chown root: /etc/letsencrypt/bookmyname.ini
chmod 600 /etc/letsencrypt/bookmyname.ini
```

## Certificate request

Acquire a wildcard certificate.  
The estimate propagation time is 360 seconds, you can reduce or increase this
value with `--dns-bookmyname-propagation-seconds <seconds>`.

```
certbot certonly \
    --authenticator dns-bookmyname \
    --dns-bookmyname-propagation-seconds 720 \
    --dns-bookmyname-credentials /etc/letsencrypt/bookmyname.ini \
    --domain 'changeme.tld' \
    --domain '*.changeme.tld'
```
