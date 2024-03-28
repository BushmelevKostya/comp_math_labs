import React from "react";

function Button({ value, selectedOption, onChange, label }) {
    return (
        <div className="button">
            <label>
                <input
                    type="radio"
                    value={value}
                    checked={selectedOption === value}
                    onChange={onChange}
                />
                {label}
            </label>
        </div>
    );
}

export default Button;
