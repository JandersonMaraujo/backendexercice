#!/bin/bash
###############################################
# Creating volumes for docker
###############################################
source /srv/backend-exercice/deploy/.env

mkdir -p "$BACKENDEXERCICE_VOLUME/server/certs"
mkdir -p "$BACKENDEXERCICE_VOLUME/server/logs"
mkdir -p "$BACKENDEXERCICE_VOLUME/db/data "
mkdir -p "$BACKENDEXERCICE_VOLUME/db/data_test"
mkdir -p "$BACKENDEXERCICE_VOLUME/db/encryption"
mkdir -p "$BACKENDEXERCICE_VOLUME/backendexercice/log"
mkdir -p "$BACKENDEXERCICE_VOLUME/backendexercice/media"
sudo chown -R 1000 "$BACKENDEXERCICE_VOLUME/backendexercice/log"
sudo chown -R 1000 "$BACKENDEXERCICE_VOLUME/backendexercice/media"


###############################################
# Create Encryption Key - mariadb
###############################################
if [ ! -f "$BACKENDEXERCICE_VOLUME/db/encryption/keyfile.key" ] || [ ! -f "$BACKENDEXERCICE_VOLUME/db/encryption/keyfile.enc" ]
then
    (echo -n "1;" ; openssl rand -hex 32 ) >> "$BACKENDEXERCICE_VOLUME/db/encryption/keyfile"
    openssl rand -hex 128 > "$BACKENDEXERCICE_VOLUME/db/encryption/keyfile.key"
    openssl enc -aes-256-cbc -md sha1 -pass file:$BACKENDEXERCICE_VOLUME/db/encryption/keyfile.key -in $BACKENDEXERCICE_VOLUME/db/encryption/keyfile -out $BACKENDEXERCICE_VOLUME/db/encryption/keyfile.enc
fi
###############################################
# Copying certificates
###############################################
# cp ../ci/dummy_certificate.crt $BACKENDEXERCICE_VOLUME/server/certs/certificate.crt
# cp ../ci/dummy_certificate.key $BACKENDEXERCICE_VOLUME/server/certs/certificate.key