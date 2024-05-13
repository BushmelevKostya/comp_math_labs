import React, { useState } from 'react';
import Graph from "./Graph";
import SubmitButton from "./lab4/SubmitButton";
import TableInput from "./lab4/TableInput";
import TextOutput from "./lab4/TextOutput";
import FileButton from "./lab4/FileButton";

function MainBlock() {
    const [inputValues, setInputValues] = useState(
        Array(12).fill(0).map(() => ({ x: 0, y: 0 }))
    );
    const [outputText, setOutputText] = useState('');

    const handleInputChange = (index, field, value) => {
        const newInputValues = [...inputValues];
        newInputValues[index][field] = value;
        setInputValues(newInputValues);
    };

    const updateInfo = (data) => {
        setOutputText(data);
    };

    const handleFileButtonClick = () => {
        const input = document.createElement('input');
        input.type = 'file';

        input.onchange = (e) => {
            const file = e.target.files[0];
            const reader = new FileReader();

            reader.onload = (event) => {
                const content = event.target.result;
                const data = content.split('\n').map(line => {
                    const [x, y] = line.split(',');
                    return { x: parseFloat(x), y: parseFloat(y) };
                });
                setInputValues(data);
            };

            reader.readAsText(file);
        };

        input.click();
    };

    return (
        <div className="main-block">
            <div className="input-number-container">
                <TableInput handleInputChange={handleInputChange} inputValues={inputValues} />
            </div>
            <button onClick={handleFileButtonClick}>Upload</button>
            <SubmitButton inputValues={inputValues} updateInfo={updateInfo} />
            <TextOutput text={outputText} />
            <Graph data={outputText}/>
        </div>
    );
}

export default MainBlock;
