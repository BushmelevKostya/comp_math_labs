import React, {useEffect, useRef} from 'react';
import Desmos from 'desmos';

function Graph({currentGraph, number}) {
    const desmosContainerRef = useRef(null);
    let latex;
    let latex2;
    if (number === 1) {
        switch (currentGraph) {
            case 0:
                latex = "y = 3x^3 + x^2 - x + 1";
                break;
            case 1:
                latex = "y = x^4 - 5x^2 + 4";
                break;
            case 2:
                latex = "y = -x^3 - x^2 - x - 1";
                break;
            default:
                console.log(currentGraph);
        }
    } else if (number === 2) {
        switch (currentGraph) {
            case 8:
                latex = "f(x) = 1 / (1 - x)";
                break;
            case 9:
                latex = "f(x) = \\frac{1}{\\sqrt{x}}";
                break;
            case 10:
                latex = "f(x) = \\ln(x)";
                break;
            default:
                console.log(currentGraph);
        }
    }

    useEffect(() => {
        const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
        calculator.setExpression({id: 'graph1', latex: latex});
        return () => {
            calculator.destroy();
        };
    }, [currentGraph, latex]);

    return <div ref={desmosContainerRef} style={{width: '600px', height: '350px'}}/>;
}

export default Graph;
