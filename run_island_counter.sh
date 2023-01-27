msg="In order to run island counter, parameter with valid path to *.txt file"

if [ -z $1 ]; then
    echo $msg
else
    if ! [[ $1 =~ ^.*\.txt$ ]]; then
        echo $msg
    else
        python solution.py $1
    fi
fi