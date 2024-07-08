import React from 'react';
import './Grid.css';

const Grid = ({ rover, error }) => {
  const createGrid = () => {
    let grid = [];
    for (let y = 4; y >= 0; y--) {
      let row = [];
      for (let x = 0; x < 5; x++) {
        let isRover = rover.x === x && rover.y === y;
        row.push(
          <div key={`${x}-${y}`} className={`cell ${isRover ? 'rover' : ''}`}>
            {isRover ? rover.facing[0] : ''}
          </div>
        );
      }
      grid.push(<div key={y} className="row">{row}</div>);
    }
    return grid;
  };

  return (
    <div className="grid">
      <div className="grid-content">
        {createGrid()}
      </div>
      {error && <div className="error-message">{error}</div>}
    </div>
  );
};

export default Grid;
