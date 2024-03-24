import React,  {useState} from 'react';
import './Button.css';


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
          // Replace this URL with your server-side endpoint for handling file uploads
          const response = await fetch("/upload", {
             method: "POST",
             body: formData
          });
 
          if (response.ok) {
            const data = await response.json(); // This line is new
            console.log(data);
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