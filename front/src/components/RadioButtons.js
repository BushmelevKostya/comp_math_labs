import React, { useState } from 'react';
import Button from "./Button";

function RadioButtons({values, number, currentGraph, setCurrentGraph}) {
    const [selectedOption, setSelectedOption] = useState(0);

    const handleOptionChange = (event) => {
        setSelectedOption(parseInt(event.target.value));
        redrawGraph(event.target.value);
    };

    if (number === 1) {
        return (
            <div className="button-box">
                <Button value={0} selectedOption={selectedOption} onChange={handleOptionChange} label={values[0]}/>
                <Button value={1} selectedOption={selectedOption} onChange={handleOptionChange} label={values[1]}/>
                <Button value={2} selectedOption={selectedOption} onChange={handleOptionChange} label={values[2]}/>
            </div>
        );
    }

    if (number === 2) {
        return (
            <div className="button-box">
                <Button value={3} selectedOption={selectedOption} onChange={handleOptionChange} label={values[0]}/>
                <Button value={4} selectedOption={selectedOption} onChange={handleOptionChange} label={values[1]}/>
                <Button value={5} selectedOption={selectedOption} onChange={handleOptionChange} label={values[2]}/>
            </div>
        );
    }

    else if (number === 3) {
        return (
            <div className="button-box">
                <Button value={6} selectedOption={selectedOption} onChange={handleOptionChange} label={values[0]}/>
                <Button value={7} selectedOption={selectedOption} onChange={handleOptionChange} label={values[1]}/>
            </div>
        );
    }
}

export default RadioButtons;
