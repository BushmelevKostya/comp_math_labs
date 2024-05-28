function CheckButtons({ onChange }) {
    const handleButtonClick = (funcType) => {
        onChange(funcType);
    };

    return (
        <div>
            <button onClick={() => handleButtonClick('x^2')}>x^2</button>
            <button onClick={() => handleButtonClick('e^x')}>e^x</button>
        </div>
    );
}

export default CheckButtons;