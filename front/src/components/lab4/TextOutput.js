import React from 'react';

const TextOutput = ({ text }) => {
    const lines = text.split('\n');

    return (
        <div>
            {lines.map((line, index) => (
                <div key={index}>{line}</div>
            ))}
        </div>
    );
}

export default TextOutput;