import React from 'react';

function IntervalInput({ value, onChange }) {
    const handleInputChange = (event) => {
        const newValue = event.target.value;
        if (!isNaN(newValue)) {
            onChange(newValue);
        }
    };

    return (
        <label>
            {value}
            <input
                type="number"
                onChange={handleInputChange}
                className="input-number"
            />
        </label>
    );
}

export default IntervalInput;
