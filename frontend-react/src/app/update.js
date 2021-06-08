import React, { Component } from 'react';
import {AxiosPost} from "./api_axios";
import { useParams } from "react-router-dom";

class Form extends Component {
  constructor(props){
    super(props)
    console.log("props", props);

    this.state= {
      name: "",
    }
    this.handleNameChange= this.handleNameChange.bind(this);
    this.handleSubmit= this.handleSubmit.bind(this);
  }

  componentDidMount() {
    console.log( window.location.pathname.split('/')[2] );
  }


  handleNameChange(event){
    this.setState({
      name: event.target.value
    });
  }

  handleSubmit(event){

    let sensors_id= window.location.pathname.split('/')[2];
    let serialNumber= null;
    let metadata= this.state.name;

    console.log("sensors_id", sensors_id);
    console.log("metadata", metadata);

    AxiosPost(sensors_id, serialNumber, metadata);
    event.preventDefault();
  }

  render() {

    return (
      <div>

        <form onSubmit= {this.handleSubmit} >
          <label>
            metadata
            <input type="text" name="name"  onChange={ this.handleNameChange}/>    
          </label>

          <input type="submit"/>
        </form>

      </div>
    );
  }
}

export default Form;


// class App extends Component {

//   constructor(props) {
//     super(props);
//     console.log("props", props);
  
//   } 

//   async componentDidMount() {
//     let sensors_id= 1;
//     let serialNumber= 111;
//     let metadata= " update something";

//     AxiosPost(sensors_id, serialNumber, metadata)
//   }

//   render() {

//     return (
//       <div>
//           update
//       </div>
//     );
//   }
// }

// export default App;
