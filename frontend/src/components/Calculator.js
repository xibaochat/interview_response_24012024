import React, { useState } from 'react';

import './Calculator.css';

const Calculator = () => {
  const [input, setInput] = useState('');
  const [inputList, setInputList] = useState([]);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const isNumber = (value) => {
    return !isNaN(parseFloat(value)) && isFinite(value);
  };

  const isOperator = (value) => {
    return ['+', '-', '*', '/', '^'].includes(value);
  };

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

const handleAddToList = () => {
  const inputValue = input.trim();

  if (inputValue !== '') {
    // Check if the input is a valid number or operator
    if (isNumber(inputValue) || isOperator(inputValue)) {
      // If it's a valid number, convert it to a number
      const numberValue = isNumber(inputValue) ? parseFloat(inputValue) : inputValue;
      console.log('numberValue: ', numberValue, typeof(numberValue))
      setInputList([...inputList, numberValue]);
      setInput(''); // Clear the input field
      setError(null);
    } else {
      setError('Invalid input. Must be a number or one of the allowed operators.');
    }
  } else {
    setError('Input cannot be empty.');
  }
};

  const handleCalculate = async () => {
  try {
    // Wrap inputList in an object with the expected structure
    const requestData = { instruction: inputList };

    const response = await fetch(`${process.env.REACT_APP_API_BASE_URL}/calculator`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData),
    });

      if (!response.ok) {
		  setInput('');
		  setInputList([]);
      throw new Error('Error calculating result');
    }
    const data = await response.json();
      setResult(data);
	  setInputList([]);
	  setError(null);
  }
	  catch (err) {
		  setResult(null);
		  setError('Error calculating result');
		  setInput('');
		  setInputList([]);
	  }
};

	return (
	<form id="container">
	<h1>Polish Calculator</h1>
      <p>Input: {inputList.join(' ')}</p>
      <p>Result: {result !== null ? result : 'N/A'}</p>
      <p>Error: {error}</p>
      <input type="text" value={input} onChange={handleInputChange} />
	  <button type="reset" onClick={handleAddToList}>Add to List</button>
      <button type="button" onClick={handleCalculate}>Calculate</button>
    </form>
  );
};

export default Calculator;
