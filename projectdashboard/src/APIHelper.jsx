var helpers = {
  fetchServerData: function(props, input) {
    const { urls, parameters } = props;
    const request = new Request(
      `${urls.base}getServerResponse/${parameters.projectId}/${input}/`,
      {
        credentials: 'same-origin'
      }
    );

    return fetch(request)
    .then(function(response) {
      return response.json()
    })
    .then(function(json) {
      return json
    })
    .catch(function(error) {
      console.log('error', error)
    })
  },
  fetchPropertyData: function(props, input_val) {
    const input = input_val.split("#")[1]
    const { urls, parameters } = props;
    const request = new Request(
      `${urls.base}getPropertyResponse/${input}`,
      {
        credentials: 'same-origin'
      }

    );


    return fetch(request)
    .then(function(response) {
      return response.json()
    })
    .then(function(json) {
      return json
    })
    .catch(function(error) {
      console.log('error', error)
    })
  }
}

module.exports = helpers;
