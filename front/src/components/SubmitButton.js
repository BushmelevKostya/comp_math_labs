import React, { useState } from 'react';

function SubmitButton({ label, updateInfo, intervalA, intervalB, graphNumber, methodNumber, error }) {
    const handleSubmit = () => {
        const data = {
            intervalA: intervalA,
            intervalB: intervalB,
            graphNumber: graphNumber,
            methodNumber: methodNumber,
            error: error
        };

        fetch('http://localhost:8080/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.text())
            .then(data => {
                updateInfo(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    };

    return (
        <button onClick={handleSubmit}>{label}</button>
    );
}

export default SubmitButton;
