export PGPASSWORD=ПАРОЛЬ
psql --host 127.0.0.1 -p 5431 -U postgres -c "DROP DATABASE swapi;"
#psql --host 127.0.0.1 -p 5431 -U postgres -c "create database swapi"