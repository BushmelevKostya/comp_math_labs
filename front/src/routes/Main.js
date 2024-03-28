import '../styles/App.css';
import Title from "../components/Title";
import MainBlock from "../components/MainBlock";

function Main() {
    const values = [["f(x) = x^3 + 2.84x^2-5.606x-14.766", "f(x) = x^5 - 8*x^2 - 4", "2^x - cos(x) - 3"], ["bisection", "secant", "simple iteration"], ["f(x, y) = x^2 + y^2 -4, g(x, y) = y - 3 * x^2", "f(x, y) = 6 * y + x ** 2 - 18 , g(x, y) = 2 * x ** 2 + 0.5 * y ** 2 - 8"]];
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
