import React, { useEffect, useRef, useState } from 'react';
import Desmos from 'desmos';

function Graph({ data }) {
    const desmosContainerRef = useRef(null);
    const [points, setPoints] = useState('');

    useEffect(() => {
        updateGraph(data);
    }, [data]);

    const updateGraph = (data) => {
        const pairs = [];
        const xLine = data.split('\n').find(line => line.includes('x -'));
        const xValues = xLine ? xLine.match(/(\d+(\.\d+)?)/g) : [];

        const yLine = data.split('\n').find(line => line.includes('y -'));
        const yValues = yLine ? yLine.match(/(\d+(\.\d+)?)/g) : [];

        // Form pairs
        if (xValues && yValues && xValues.length === yValues.length) {
            for (let i = 0; i < xValues.length; i++) {
                pairs.push(`(${xValues[i]}, ${yValues[i]})`);
            }
        }

        setPoints(pairs.join(', '));
    };

    useEffect(() => {
        const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
        calculator.setExpression({ id: 'graph1', latex: `\\left[ ${points} \\right]`, color: '#000' });

        return () => {
            calculator.destroy();
        };
    }, [points]);

    return (
        <div>
            <div ref={desmosContainerRef} style={{ width: '600px', height: '350px' }}></div>
        </div>
    );
}

export default Graph;
