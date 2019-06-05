import React from 'react';
import ReactDOM from 'react-dom';
import BottomPanel from './BottomPanel';
import './bootstrap.css';
import { Label} from 'react-bootstrap';


class BasicDiv extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isToggleOn: true,
      projectId: props.parameters.projectId,
      datasetIds: props.parameters.datasetIds
    };
  }

  render() {
    return (
      <div>
        { this.state.projectId != '-1' ? (
        	<div>
        		<BottomPanel urls={ globalURLs } parameters={ parameters }/>
        	</div>
        ) : (
            <h1><Label>No Data Available</Label></h1>
        )}
      </div>
    );
  }
}

ReactDOM.render(<BasicDiv urls={ globalURLs } parameters={ parameters } />, document.getElementById('project_dashboard'));
