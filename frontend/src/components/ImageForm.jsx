import React, { useState } from 'react';
import axios from 'axios';

const FileUploadComponent = () => {
  const [documents, setDocuments] = useState([]);
  const [activeDrag, setActiveDrag] = useState(false);

  const startDrag = (event) => {
    event.preventDefault();
    setActiveDrag(true);
  };

  const leaveDrag = (event) => {
    event.preventDefault();
    setActiveDrag(false);
  };

  const handleFileDropped = (event) => {
    event.preventDefault();
    setActiveDrag(false);
    const files = Array.from(event.dataTransfer.files);
    const validFiles = files.filter(file => file.type === 'image/jpeg' || file.type === 'image/png');
    setDocuments([...documents, ...validFiles]);
  };

  const handleFileChange = (event) => {
    const files = Array.from(event.target.files);
    const validFiles = files.filter(file => file.type === 'image/jpeg' || file.type === 'image/png');
    setDocuments([...documents, ...validFiles]);
  };

  const handleGenerate = () => {
    const formData = new FormData();
    documents.forEach((doc, index) => {
      formData.append('files', doc);
    });

    axios.post('http://localhost:8000/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(response => {
      console.log('Upload successful:', response.data);
    })
    .catch(error => {
      console.error('Upload error:', error);
    });
  };

  return (
    <div className="bg-gray-100 p-8 h-screen">
      <div className="max-w-xl p-6 bg-white shadow-md mx-auto relative rounded-xl">
        <p className="text-lg bold mb-4">Upload Your Documents</p>
        <button className="absolute top-6 right-6">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M6 18L18 6M6 6L18 18" stroke="#2E2F2F" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </button>
        <div>
          <div className="flex items-center justify-center w-full">
            <label
              onDrop={handleFileDropped}
              onDragEnter={startDrag}
              onDragOver={(e) => e.preventDefault()}
              onDragLeave={leaveDrag}
              htmlFor="dropzone-file"
              className={`flex flex-col items-center justify-center w-full h-64 border-gray-900 border-2 border-dashed rounded-lg cursor-pointer 
              ${activeDrag ? 'bg-blue-50 hover:bg-blue-50 border-blue-600' : 'bg-zinc-50 hover:bg-zinc-100 border-gray-300'}`}
            >
              <div className="flex flex-col items-center justify-center pt-5 pb-6 pointer-events-none">
                <svg
                  className={`w-8 h-8 mb-4 text-gray-900 ${activeDrag ? 'text-blue-600' : ''}`}
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 20 16"
                >
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
                  />
                </svg>
                <p className={`pointer-events-none mb-2 text-sm text-gray-900 ${activeDrag ? 'text-blue-600' : ''}`}>
                  <span className="font-semibold">Click to upload</span> or drag and drop
                </p>
              </div>
              <input id="dropzone-file" type="file" className="hidden" accept=".jpg,.jpeg,.png" onChange={handleFileChange} multiple />
            </label>
          </div>
          <div className="flex justify-between mt-2">
            <p className="text-xs text-gray-900">Supported Formats: SVG, PNG, JPG or GIF</p>
            <p className="text-xs text-gray-900">Max size: 25MB</p>
          </div>
        </div>
        <div className={`w-full mt-3 gap-1 flex flex-col ${documents.length ? '' : 'hidden'}`}>
          {documents.map((doc, key) => (
            <div key={key} className="w-full bg-white shadow-sm p-2 rounded-lg border">
              <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" viewBox="0 0 38 38" fill="none">
                <rect width="38" height="38" rx="8" fill="#8331A7" />
                <path
                  d="M10 14V24C10 25.1046 10.8954 26 12 26H26C27.1046 26 28 25.1046 28 24V16C28 14.8954 27.1046 14 26 14H20L18 12H12C10.8954 12 10 12.8954 10 14Z"
                  stroke="white"
                  strokeWidth="1.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </div>
          ))}
        </div>
        <button
          onClick={handleGenerate}
          className="mt-4 bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600"
        >
          Generate
        </button>
      </div>
    </div>
  );
};

export default FileUploadComponent;
