# Check container exist or not, if exist then delete
docker ps -a | grep sandbox > /dev/null
if [ $? -eq 0 ];
then
    docker rm sandbox
fi

# Check image exist or not, if exist then delete
docker images | grep python_sandbox > /dev/null
if [ $? -eq 0 ];
then
    docker rmi python_sandbox
fi


# create image
docker build -t python_sandbox .

# create container 
docker run -it -v `pwd`:/code --name sandbox python_sandbox
