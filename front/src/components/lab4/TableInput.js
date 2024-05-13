import React, {useState} from 'react';
import FloatInput from "./FloatInput";


const TableInput = ({inputValues, handleInputChange}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>x</th>
                <th>y</th>
            </tr>
            </thead>
            <tbody>
            {Array(12).fill(0).map((_, i) => (
                <div key={i}>
                    <FloatInput
                        value={inputValues[i].x}
                        onChange={(e) => handleInputChange(i, 'x', e.target.value)}
                    />
                    <FloatInput
                        value={inputValues[i].y}
                        onChange={(e) => handleInputChange(i, 'y', e.target.value)}
                    />
                </div>
            ))}
            </tbody>
        </table>
    );
}

export default TableInput;