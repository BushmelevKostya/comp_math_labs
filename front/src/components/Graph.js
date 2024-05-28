import React, {useEffect, useRef, useState} from 'react';
import Desmos from 'desmos';

function Graph({data, inputValues}) {
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

        // if (line) {
        //     let word = line.split(' ')[0];
        //     let a0, a1, a2, a3;
        //     switch (word) {
        //         case "Linear":
        //             line = data.split('\n').find(line => line.includes('a:'));
        //             a0 = line.replace("a: ", "")
        //             line = data.split('\n').find(line => line.includes('b:'));
        //             a1 = line.replace("b: ", "")
        //             setLatex1(`${a0}*x + (${a1})`);
        //             setLatex2(`${points}`);
        //             break;
        //         case "Polynomial_2":
        //             line = data.split('\n').find(line => line.includes('a0'));
        //             a0 = line.replace("a0: ", "")
        //             line = data.split('\n').find(line => line.includes('a1'));
        //             a1 = line.replace("a1: ", "")
        //             line = data.split('\n').find(line => line.includes('a2'));
        //             a2 = line.replace("a2: ", "")
        //             setLatex1(`${a0} + (${a1}*x) + (${a2}*x^2)`);
        //             setLatex2(`${points}`);
        //             break;
        //         case "Polynomial_3":
        //             line = data.split('\n').find(line => line.includes('a0'));
        //             a0 = line.replace("a0: ", "")
        //             line = data.split('\n').find(line => line.includes('a1'));
        //             a1 = line.replace("a1: ", "")
        //             line = data.split('\n').find(line => line.includes('a2'));
        //             a2 = line.replace("a2: ", "")
        //             line = data.split('\n').find(line => line.includes('a3'));
        //             a3 = line.replace("a3: ", "")
        //             setLatex1(`${a0} + (${a1}*x) + (${a2}*x^2) + (${a3}*x^3)`);
        //             setLatex2(`${points}`);
        //             break;
        //         case "Power":
        //             line = data.split('\n').find(line => line.includes('a:'));
        //             a0 = line.replace("a: ", "")
        //             line = data.split('\n').find(line => line.includes('b:'));
        //             a1 = line.replace("b: ", "")
        //             setLatex1(`${a0}*x^(${a1})`);
        //             setLatex2(`${points}`);
        //             break;
        //         case "Exponential":
        //             line = data.split('\n').find(line => line.includes('a:'));
        //             a0 = line.replace("a: ", "")
        //             line = data.split('\n').find(line => line.includes('b:'));
        //             a1 = line.replace("b: ", "")
        //             setLatex1(`${a0} \\cdot e^{${a1}*x}`);
        //             setLatex2(`${points}`);
        //             break;
        //         case "Logarithmic":
        //             line = data.split('\n').find(line => line.includes('a:'));
        //             a0 = line.replace("a: ", "")
        //             line = data.split('\n').find(line => line.includes('b:'));
        //             a1 = line.replace("b: ", "")
        //             setLatex1(`${a0} \\cdot \\ln{x} + ${a1}`);
        //             setLatex2(`${points}`);
        //             break;
        //         default:
        //             setLatex1("");
        //     }
        // }
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
        return () => {
            calculator.destroy();
        };
    }, [latex1, latex2, latex3, latex4, latex5, latex6, latex7, latex8, latex9]);

    return <div ref={desmosContainerRef} style={{width: '600px', height: '350px'}}/>;
}

export default Graph;
