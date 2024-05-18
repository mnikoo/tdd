RED='\033[0;31m'
GREEN='\033[0;32m'

while true; do
    python3 -m unittest
    if [ $? -eq 0 ]; then
        echo "${GREEN}"
    else 
        echo "${RED}"
    fi

    date
    echo "*******************************"
    echo "*******************************"
    echo "*******************************"
    echo "*******************************"
    echo "*******************************"

    sleep 1
done