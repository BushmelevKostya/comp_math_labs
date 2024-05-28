import React, {useEffect, useRef, useState} from 'react';
import Desmos from 'desmos';

function Graph({data, inputValues}) {
    const desmosContainerRef = useRef(null);
    const [latex1, setLatex1] = useState('');
    const [latex2, setLatex2] = useState('');
    useEffect(() => {
        updateGraph(data);
    }, [data]);

    const updateGraph = (data) => {
        // let line = data.split('\n').find(line => line.includes('approximation'));
        let points = inputValues
            .filter(point => point.x !== '' && point.y !== '')
            .map(point => `(${point.x},${point.y})`)
            .join(',');
        setLatex1(`${points}`);
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
        calculator.setExpression({id: 'graph1', latex: latex1});
        calculator.setExpression({id: 'graph2', latex: latex2});
        return () => {
            calculator.destroy();
        };
    }, [latex1, latex2]);

    return <div ref={desmosContainerRef} style={{width: '600px', height: '350px'}}/>;
}

export default Graph;
