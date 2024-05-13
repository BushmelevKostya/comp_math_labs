import React from 'react';

const FloatInput = ({ value, onChange }) => {
    return <input type="number" value={value} onChange={onChange} step="0.01" />;
}

export default FloatInput;