import React from 'react';

function IntervalInput({ value, onChange }) {
    const handleInputChange = (event) => {
        const newValue = event.target.value;
        if (!isNaN(newValue)) {
            onChange(newValue);
        }
    };

    return (
        <input
            type="number"
            value={value}
            onChange={handleInputChange}
            className="input-number"
        />
    );
}

export default IntervalInput;