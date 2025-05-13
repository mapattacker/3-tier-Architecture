name=${1}

docker tag 3-tier-architecture-frontend ${name}/titanic-frontend
docker tag 3-tier-architecture-backend ${name}/titanic-backend
docker tag 3-tier-architecture-model ${name}/titanic-model

docker push ${name}/titanic-frontend
docker push ${name}/titanic-backend
docker push ${name}/titanic-model