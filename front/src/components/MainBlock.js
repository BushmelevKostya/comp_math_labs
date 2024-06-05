import React, { useState } from 'react';
import Graph from "./Graph";
import CheckButtons from "./lab4/CheckButtons";
import FloatInput from "./lab4/FloatInput";
import IntInput from "./lab4/IntInput";
import SubmitButton from "./lab4/SubmitButton";
import TextOutput from "./lab4/TextOutput";

function MainBlock() {
    const [outputText, setOutputText] = useState('');
    const [errorText, setErrorText] = useState('');
    const [floatValues, setFloatValues] = useState(Array(5).fill(0));
    const [intValue, setIntValue] = useState(0);
    const [selectedFunc, setSelectedFunc] = useState('y + (1 + x)*y^2');

    const updateInfo = (data) => {
        setOutputText(data);
        setErrorText('');
    };

    const handleFloatInputChange = (index, event) => {
        const newFloatValues = [...floatValues];
        newFloatValues[index] = parseFloat(event.target.value);
        setFloatValues(newFloatValues);
    };

    const handleIntInputChange = (event) => {
        setIntValue(parseInt(event.target.value, 10));
    };

    const handleFuncChange = (funcType) => {
        setSelectedFunc(funcType);
    };

    return (
        <div className="main-block">
            <div className="text-block">
                <div className="float-inputs">
                    {floatValues.map((value, index) => (
                        <div key={index}>
                            {`Float ${index + 1}: `}
                            <FloatInput
                                value={value}
                                onChange={(e) => handleFloatInputChange(index, e)}
                            />
                        </div>
                    ))}
                </div>
                <div>
                    Int: <IntInput
                    value={intValue}
                    onChange={handleIntInputChange}
                />
                </div>
                <div className="check-buttons">
                    <CheckButtons onChange={handleFuncChange} />
                </div>
                <SubmitButton
                    floatValues={floatValues}
                    intValue={intValue}
                    selectedFunc={selectedFunc}
                    updateInfo={updateInfo}
                />
                {errorText && <div className="error-message">{errorText}</div>}
                <TextOutput text={outputText} />
            </div>
            <div className="graph-block">
                 {/*<Graph data={outputText} />*/}
            </div>
        </div>
    );
}

export default MainBlock;
