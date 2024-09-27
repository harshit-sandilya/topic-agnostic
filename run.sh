docker build -t conv .
docker run --privileged -it  --net host --shm-size=2g --ulimit memlock=-1 --ulimit stack=67108864 --gpus all --name conv_instance -v $(pwd):/workspace -w /workspace  conv
docker stop sales-instance
docker rm sales-instance
docker rmi conv