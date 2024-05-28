import React from 'react';

const SubmitButton = ({inputValues, x, updateInfo, selectedFunc, a, b, count}) => {
    const filteredInputValues = inputValues.filter(pair => pair.x !== '' && pair.y !== '');
    const handleSubmit = () => {
        const data = {
            pairs: filteredInputValues,
            x: x,
            selectedFunc: selectedFunc,
            a: a,
            b: b,
            count: count
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