from flask import Flask, request, Response, send_from_directory
from flask_cors import CORS
import json
import os


app = Flask(__name__, static_folder='../frontend/build')
CORS(app)  # Enable CORS for all routes


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
    

# Define a class `Rover` to encapsulate rover behavior and state

class Rover:
    DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    MOVE_DELTA = {
        'NORTH': (0, 1),
        'EAST': (1, 0),
        'SOUTH': (0, -1),
        'WEST': (-1, 0)
    }

    # Constructor (__init__) initializes the rover's state

    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None

    # Method to place the rover on the grid

    def place(self, x, y, facing):
        if facing in self.DIRECTIONS and 0 <= x < 5 and 0 <= y < 5: 
            self.x = x
            self.y = y
            self.facing = facing
            data = {"message": "Rover placed successfully"}
            return Response(json.dumps(data), status=200)
        else:
            return Response("Invalid PLACE command: Out of bounds or incorrect facing direction.", status=400)

    # Method to move the rover

    def move(self):
        if self.x is None or self.y is None or self.facing is None:
            return Response("MOVE command ignored: Rover not placed on the grid.", status=400)
        dx, dy = self.MOVE_DELTA[self.facing]
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < 5 and 0 <= new_y < 5:
            self.x = new_x
            self.y = new_y
            data = {"message": "Rover moved successfully"}
            return Response(json.dumps(data), status=200)
        else:
            return Response("Invalid MOVE command: The rover will fall off the table.", status=400)

    # Method to turn the rover left

    def left(self):
        if self.facing is not None:
            current_index = self.DIRECTIONS.index(self.facing)
            self.facing = self.DIRECTIONS[(current_index + 3) % 4] 
            data = {"message": "Rover turned LEFT successfully"}
            return Response(json.dumps(data), status=200)
        else:
            return Response("LEFT command ignored: Rover not placed on the grid.", status=400)

    # Method to turn the rover right

    def right(self):
        if self.facing is not None:
            current_index = self.DIRECTIONS.index(self.facing)
            self.facing = self.DIRECTIONS[(current_index + 1) % 4]  
            data = {"message": "Rover turned RIGHT successfully"}
            return Response(json.dumps(data), status=200)
        else:
            return Response("RIGHT command ignored: Rover not placed on the grid.", status=400)

    # Method to report the current position and direction of the rover

    def report(self):
        if self.x is not None and self.y is not None and self.facing is not None:
            data = {"x": self.x, "y": self.y, "facing": self.facing} 
            return Response(json.dumps(data), status=200)
        else:
            return Response("The rover is not on the table.", status=400)

# Create an instance of the Rover class

rover = Rover()

# Define a route in the Flask app to handle commands sent via POST

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    command = data.get('command')
    if not command:
        return Response("Command is required", status=400)

    parts = command.strip().split()

   

    if parts[0] == 'PLACE' and len(parts) == 2: 
        try:
            x, y, facing = parts[1].split(',')
            return rover.place(int(x), int(y), facing)
        except (ValueError, IndexError):
            return Response("Invalid PLACE command format. Use PLACE X,Y,FACING.", status=400)
    elif parts[0] == 'MOVE':
        return rover.move()
    elif parts[0] == 'LEFT':
        return rover.left()
    elif parts[0] == 'RIGHT':
        return rover.right()
    elif parts[0] == 'REPORT':
        return rover.report()
    else:
        return Response(f"Invalid command: {command}", status=400)

# Run the Flask application if this script is executed directly

if __name__ == '__main__':
    app.run(debug=True)
