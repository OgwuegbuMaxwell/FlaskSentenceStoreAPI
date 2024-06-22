### **Flask Sentence Store API**

**Introduction**
The Flask Sentence Store API allows users to register, store and retrieve sentences securely using tokens as currency. Each user receives 10 tokens upon registration which they can use to store or retrieve sentences.

**Features**

1. User registration with secure password handling.
2. Token-based operations allowing sentence storage and retrieval.
3. MongoDB for robust data handling.
4. Docker support for easy deployment and scalability.

### **Setup**

**Prerequisites**

- Docker
- Docker Compose
- Python 3.8+

**Local Deployment**

1. Clone the repository:
git clone <repository-url>

2. Navigate to the project directory:
`cd FlaskSentenceStoreAPI
`
3. Build the Docker containers:
`docker-compose up --build
`
**### Usage**

**API Endpoints**


**POST /register: Register a new user.**

- Payload: { "username": "user1", "password": "pass1" }
- Response: { "status": 200, "msg": "You have successfully signed up for the API" }

**POST /store: Store a sentence using a token.**

- Payload: { "username": "user1", "password": "pass1", "sentence": "Hello, World!" }
- Response: { "status": 200, "msg": "Sentence saved successfully!" }


**POST /tokens: Check remaining tokens.**

- Payload: { "username": "user1", "password": "pass1" }
- Response: { "status": 200, "msg": "You have X tokens remaining." }


**POST /get: Retrieve the stored sentence.**

- Payload: { "username": "user1", "password": "pass1" }
- Response: { "status": 200, "Sentence": "Hello, World!" }







