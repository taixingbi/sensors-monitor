const axios = require('axios').default;

export async function AxiosGet(){
    console.log("AxiosGet");
    let url= 'http://0.0.0.0:8090/api/data/';
    console.log(url);

    let response= await axios.get(url);
    console.log("response", response);

    let data= response.data;
    console.log("data", data);

    return data;
}

export function AxiosPost(sensors_id, serialNumber, metadata){
    let url= 'http://0.0.0.0:8090/api/sensorsUpdate/';
    console.log(serialNumber, metadata);
  
    axios.post(url, {
        sensors_id: sensors_id,
        serialNumber: serialNumber,
        metadata: metadata,
    })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
  }

export default 
{
    AxiosGet,
    AxiosPost,
};