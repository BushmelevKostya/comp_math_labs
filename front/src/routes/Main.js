import '../styles/App.css';
import Title from "../components/Title";
import MainBlock from "../components/MainBlock";

function Main() {
    const values = [["f(x) = 3x^3 + x^2 - x + 1", "f(x) = x^4 - 5x^2 + 4", "f(x) = -x^3 - x^2 - x - 1"], ["left_rectangle", "right_rectangle", "middle_rectangle", "trapezoid", "simpson"], ["f(x) = 1 / (1 - x)", "f(x) = 1 / x ** 0.5", "f(x) = ln(x)"]];
    return (
        <div className="App">
            <header className="App-header">
                <Title/>
            </header>
            <body>
            <div className="graph-container">
                <MainBlock values={values} number={1}/>
                <MainBlock values={values} number={2}/>
            </div>
            </body>
        </div>
    );
}

export default Main;
