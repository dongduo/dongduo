#!/bin/bash
set -e

# enable this option when debugging
# set -x

# helper functions
function must_run_as_root {
    if [[ $(/usr/bin/id -u) -ne 0 ]]; then
        echo "must run as root"
        exit 1
    fi
}

function get {
    local packages="$@"
    apt-get install --quiet -y $packages
}

function install_system_packages {
    local postgre=( postgresql-9.1 postgresql-client-9.1\
                    postgresql-contrib-9.1 postgresql-server-dev-9.1\
                    pgadmin3 libpq-dev )
    local system=(python-dev build-essential)
    local fun=(figlet)
    local packages=( ${postgre[@]}\
                     ${system[@]}\
                     ${fun[@]})

    for p in "${packages[@]}"
    do
        get $p
    done
}

function activate_virtualenv {
    local env_dir=$1
    local requirements=$2
    local archive_dir=$3
    mkdir -p $archive_dir
    virtualenv --no-site-packages $env_dir
    source $env_dir/bin/activate

    echo "Downloading required packages"
    pip install --quiet --download $archive_dir -r $requirements

    echo "Installing package archives"
    pip install --quiet --no-index --find-links=$archive_dir -r $requirements
}

function install_nginx {
    if ! which nginx > /dev/null 2>&1; then
        echo "Nginx not installed: fetching source and installing"
    else
        local version=$(nginx -v)
        echo "Nginx found: $version"
        return
    fi

    local baseurl=$1
    local filename=$2
    local temp_dir=$(mktemp -d)
    local extract_dir=$temp_dir/${filename%.tar.gz}

    # install required packages for http rewrite module
    get libpcre3 libpcre3-dev
    wget $baseurl/$filename --directory-prefix=$temp_dir
    tar xvzf $temp_dir/$filename -C $temp_dir
    cd $extract_dir
    ./configure --sbin-path=/usr/local/sbin --with-http_ssl_module
    make
    make install
    cd -
}

#### script start ####

# make sure sudo is used
must_run_as_root

# set up all system package requirements
install_system_packages

# install nginx
NGINX_BASEURL=http://nginx.org/download
NGINX_FILE=nginx-1.4.1.tar.gz
install_nginx $NGINX_BASEURL $NGINX_FILE

# activate virtualenv
ARCHIVE_DIR=../DongduoPythonPackages
REQUIRE_DIR=.
REQUIRE_FILE=$REQUIRE_DIR/requirements.txt
VIRTUALENV_DIR=../DongduoVirtualEnv
activate_virtualenv $VIRTUALENV_DIR $REQUIRE_FILE $ARCHIVE_DIR


# report success
figlet -f banner "Happy Coding!"
