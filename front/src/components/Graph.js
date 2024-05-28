import React, {useEffect, useRef, useState} from 'react';
import Desmos from 'desmos';

function Graph({data, inputValues, func}) {
    const desmosContainerRef = useRef(null);
    const [latex1, setLatex1] = useState('');
    const [latex2, setLatex2] = useState('');
    const [latex3, setLatex3] = useState('');
    const [latex4, setLatex4] = useState('');
    const [latex8, setLatex8] = useState('');
    const [latex5, setLatex5] = useState('');
    const [latex6, setLatex6] = useState('');
    const [latex7, setLatex7] = useState('');
    const [latex9, setLatex9] = useState('');
    const [latex10, setLatex10] = useState('');
    useEffect(() => {
        updateGraph(data);
    }, [data]);

    const updateGraph = (data) => {
        let points = inputValues
            .filter(point => point.x !== '' && point.y !== '')
            .map(point => `(${point.x},${point.y})`)
            .join(',');
        setLatex1(`${points}`);
        let line;
        line = data.split('\n').find(line => line.includes('Lagrange equation:'));
        if (line) {
            line = line.replace("Lagrange equation: ", "");
            setLatex2(line);
        }
        line = data.split('\n').find(line => line.includes('Newton equation:'));
        if (line) {
            line = line.replace("Newton equation: ", "");
            setLatex3(line);
        }
        line = data.split('\n').find(line => line.includes('Gauss equation:'));
        if (line) {
            line = line.replace("Gauss equation: ", "");
            setLatex4(line);
        }
        line = data.split('\n').find(line => line.includes('Stirling equation:'));
        if (line) {
            line = line.replace("Stirling equation: ", "");
            setLatex8(line);
        }
        let x, y, arr;
        line = data.split('\n').find(line => line.includes('Lagrange method - result value f('));
        if (line) {
            line = line.replace("Lagrange method - result value f( ", "").replace(" )", "");
            arr = line.split(":")
            x = arr[0]
            y = arr[1]
            setLatex5("(" + x + "," + y + ")");
        }
        line = data.split('\n').find(line => line.includes('Newton method - result value f('));
        if (line) {
            line = line.replace("Newton method - result value f( ", "").replace(" )", "");
            arr = line.split(":")
            x = arr[0]
            y = arr[1]
            setLatex6("(" + x + "," + y + ")");
        }
        line = data.split('\n').find(line => line.includes('Gauss method - result value f('));
        if (line) {
            line = line.replace("Gauss method - result value f( ", "").replace(" )", "");
            arr = line.split(":")
            x = arr[0]
            y = arr[1]
            setLatex7("(" + x + "," + y + ")");
        }
        line = data.split('\n').find(line => line.includes('Stirling method - result value f('));
        if (line) {
            line = line.replace("Stirling method - result value f( ", "").replace(" )", "");
            arr = line.split(":")
            x = arr[0]
            y = arr[1]
            setLatex9("(" + x + "," + y + ")");
        }
        setLatex10(func)
    };

    useEffect(() => {
        const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
        calculator.setExpression({id: 'graph1', latex: latex1, color: '#000'});
        calculator.setExpression({id: 'graph2', latex: latex2, color: '#FF0000'});
        calculator.setExpression({id: 'graph3', latex: latex3, color: '#00FF00'});
        calculator.setExpression({id: 'graph4', latex: latex4, color: '#0000FF'});
        calculator.setExpression({id: 'graph8', latex: latex8, color: '#E8E88E'});
        calculator.setExpression({id: 'graph5', latex: latex5, color: '#FF0000'});
        calculator.setExpression({id: 'graph6', latex: latex6, color: '#00FF00'});
        calculator.setExpression({id: 'graph7', latex: latex7, color: '#0000FF'});
        calculator.setExpression({id: 'graph9', latex: latex9, color: '#E8E88E'});
        calculator.setExpression({id: 'graph10', latex: latex10, color: '#222'});
        return () => {
            calculator.destroy();
        };
    }, [latex1, latex2, latex3, latex4, latex5, latex6, latex7, latex8, latex9, latex10]);

    const legendItems = [
        {label: 'Input Points', color: '#000', latex: latex1},
        {label: 'Lagrange Equation', color: '#FF0000', latex: latex2},
        {label: 'Newton Equation', color: '#00FF00', latex: latex3},
        {label: 'Gauss Equation', color: '#0000FF', latex: latex4},
        {label: 'Lagrange Result', color: '#FF0000', latex: latex5},
        {label: 'Newton Result', color: '#00FF00', latex: latex6},
        {label: 'Gauss Result', color: '#0000FF', latex: latex7},
        {label: 'Stirling Equation', color: '#E8E88E', latex: latex8},
        {label: 'Stirling Result', color: '#E8E88E', latex: latex9},
        {label: 'Input Function', color: '#222', latex: latex10}
    ];

    return (
        <div>
            <div ref={desmosContainerRef} style={{width: '600px', height: '350px'}}></div>
            <div className="legend">
                {legendItems.map((item, index) => (
                    <div key={index} className="legend-item" style={{color: item.color}}>
                        <span style={{backgroundColor: item.color}} className="legend-color"></span>
                        {item.label}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Graph;
