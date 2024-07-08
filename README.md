# Mars Rover Simulator

The Mars Rover Simulator is a web-based application that allows users to control a simulated Mars rover on a 5x5 grid. Users can send commands to the rover to move it around the grid, turn it left or right, and report its current position and facing direction. The project is built using Flask for the backend and React for the frontend.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Commands](#commands)
  - [Example Command Sequence](#example-command-sequence)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features
- Place the rover on a 5x5 grid.
- Move the rover forward in the direction it is facing.
- Rotate the rover 90 degrees to the left or right.
- Report the current position and facing direction of the rover.
- User-friendly web interface to input commands and visualize the rover's position.

## Installation

### Prerequisites
- Python 3.x
- Node.js and npm

### Backend Setup

```bash
cd mars-rover-simulator
```
Create a virtual environment and activate it:

```bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install the required Python packages:

```bash
Copy code
pip install -r requirements.txt
```
Run the Flask app:

```bash
Copy code
python app.py
```
Frontend Setup
Navigate to the frontend directory:

```bash
Copy code
cd frontend
```
Install the required npm packages:

```bash
Copy code
npm install
```
Build the React app:

```bash
Copy code
npm run build
```
Start the React app:

```bash
Copy code
npm start
```
Usage
Open your web browser and navigate to http://localhost:3000.
Use the command input box to enter commands to control the Mars Rover.
The grid will display the rover's position and facing direction.

API Endpoints
POST /command
Description: Send a command to control the Mars Rover.

Request Body:

```json
{
  "command": "PLACE 1,2,EAST"
}
```
Responses:
```
200 OK # if the command is successfully executed.
400 Bad Request # if there is an error in the command.
```
Commands
```
PLACE X,Y,FACING: Place the rover on the grid at position (X, Y) facing direction FACING (NORTH, EAST, SOUTH, WEST).
MOVE: Move the rover one grid unit forward in the direction it is facing.
LEFT: Rotate the rover 90 degrees to the left.
RIGHT: Rotate the rover 90 degrees to the right.
REPORT: Display the current position and facing direction of the rover.
```
Example Command Sequence
```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```

Project Structure
```
Copy code
mars-rover-simulator/
│
├── app.py               # Flask backend application
├── requirements.txt     # Python dependencies
├── frontend/            # React frontend application
│   ├── public/
│   ├── src/
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── CommandInput.js
│   │   ├── Grid.js
│   │   └── index.js
│   ├── package.json
│   └── package-lock.json
├── README.md            # Project readme
└── .gitignore           # Git ignore file
```
Technologies Used
Backend: Flask, Python
Frontend: React, JavaScript, CSS
Others: Flask-CORS, HTML

## Application Screenshots

![Screenshot (108)](https://github.com/varun1299/mars-rover-backend/assets/56631564/2e66e408-bdc1-454b-b8d0-124e05d7a20a)
![Screenshot (109)](https://github.com/varun1299/mars-rover-backend/assets/56631564/831ff12d-23f8-4679-a2ba-e76b375c6fcb)
![Screenshot (110)](https://github.com/varun1299/mars-rover-backend/assets/56631564/fe4090ca-b718-4b7e-af50-d24aa897d168)
![Screenshot (111)](https://github.com/varun1299/mars-rover-backend/assets/56631564/96bcdf2f-1a74-4388-9d81-fe3bcd3da684)
![Screenshot (112)](https://github.com/varun1299/mars-rover-backend/assets/56631564/151e05c1-aeec-4c63-8abe-48b14e913400)
![Screenshot (113)](https://github.com/varun1299/mars-rover-backend/assets/56631564/2e1e2c17-894c-4cd3-a7bd-ea937a02df80)
![Screenshot (114)](https://github.com/varun1299/mars-rover-backend/assets/56631564/03eada87-3d4a-4df9-bc46-7ec9298caf82)
![Screenshot (115)](https://github.com/varun1299/mars-rover-backend/assets/56631564/1b43ed0d-e2a1-4c90-a981-38d0cd7c1bd9)

