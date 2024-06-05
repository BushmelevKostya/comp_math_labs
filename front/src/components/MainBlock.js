import React, {useState} from 'react';
import Graph from "./Graph";
import SubmitButton from "./lab4/SubmitButton";
import CheckButtons from "./lab4/CheckButtons";
import TableInput from "./lab4/TableInput";
import TextOutput from "./lab4/TextOutput";
import FloatInput from "./lab4/FloatInput";
import IntInput from "./lab4/IntInput";

function MainBlock() {
    const [inputValues, setInputValues] = useState(
        Array(7).fill(0).map(() => ({ x: 0, y: 0 }))
    );
    const [outputText, setOutputText] = useState('');
    const [errorText, setErrorText] = useState('');
    const [floatValue, setFloatValue] = useState(0);
    const [aValue, setAValue] = useState(0);
    const [bValue, setBValue] = useState(0);
    const [countValue, setCountValue] = useState(0);
    const [selectedFunc, setSelectedFunc] = useState('x^2');

    const handleInputChange = (index, field, value) => {
        const newInputValues = [...inputValues];
        newInputValues[index][field] = value;
        setInputValues(newInputValues);
    };

    const updateInfo = (data) => {
        setOutputText(data);
        setErrorText('');
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
                    setErrorText('');
                } catch (error) {
                    setErrorText('Error reading file');
                }
            };

            reader.readAsText(file);
        };

        input.click();
    };

    const handleFloatInputChange = (event) => {
        setFloatValue(event.target.value);
    };

    const handleAInputChange = (event) => {
        setAValue(event.target.value);
    };

    const handleBInputChange = (event) => {
        setBValue(event.target.value);
    };

    const handleCountInputChange = (event) => {
        setCountValue(event.target.value);
    };

    const handleFuncChange = (funcType) => {
        setSelectedFunc(funcType);
    };

    return (
        <div className="main-block">
            <div className="text-block">
                <div className="input-number-container">
                    <TableInput handleInputChange={handleInputChange} inputValues={inputValues} />
                </div>
                <div>
                    x: <FloatInput
                    value={floatValue}
                    onChange={handleFloatInputChange}
                />
                </div>
                <div className="another-input">
                    <CheckButtons onChange={handleFuncChange} />
                    a: <FloatInput
                    value={aValue}
                    onChange={handleAInputChange} />
                    b: <FloatInput
                    value={bValue}
                    onChange={handleBInputChange} />
                    count: <IntInput
                    value={countValue}
                    onChange={handleCountInputChange} />
                </div>
                <button onClick={handleFileButtonClick}>Upload</button>
                <SubmitButton inputValues={inputValues} x={floatValue} updateInfo={updateInfo} selectedFunc={selectedFunc} a={aValue} b={bValue} count={countValue} />
                {errorText && <div className="error-message">{errorText}</div>}
                <TextOutput text={outputText} />
            </div>
            <div className="graph-block">
                <Graph data={outputText} inputValues={inputValues} func={selectedFunc}/>
            </div>
        </div>
    );
}


export default MainBlock;
