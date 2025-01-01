#!/bin/bash --login

# Make bashline configurations.
set -e
RESET='\033[0m'
COLOR='\033[1;32m'
COLOR_ERR='\033[1;31m'

function msg {
    echo -e "${COLOR}$(date): $1${RESET}"
}

function msgerr {
    echo -e "${COLOR_ERR}$(date): $1${RESET}"
}

function fail {
    msgerr "Error : $?"
    exit 1
}

function mcd {
    mkdir -p "$1" || fail
    cd "$1" || fail
}

function nvm_has {
    type "$1" > /dev/null 2>&1
}

msg "Developer's environment for Flask SQLAlchemy Compat."

BASH=false
RUN_PYTHON=false
RUN_DEMO=false
DEMO_NAME=""

# Pass options from command line
for ARGUMENT in "$@"
do
    KEY=$(echo $ARGUMENT | cut -f1 -d=)
    if [[ $KEY != '--*' ]]
    then
        VALUE=$(echo $ARGUMENT | cut -f2 -d=)   
    fi
    case "$KEY" in
        --bash)         BASH=true ;;
        --python)       RUN_PYTHON=true ;;
        --demo)         RUN_DEMO=true ;;
        demo)           DEMO_NAME=${VALUE} ;;
        *)
    esac
done

# Enter the virtual environment if necessary.
if [ -s "/opt/pyvenv/bin/activate" ]; then
  source /opt/pyvenv/bin/activate  || fail
  msg "Using the venv $(which python)"
fi

if $BASH
then
    # Run bash
    exec bash --login
    exit 0
fi

if nvm_has "python"; then
    PYTHON=python
else
    if nvm_has "python3"; then
        PYTHON=python3
    else
        msgerr "Fail to find Python3 in the base image, stop the container."
        exit 1
    fi
fi

if $RUN_PYTHON
then
    # Run Python.
    msg "Run Python."
    exec ${PYTHON}
    exit 0
fi

if $RUN_DEMO
then
    # Run python demo.
    if [ "x${DEMO_NAME}" = "x" ] || [ "x${DEMO_NAME}" = "xdefault" ]; then
        msg "Run the default Flask demo app."
        ${PYTHON} usage.py || fail
    else
        msg "Run the Flask demo app: ${DEMO_NAME}"
        ${PYTHON} -m examples.${DEMO_NAME} || fail
    fi
    exit 0
fi

# Run pytests.
msg "Run unit tests."
${PYTHON} -m pytest  || fail
