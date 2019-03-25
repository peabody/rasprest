# Simple Restart/Shutdown Utility For Raspberry Pi

## Clone this repo

```bash
git clone git@github.com:peabody/rasprest.git
```

## Setup your virtual environment

```bash
virtualenv venv
```

## Install requirements

```bash
venv/bin/pip install -r requirements.txt
```

## Add a password

```bash
echo 'mypassword' > ~/.passwd.txt
```

## Run the app

```bash
venv/bin/python rasprest.py
```

## Reboot your pi

```bash
curl http://<hostname:5000>/reboot?password=mypassword
```

## Shutdown your pi

```bash
curl http://<hostname:5000>/shutdown?password=mypassword
```