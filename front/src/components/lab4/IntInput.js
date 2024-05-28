import React from 'react';

const IntInput = ({ value, onChange }) => {
    return <input type="number" value={value} onChange={onChange} step="1" />;
}

export default IntInput;