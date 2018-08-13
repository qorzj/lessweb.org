tar czf lessweb_org.tar.gz start.py build.sh lessweb_org/ data/ static/ test/
docker-compose -p armstrong -f docker/production/docker-compose.yml up -d --build