import button from "../Button";

function FileButton({setInputValues, fileData}) {
    return (
        <button value={"Upload"} onClick={setInputValues(fileData)}/>
    );
}

export default FileButton;