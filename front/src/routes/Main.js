import '../styles/App.css';
import Title from "../components/Title";
import MainBlock from "../components/MainBlock";

function Main() {
    return (
        <div className="App">
            <header className="App-header">
                <Title/>
            </header>
            <body>
            <div className="graph-container">
                <MainBlock/>
            </div>
            </body>
        </div>
    );
}

export default Main;
