import React, {useState} from 'react';
import Graph from "./Graph";
import SubmitButton from "./lab4/SubmitButton";
import TableInput from "./lab4/TableInput";
import TextOutput from "./lab4/TextOutput";

function MainBlock() {
    const [inputValues, setInputValues] = useState(
        Array(12).fill(0).map(() => ({x: 0, y: 0}))
    );
    const [outputText, setOutputText] = useState('');
    const [errorText, setErrorText] = useState('');

    const handleInputChange = (index, field, value) => {
        const newInputValues = [...inputValues];
        newInputValues[index][field] = value;
        setInputValues(newInputValues);
    };

    const updateInfo = (data) => {
        setOutputText(data);
        setErrorText('')
    };

    const handleFileButtonClick = () => {
        const input = document.createElement('input');
        input.type = 'file';

        input.onchange = (e) => {
            const file = e.target.files[0];
            const reader = new FileReader();

            reader.onload = (event) => {
                try {
                    const content = event.target.result;
                    const data = content.split('\n').map(line => {
                        const [x, y] = line.split(',');
                        if (x !== undefined && y !== undefined) {
                            return { x: parseFloat(x), y: parseFloat(y) };
                        } else {
                            throw new Error('Invalid data format in the file.');
                        }
                    });
                    setInputValues(data);
                    setErrorText('')
                } catch (error) {
                    setErrorText('Error reading file');
                }
            };

            reader.readAsText(file);
        };

        input.click();
    };

    return (
        <div className="main-block">
            <div className="text-block">
                <div className="input-number-container">
                    <TableInput handleInputChange={handleInputChange} inputValues={inputValues}/>
                </div>
                <button onClick={handleFileButtonClick}>Upload</button>
                <SubmitButton inputValues={inputValues} updateInfo={updateInfo}/>
                {errorText && <div className="error-message">{errorText}</div>}
                <TextOutput text={outputText}/>
            </div>
            <div className="graph-block">
                <Graph data={outputText} inputValues={inputValues}/>
            </div>
        </div>
    );
}

export default MainBlock;
