import React, { Component } from 'react';

import {AxiosGet} from "./api_axios";
import MaterialTable from "material-table";
import Update from "./update";


import {Link } from "react-router-dom";

const columns =  [
  {
    title: "Id",
    field: "id",
  },
  {
    title: "SerialNumber",
    field: "serialNumber",
  },
  {
    title: "Metadata",
    field: "metadata",
  },

  {
    title: "",
    field: "metadataUpdate",
    render: row => <div onClick={ () => {
                    console.log(row.metadataUpdate);
                }
            }> 
                <a href={ `/update/${row.metadataUpdate}` }> update</a>
            </div>
  },

  {
    title: "Message",
    field: "message",
  },

  {
    title: "State",
    field: "state",
  },
];

const data = [
  { id: 1, serialNumber: null, metadata: null, metadataUpdate: "update1", message: null, state: null},
  { id: 2, serialNumber: null, metadata: null, metadataUpdate: "update2", message: null, state: null},
  { id: 3, serialNumber: null, metadata: null, metadataUpdate: "update3", message: null , state: null},
];


class App extends Component {

  constructor(props) {
    super(props);
    console.log("props", props);
    this.state = {
      columns: columns,
      data: data,
    };
  } 


   sensors = async () => {
    let sensors= await AxiosGet();
    var data= sensors;

    for(let i=0; i<data.length; i++){
      data[i].message= data[i].heartbeat.message;

      if(data[i].heartbeat.state===0) data[i].state= "Offline";
      else data[i].state= "Alive";

      data[i].metadataUpdate= data[i].id;
    }

    this.setState({ data: data }) 
  }

  async componentDidMount() {
    await this.sensors();
    // this.interval = setInterval(() =>  this.sensors(), 5000);
  }

  render() {
    const {data, columns}= this.state

    return (
    <div>
        <div>
            <MaterialTable title="Sensors" data={data} columns={columns} />
        </div>
    </div>
    );
  }
}

export default App;
