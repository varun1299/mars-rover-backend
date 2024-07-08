import React, { useState } from 'react';
import Grid from './Grid';
import CommandInput from './CommandInput';
import './App.css';

const App = () => {
  const [rover, setRover] = useState({ x: null, y: null, facing: null });
  const [positionString, setPositionString] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const executeCommand = async (command) => {
    setErrorMessage('');
    try {
      const response = await fetch('http://localhost:5000/command', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command }),
      });

      if (response.ok) {
        const data = await response.json();
        
        // Handle specific commands that update rover position
        if (data && data.x !== undefined && data.y !== undefined && data.facing !== undefined) {
          setRover(data);
          setPositionString(`Position: (X = ${data.x}, Y = ${data.y}), Facing: ${data.facing}`);
          setSuccessMessage('');
        }

        // Handle commands that return a message
        if (data && data.message) {
          setSuccessMessage(data.message);
        }
      } else {
        const errorText = await response.text();
        setErrorMessage(errorText);
        setSuccessMessage('');
      }
    } catch (error) {
      console.error('Fetch error:', error);
      setErrorMessage('Failed to execute command. Please try again.');
      setSuccessMessage('');
    }
  };

  return (
    <div className="App">
      <div className="header">
        <h1>Mars Rover Simulator</h1>
      </div>
      <div className="content">
        <div className="instructions">
          <h2>Instructions</h2>
          <ul>
            <li>Use the following commands to control the Mars Rover:</li>
            <ul>
              <li>
                <strong>PLACE X,Y,FACING</strong> - Place the rover on the grid at position (X, Y) facing direction FACING (NORTH, EAST, SOUTH, WEST)
              </li>
              <li>
                <strong>MOVE</strong> - Move the rover one grid unit forward in the direction it is facing
              </li>
              <li>
                <strong>LEFT</strong> - Rotate the rover 90 degrees to the left
              </li>
              <li>
                <strong>RIGHT</strong> - Rotate the rover 90 degrees to the right
              </li>
              <li>
                <strong>REPORT</strong> - Display the current position and facing direction of the rover
              </li>
              <li>
                <strong>Example:</strong> PLACE 1,2,EAST; MOVE; MOVE; LEFT; MOVE; REPORT;
              </li>
            </ul>
          </ul>
        </div>
        <div className="grid-and-input">
          <Grid rover={rover} />
          <CommandInput onCommand={executeCommand} />
          {errorMessage && <div className="error-message">{errorMessage}</div>}
          {rover.x !== null && (
            <div className="position-string">
              {positionString}
            </div>
          )}
          {successMessage && <div className="success-message">{successMessage}</div>}
        </div>
      </div>
    </div>
  );
};

export default App;
