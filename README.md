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

