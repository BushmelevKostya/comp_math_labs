import Graph from "./Graph";
import RadioButtons from "./RadioButtons";
import IntervalInput from "./IntervalInput";
import InfoField from "./InfoField";

function MainBlock() {
    return (
        <div className="main-block">
            <Graph/>
            <div className="input-button-container">
                <RadioButtons/>
                <RadioButtons/>
            </div>
            <div className="input-number-container">
                <IntervalInput/>
                <IntervalInput/>
            </div>
            <InfoField value="There is answer"/>
        </div>
    );
}

export default MainBlock;