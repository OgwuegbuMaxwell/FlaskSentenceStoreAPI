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



![img1](https://github.com/OgwuegbuMaxwell/FlaskSentenceStoreAPI/assets/53094485/5fc2e834-383b-4e96-999b-0368af1c1573)
![img2](https://github.com/OgwuegbuMaxwell/FlaskSentenceStoreAPI/assets/53094485/d3449ad4-29d2-48f4-a7e3-a9093edb07c3)
![img3](https://github.com/OgwuegbuMaxwell/FlaskSentenceStoreAPI/assets/53094485/8a25aed9-7f13-4bba-aec7-a2dcfe2d8b62)
![img4](https://github.com/OgwuegbuMaxwell/FlaskSentenceStoreAPI/assets/53094485/8ed0eaa4-8b37-4c5f-a887-9cb01b549e20)
![img5](https://github.com/OgwuegbuMaxwell/FlaskSentenceStoreAPI/assets/53094485/1c533895-9716-43d6-8a68-4b4858cb6b6c)




