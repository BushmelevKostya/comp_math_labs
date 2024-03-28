import React, { useState } from 'react';
import Button from "./Button";

function RadioButtons({values, number}) {
    const [selectedOption, setSelectedOption] = useState('option1');

    const handleOptionChange = (event) => {
        setSelectedOption(event.target.value);
    };

    if (number === 1) {
        return (
            <div className="button-box">
                <Button value={values[0]} option={selectedOption} onChange={handleOptionChange} label={values[0]}/>
                <Button value={values[1]} option={selectedOption} onChange={handleOptionChange} label={values[1]}/>
                <Button value={values[2]} option={selectedOption} onChange={handleOptionChange} label={values[2]}/>
            </div>
        );
    }

    else if (number === 2) {
        return (
            <div className="button-box">
                <Button value={values[0]} option={selectedOption} onChange={handleOptionChange} label={values[0]}/>
                <Button value={values[1]} option={selectedOption} onChange={handleOptionChange} label={values[1]}/>
            </div>
        );
    }
}

export default RadioButtons;
