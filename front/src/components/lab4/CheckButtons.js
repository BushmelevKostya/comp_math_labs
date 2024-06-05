import React, { useState } from 'react';

function CheckButtons({ onChange }) {
    const [selectedButton, setSelectedButton] = useState('');

    const handleButtonClick = (funcType) => {
        setSelectedButton(funcType);
        onChange(funcType);
    };

    return (
        <div>
            <input
                type="radio"
                id="y + (1 + x)*y^2"
                name="function"
                value="y + (1 + x)*y^2"
                checked={selectedButton === 'y + (1 + x)*y^2'}
                onChange={() => handleButtonClick('y + (1 + x)*y^2')}
            />
            <label htmlFor="y + (1 + x)*y^2">y + (1 + x)*y^2</label>

            <input
                type="radio"
                id="x + y"
                name="function"
                value="x + y"
                checked={selectedButton === 'x + y'}
                onChange={() => handleButtonClick('x + y')}
            />
            <label htmlFor="x + y">x + y</label>

            <input
                type="radio"
                id="sin(x) - y"
                name="function"
                value="sin(x) - y"
                checked={selectedButton === 'sin(x) - y'}
                onChange={() => handleButtonClick('sin(x) - y')}
            />
            <label htmlFor="sin(x) - y">sin(x) - y</label>
        </div>
    );
}

export default CheckButtons;
