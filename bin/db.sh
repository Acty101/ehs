#!/bin/bash
set -Eeuo pipefail

# Sanity check command line options
usage() {
    echo "Usage: $0 (create|destroy|reset)"
}

if [ $# -ne 1 ]; then
    usage
    exit 1
fi

# variables
DATABASE_PATH="var/ehs.sqlite3"
DB_SCHEMA="sql/schema.sql"
DB_DATA="sql/data.sql"

# functions
create() {
    if test -e "$DATABASE_PATH"; then
        echo "Error: database already exists"
        exit 1
    fi
    sqlite3 "$DATABASE_PATH" <"$DB_SCHEMA"
    sqlite3 "$DATABASE_PATH" <"$DB_DATA"
}

destroy() {
    rm -rf "$DATABASE_PATH"
}

# Parse argument $1 is the first argument
case $1 in
"create")
    create
    ;;

"destroy")
    destroy
    ;;

"reset")
    destroy
    create
    ;;

"dump")
    for table in $( (sqlite3 $DATABASE_PATH .tables) 2>/dev/null); do
        echo "Printing data from table: $table"
        sqlite3 -batch -line $DATABASE_PATH "SELECT * FROM $table"
        echo
    done
    ;;
*)
    usage
    exit 1
    ;;
esac
