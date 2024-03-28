import React from "react";

function Button({ value, option, onChange, label }) {
    return (
        <div>
            <label>
                <input
                    type="radio"
                    value={value}
                    checked={option === value}
                    onChange={onChange}
                />
                {label}
            </label>
        </div>
    );
}

export default Button;