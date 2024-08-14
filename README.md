# Pet Clinic - Microservices with FastAPI and Docker
This project implements a pet clinic system as a collection of microservices using FastAPI and Docker. Each Bounded Context (BC) is a separate FastAPI project with its own Docker container.

## Architecture
The system follows a microservices architecture with Bounded Contexts (BCs):

- Billing-BC
- Inventory-BC
- Lab-BC
- PetHealthRecord-BC
- ResourceManagement-BC (includes Client and Pet entities)

This README focuses on the ResourceManagement-BC for illustrative purposes.

## Technologies Used
- **Backend:** Python 3.x, FastAPI
- **Database:** (Example) PostgreSQL (implementation details will vary)
- **Docker:** Containerization
- **Docker Compose:** Orchestration (optional)

## Running the Project

### 1. Prerequisites:
- Install Python 3.x and pip package manager.
- Install Docker: https://www.docker.com/products/docker-desktop/

### 2. Clone the Project:
```Bash
git clone https://github.com/your-username/pet-clinic-microservices.git
```


### 3. Build Docker Images:
```Bash
cd pet-clinic-microservices
docker-compose build
```
(Alternatively, build individual BCs: docker build -t resource-management-bc:latest resource-management-bc)

### 4. Run the Services (using Docker Compose):
```Bash
docker-compose up -d
```
(Alternatively, run each BC container individually)

### 5. (Optional) Access Services:
Expose specific ports in docker-compose.yml for accessing individual BC APIs based on their configurations.

## Project Structure (Example: ResourceManagement-BC):
The project structure is based on `https://github.com/jasontaylordev/CleanArchitecture.git` and recommendation of `https://github.com/ddd-crew`
```
resource-management-bc/
├── core/  # Domain layer (entities, repositories, services)
│   ├── domain/
│   │   ├── entities/
│   │   ├── repositories/
│   │   └── services/
├── application/  # Application services and use cases
│   ├── services/
│   └── use_cases/
├── infrastructure/  # Infrastructure layer (database adapters, API endpoints)
│   ├── adapters/
│   │   └── database/
│   └── api/
│       ├── endpoints/
│       └── dependencies/
├── tests/  # Unit and integration tests
├── Dockerfile  # Docker build instructions for the BC
└── docker-compose.yml  # (Optional) Service configuration for Docker Compose
```
## Additional Notes
This is a high-level overview. Specific implementation details (database setup, API endpoints, etc.) will be found within each BC's project directory.
Consider using environment variables for configuration.
Implement robust logging and error handling.
Explore advanced topics like event sourcing and API gateways.

**This README provides a starting point for the pet clinic system. Each BC will have its own specific details and functionalities.**

Feel free to contribute or extend this project to fit your specific needs!