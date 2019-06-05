import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import '../../bootstrap.css';

class Infobox extends Component {
    constructor(props) {
      super(props);
      this.state = {
        infoboxKey : this.props.infoboxKey,
        infoboxValue: this.props.infoboxValue
      };
    };
    render (){
      return (
        <div><p><div className="infobox_key"><a href={this.state.infoboxKey} target="_blank">{this.state.infoboxKey}</a></div>{this.state.infoboxValue}</p></div>
      );
    }
  }

  export default Infobox;
