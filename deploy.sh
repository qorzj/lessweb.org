mkdir -p dist && rm -rf dist/*
tar czf dist/lessweb_org.tar.gz start.py lessweb_org/ data/ static/ test/
docker-compose -p armstrong -f docker/production/docker-compose.yml up -d --build