import React, { useState } from 'react';
import Button from "./Button";

function RadioButtons() {
    const [selectedOption, setSelectedOption] = useState('option1');

    const handleOptionChange = (event) => {
        setSelectedOption(event.target.value);
    };

    return (
        <div className="button-box">
            <Button value={"option1"} option={selectedOption} onChange={handleOptionChange} label={"Option 1"}/>
            <Button value={"option2"} option={selectedOption} onChange={handleOptionChange} label={"Option 2"}/>
            <Button value={"option3"} option={selectedOption} onChange={handleOptionChange} label={"Option 3"}/>
        </div>
    );
}

export default RadioButtons;