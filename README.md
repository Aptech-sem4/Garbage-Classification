# b1. Add file
Add file model to \sources\app\models\files

# b2.Dành cho ai sử dụng docker

# Server build docker container
docker build --no-cache -t prj_sem4 .

# Run container
docker run -d --network=host -v /home/is_mpv/test_docker/test/app_test/project-test1:/sites/aptech-s4 prj_sem4

# Docker
docker exec -it container_id /bin/bash

# b2.Dành cho ai chạy trực tiếp trên máy hoặc linux

# Requirements 
- Flask==3.0.0
#pip install -U Flask
- tensorflow==2.14.0
#pip install "tensorflow<2.14" 
- pillow==8.4.0
#pip install Pillow

# Run Flask
- cd sources/
- py run.py



