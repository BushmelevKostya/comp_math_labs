import React, {useEffect, useRef, useState} from 'react';
import Desmos from 'desmos';

function Graph({data}) {
    const desmosContainerRef = useRef(null);
    const [latex, setLatex] = useState('');
    useEffect(() => {
        updateGraph(data);
    }, [data]);

    const updateGraph = (data) => {
        let line = data.split('\n').find(line => line.includes('approximation'));

        if (line) {
            let word = line.split(' ')[0];
            let a0, a1, a2, a3
            switch (word) {
                case "Linear":
                    line = data.split('\n').find(line => line.includes('a:'));
                    a0 = line.replace("a: ", "")
                    line = data.split('\n').find(line => line.includes('b:'));
                    a1 = line.replace("b: ", "")
                    setLatex(a0 + "*x" + "+ (" + a1 + ")")
                    break
                case "Polynomial_2":
                    line = data.split('\n').find(line => line.includes('a0'));
                    a0 = line.replace("a0: ", "")
                    line = data.split('\n').find(line => line.includes('a1'));
                    a1 = line.replace("a1: ", "")
                    line = data.split('\n').find(line => line.includes('a2'));
                    a2 = line.replace("a2: ", "")
                    setLatex(a0 + "+" + "(" + a1 + "x" + ")" + "+" + "(" + a2 + "x^2" + ")")
                    break
                case "Polynomial_3":
                    line = data.split('\n').find(line => line.includes('a0'));
                    a0 = line.replace("a0: ", "")
                    line = data.split('\n').find(line => line.includes('a1'));
                    a1 = line.replace("a1: ", "")
                    line = data.split('\n').find(line => line.includes('a2'));
                    a2 = line.replace("a2: ", "")
                    line = data.split('\n').find(line => line.includes('a3'));
                    a3 = line.replace("a3: ", "")
                    setLatex(a0 + "+" + "(" + a1 + "x" + ")" + "+" + "(" + a2 + "x^2" + ")" + "+" + "(" + a3 + "x^3" + ")")
                    break
                case "Power":
                    line = data.split('\n').find(line => line.includes('a:'));
                    a0 = line.replace("a: ", "")
                    line = data.split('\n').find(line => line.includes('b:'));
                    a1 = line.replace("b: ", "")
                    setLatex(a0 + "*x^" + "(" + a1 + ")")
                    break
                case "Exponential":
                    line = data.split('\n').find(line => line.includes('a:'));
                    a0 = line.replace("a: ", "")
                    line = data.split('\n').find(line => line.includes('b:'));
                    a1 = line.replace("b: ", "")
                    setLatex(`${a0} \\cdot e^{${a1}x}`)
                    break
                case "Logarithmic":
                    line = data.split('\n').find(line => line.includes('a:'));
                    a0 = line.replace("a: ", "")
                    line = data.split('\n').find(line => line.includes('b:'));
                    a1 = line.replace("b: ", "")
                    setLatex(`${a0} \\cdot \\ln{x} + ${a1}`);
                    break
                default:
                    setLatex("")
            }
        }
    };

    useEffect(() => {
        const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
        calculator.setExpression({id: 'graph1', latex: latex});
        return () => {
            calculator.destroy();
        };
    }, [latex]);

    return <div ref={desmosContainerRef} style={{width: '600px', height: '350px'}}/>;
}

export default Graph;
