import React, {Component}from 'react'
import axios from 'axios'
import styled from 'styled-components'

const state = { 
  selectedFile: null
}; 
     
const onFileChange = event => { 
  this.setState({ selectedFile: event.target.files[0] }); 
}; 

const onFileUpload = () => { 
  const formData = new FormData(); 
    formData.append( 
      "myFile", 
      this.state.selectedFile, 
      this.state.selectedFile.name 
    ); 
         
  console.log(this.state.selectedFile); 
      
  axios.post("api/uploadfile", formData); 
}; 
     
const fileData = () => { 
  if (this.state.selectedFile) {           
    return ( 
      <div> 
        <h2>File Details:</h2> 
        <p>File Name: {this.state.selectedFile.name}</p> 
        <p>File Type: {this.state.selectedFile.type}</p> 
        <p> 
          Last Modified:{" "} 
          {this.state.selectedFile.lastModifiedDate.toDateString()} 
        </p> 
      </div> 
    ); 
  } else { 
    return ( 
      <div> 
        <br /> 
        <h4>Choose before Pressing the Upload button</h4> 
      </div> 
    ); 
  } 
}; 

 const App = () => (
   <AppContainer>
     <Intro>
      <h1> 
        Análise de Sentimentos
      </h1> 
      <h4> 
        Faça o Upload do seu arquivo JSON
      </h4> 
      <div> 
        <input type="file" onChange={() => onFileChange()} /> 
        <button onClick={() => onFileUpload()}> 
          Upload! 
        </button> 
      </div> 
     </Intro>
   </AppContainer>
 )

 export default App

 const AppContainer = styled.div`
   display: flex;
   justify-content: center;
   align-items: center;

   height: 100vh;
   background: #1d1f27;
 `

 const Intro = styled.h1`
   font-size: 2.5vw;
   color: #ffff;
 `