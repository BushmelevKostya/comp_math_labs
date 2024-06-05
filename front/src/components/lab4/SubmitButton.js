import React from 'react';

const SubmitButton = ({ floatValues, intValue, selectedFunc, updateInfo }) => {
    const handleSubmit = () => {
        const data = {
            floatValues: floatValues,
            intValue: intValue,
            selectedFunc: selectedFunc
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
        <button onClick={handleSubmit}>Submit</button>
    );
}

export default SubmitButton;
