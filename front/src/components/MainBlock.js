import React, { useState } from 'react';
import Graph from "./Graph";
import RadioButtons from "./RadioButtons";
import IntervalInput from "./IntervalInput";
import InfoField from "./InfoField";
import SubmitButton from "./SubmitButton";
import TextInput from "./TextInput";

function MainBlock({ values, number }) {
    const [currentGraph1, setCurrentGraph1] = useState(0);
    const [currentGraph2, setCurrentGraph2] = useState(6);
    const [currentMethod, setCurrentMethod] = useState(3);
    const [answer, setAnswer] = useState('');
    const [file, setFile] = useState('');
    const [filepath, setFilepath] = useState('');
    const handleUpdateInfo = (newInfo) => {
        setAnswer(newInfo);
    };

    const handleUpdateFile = (newInfo) => {
        setFile(newInfo);
    };

    const [intervalA, setIntervalA] = useState('');
    const [intervalB, setIntervalB] = useState('');
    const [error, setError] = useState('');

    const handleIntervalAChange = (newValue) => {
        setIntervalA(newValue);
    };

    const handleIntervalBChange = (newValue) => {
        setIntervalB(newValue);
    };

    const handleErrorChange = (newValue) => {
        setError(newValue);
    };

    const handleFilepathChange = (newValue) => {
        setFilepath(newValue);
    };

    if (number === 1) {
        return (
            <div className="main-block">
                <Graph currentGraph={currentGraph1} number={1}/>
                <div className="input-button-container">
                    <RadioButtons values={values[0]} number={1} currentGraph={currentGraph1} setCurrentGraph={setCurrentGraph1}/>
                    <RadioButtons values={values[1]} number={2} currentGraph={currentMethod} setCurrentGraph={setCurrentMethod}/>
                </div>
                <div className="input-number-container">
                    <IntervalInput value={"a: "} onChange={handleIntervalAChange}/>
                    <IntervalInput value={"b: "} onChange={handleIntervalBChange}/>
                    <IntervalInput value={"error: "} onChange={handleErrorChange}/>
                    {/*<TextInput value={"filepath: "} onChange={handleFilepathChange}/>*/}
                </div>
                <SubmitButton label="Submit" updateInfo={handleUpdateInfo} intervalA={intervalA} intervalB={intervalB} graphNumber={currentGraph1} methodNumber={currentMethod} error={error    } answer={"None"} filepath={filepath}/>
                {/*<SubmitButton label="Save to file" updateInfo={handleUpdateFile} intervalA={intervalA} intervalB={intervalB} graphNumber={currentGraph1} methodNumber={currentMethod} error={error    } answer={answer} filepath={"None"}/>*/}
                <InfoField value={answer}/>
            </div>
        );
    } else if (number === 2) {
        return (
            <div className="main-block">
                <Graph currentGraph={currentGraph2} number={2}/>
                <div className="input-button-container">
                    <RadioButtons values={values[2]} number={3} currentGraph={currentGraph2} setCurrentGraph={setCurrentGraph2}/>
                </div>
                <div className="input-number-container">
                    <IntervalInput value={"a: "} onChange={handleIntervalAChange}/>
                    <IntervalInput value={"b: "} onChange={handleIntervalBChange}/>
                    <IntervalInput value={"error: "} onChange={handleErrorChange}/>
                    {/*<TextInput value={"filepath: "} onChange={handleFilepathChange}/>*/}
                </div>
                <SubmitButton label="Submit" updateInfo={handleUpdateInfo} intervalA={intervalA} intervalB={intervalB} graphNumber={currentGraph2} methodNumber={currentGraph2} error={error} answer={"None"} filepath={filepath}/>
                {/*<SubmitButton label="Save to file" updateInfo={handleUpdateFile} intervalA={intervalA} intervalB={intervalB} graphNumber={currentGraph1} methodNumber={currentMethod} error={error    } answer={answer} filepath={"None "}/>*/}
                <InfoField value={answer}/>
            </div>
        );
    }
}

export default MainBlock;
