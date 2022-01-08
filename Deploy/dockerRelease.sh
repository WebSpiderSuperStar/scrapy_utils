#!/usr/bin/env sh
# Build and release docker image

## some Environment variable
dockerUser='awesomepayne'
pkgName=$(basename `pwd`)
dateTag=$(date "+%Y%m%d%H%M%S")
ImageTag=${dockerUser}/${pkgName}:${dateTag}

## build images
docker build -f Deploy/Dockerfile -t ${ImageTag} .

## release
docker push ${ImageTag}
if [[ $? == 0 ]]; then
    echo -e "Successfully published Image：\n\n\t\t ${ImageTag} \t\t\n"
else
    echo -e "Failed published Image： \n\t\t ${ImageTag} \t\t"
    exit 1;
fi

# remove residual images
#docker images | grep awesomepayne/imsilkroad | awk '{print $3}'  | xargs docker rmi -f