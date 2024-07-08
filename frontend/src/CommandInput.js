import React, { useState } from 'react';

const CommandInput = ({ onCommand }) => {
  const [command, setCommand] = useState('');

  const handleChange = (e) => {
    setCommand(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (command.trim()) {
      onCommand(command);
      setCommand('');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: '10px' }}>
      <input
        type="text"
        value={command}
        onChange={handleChange}
        placeholder="Enter command"
        style={{ padding: '10px', marginRight: '10px' }}
      />
      <button type="submit" style={{ padding: '10px' }}>Send</button>
    </form>
  );
};

export default CommandInput;
