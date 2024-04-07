import React from 'react';

function TextInput({ value, onChange }) {
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
                type="text"
                onChange={handleInputChange}
                className="input-text"
            />
        </label>
    );
}

export default TextInput;
