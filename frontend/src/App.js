import React from 'react';
import { Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import Example from './components/stacked';
import FileUploadComponent from './components/ImageForm';


function App() {

  return (
    <div>
      <Routes>
        <Route exact path="/" element={<HomePage />} />
        <Route exact path="/me" element={<FileUploadComponent />} />

      </Routes>
    </div>
  );
}

export default App;