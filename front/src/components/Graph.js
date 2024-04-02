import React, {useEffect, useRef} from 'react';
import Desmos from 'desmos';

function Graph({currentGraph, number}) {
    const desmosContainerRef = useRef(null);
    let latex;
    let latex2;
    if (number === 1) {
        switch (currentGraph) {
            case 0:
                latex = "y = x^3 + 2.84x^2 - 5.606x - 14.766";
                break;
            case 1:
                latex = "y = x^5 - 8*x^2 - 4";
                break;
            case 2:
                latex = "y = 2^x - cos(x) - 3";
                break;
            default:
                console.log(currentGraph);
        }
    } else if (number === 2) {
        switch (currentGraph) {
            case 6:
                latex = "x^2 + y^2 - 4 = 0";
                latex2 = "y - 3x^2 = 0";
                break;
            case 7:
                latex = "x^2 + cos(y) = 4";
                latex2 = "cos(y) + x = 2";
                break;
            default:
                console.log(currentGraph);
        }
    }

    useEffect(() => {
        const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
        calculator.setExpression({id: 'graph1', latex: latex});
        if (number === 2) calculator.setExpression({id: 'graph2', latex: latex2});
        return () => {
            calculator.destroy();
        };
    }, [currentGraph, latex]);

    return <div ref={desmosContainerRef} style={{width: '600px', height: '350px'}}/>;
}

export default Graph;
