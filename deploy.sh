# Variables
IMAGE_NAME="oc-letting"
DOCKER_USERNAME="kassim93"
DOCKER_REGISTRY="${DOCKER_USERNAME}/${IMAGE_NAME}"
COMMIT_HASH=$(git rev-parse --short HEAD)
TAG="${DOCKER_REGISTRY}:${COMMIT_HASH}"
SENTRY_DSN=$1

# Construire l'image Docker
echo "Building Docker image..."
docker build -t $TAG .

# Taguer l'image avec un label distinct
echo "Tagging Docker image..."
docker tag $TAG $DOCKER_REGISTRY:latest

# Pousser l'image vers Docker Hub
echo "Pushing Docker image to Docker Hub..."
docker push $TAG
docker push $DOCKER_REGISTRY:latest

# Lancer le conteneur localement
echo "Running Docker container..."
docker run -d -p 8000:8000 $TAG -e SENTRY_DSN=$SENTRY_DSN $TAG
