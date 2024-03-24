import React,  {useState} from 'react';
import './Button.css';
import ReactDOM from 'react-dom/client';
import Notes from './Notes';


function Button() {
    const [selectedFile, setSelectedFile] = useState(null);
    const handleFileChange = (e) => {
       setSelectedFile(e.target.files[0]);
       document.getElementById("fileName").innerHTML = e.target.files[0].name;
    };
 
    const handleUpload = async () => {
       if (!selectedFile) {
          alert("Please first select a file");
          return;
       }
 
       const formData = new FormData();
       formData.append("file", selectedFile);
       
       try {
          const response = await fetch("https://your-upload-endpoint.com/upload", {
             method: "POST",
             body: formData
          });
 
          if (response.ok) {
            const data = await response.json();
            console.log(data);
            ReactDOM.createRoot(document.getElementById('root')).render(
               <React.StrictMode>
                  <Notes text={data}/>
               </React.StrictMode>
            );
          } else {
             alert("Failed to upload the file due to errors");
          }
       } catch (error) {
          console.error("Error while uploading the file:", error);
          alert("Error occurred while uploading the file");
       }
    };
  return (
    <div>
        <div className="B">
            <input type="file" onChange={handleFileChange}/>
            <button onClick={handleUpload} className="uploadButton">Upload</button>
            <p id="fileName">No file chosen</p>
        </div>
    </div>
        
  );
}

export default Button;