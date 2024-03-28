import React, { useState } from 'react';
import Graph from "./Graph";
import RadioButtons from "./RadioButtons";
import IntervalInput from "./IntervalInput";
import InfoField from "./InfoField";
import SubmitButton from "./SubmitButton";

function MainBlock({ values, number }) {
    const handleSubmit = () => {
        console.log('Form submitted!');
    };

    const [intervalA, setIntervalA] = useState('');
    const [intervalB, setIntervalB] = useState('');

    const handleIntervalAChange = (newValue) => {
        setIntervalA(newValue);
    };

    const handleIntervalBChange = (newValue) => {
        setIntervalB(newValue);
    };

    if (number === 1) {
        return (
            <div className="main-block">
                <Graph/>
                <div className="input-button-container">
                    <RadioButtons values={values[0]} number={number}/>
                    <RadioButtons values={values[1]} number={number}/>
                </div>
                <div className="input-number-container">
                    <IntervalInput value={"a: "} onChange={handleIntervalAChange}/>
                    <IntervalInput value={"b: "} onChange={handleIntervalBChange}/>
                </div>
                <SubmitButton label="Submit" onClick={handleSubmit} />
                <InfoField value="There is answer"/>
            </div>
        );
    } else if (number === 2) {
        return (
            <div className="main-block">
                <Graph/>
                <div className="input-button-container">
                    <RadioButtons values={values[2]} number={number}/>
                </div>
                <div className="input-number-container">
                    <IntervalInput value={"a: "} onChange={handleIntervalAChange}/>
                    <IntervalInput value={"b: "} onChange={handleIntervalBChange}/>
                </div>
                <SubmitButton label="Submit" onClick={handleSubmit} />
                <InfoField value="There is answer"/>
            </div>
        );
    }
}

export default MainBlock;
