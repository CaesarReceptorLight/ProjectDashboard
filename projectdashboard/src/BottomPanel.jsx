import React from 'react';
import ReactDOM from 'react-dom';
import { PanelGroup, Panel, Well, Tabs, Tab} from 'react-bootstrap';
import './bootstrap.css';
import Table from './components/Table/Table';


class BottomPanel extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      projectId: props.parameters.projectId,
      datasetIds: props.parameters.datasetIds,
      data: '',
      plot: '',
      loading: true,
      tabledata: [],
      columns: []
    };
  }


  render() {
    return (
      <div>
        <Well key="third_well" bsSize="large">
          <PanelGroup className="first_panel_group">
            <Panel header={<h1>The Plot</h1>} className="left_panel">
              <div><Table data="plot" urlprops={this.props} /></div>
            </Panel>
            <Panel header={<h1>The Characters</h1>} className="right_panel" id="characters_panel">
              {/* <RightSidebar dict={ this.state.characters }/> */}
              <div><Table data="agents" urlprops={this.props} /></div>
            </Panel>
          </PanelGroup>
          <PanelGroup className="second_panel_group">
            <Panel header={<h1>Materials</h1>} >
            <Tabs activeKey={this.state.key} id="controlled-tab-material" mountOnEnter={true}>
              <Tab eventKey={1} title="Vector">
                  <Tab.Content animation={false} className="paneltabcontent">
                    <div><Table data="Vector" urlprops={this.props}/></div>
                  </Tab.Content>
              </Tab>
              <Tab eventKey={2} title="Plasmid">
                  <Tab.Content animation={false} className="paneltabcontent">
                    <div><Table data="Plasmid" urlprops={this.props}/></div>
                  </Tab.Content>
              </Tab>
              <Tab eventKey={3} title="Protein">
                  <Tab.Content animation={false} className="paneltabcontent">
                    <div><Table data="Protein" urlprops={this.props}/></div>
                  </Tab.Content>
              </Tab>
              <Tab eventKey={4} title="Chemical">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="Chemical" urlprops={this.props} /></div>
                </Tab.Content>
              </Tab>
              <Tab eventKey={5} title="Solution">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="Solution" urlprops={this.props}/></div>
                </Tab.Content>
              </Tab>
              <Tab eventKey={6} title="DNA">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="DNA" urlprops={this.props}/></div>
                </Tab.Content>
              </Tab>
              <Tab eventKey={7} title="RNA">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="RNA" urlprops={this.props}/></div>
                </Tab.Content>
              </Tab>
              <Tab eventKey={8} title="Restriction Enzyme">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="RestrictionEnzyme" urlprops={this.props}/></div>
                </Tab.Content>
              </Tab>
              <Tab eventKey={9} title="Fluorescent Protein">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="FluorescentProtein" urlprops={this.props}/></div>
                </Tab.Content>
              </Tab>
              <Tab eventKey={10} title="Oligonucleotide">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="Oligonucleotide" urlprops={this.props}/></div>
                </Tab.Content>
              </Tab>
            </Tabs>
            </Panel>
            <Panel header={<h1>External Resources</h1>} >
              <div><Table data="externalresources" urlprops={this.props}/></div>
            </Panel>
            <Panel header={<h1>Files Used</h1>} >
              <div><Table data="filesusedinstep" urlprops={this.props}/></div>
            </Panel>
	          <Panel header={<h1>Jupyter Notebooks</h1>} >
              <div><Table data="scriptusedinexperiment" urlprops={this.props}/></div>
            </Panel>

            <Panel header={<h1>Steps/Activities</h1>} >
              <div><Table data="steps" urlprops={this.props}/></div>
            </Panel>

          </PanelGroup>
          <PanelGroup className="third_panel_group">
            <Panel header={<h1>Devices</h1>} >
             <Tabs activeKey={this.state.key} id="controlled-tab-devices" mountOnEnter={true}>
                <Tab eventKey={1} title="LightSource">
                    <Tab.Content animation={false} className="paneltabcontent">
                      <div><Table data="LightSource" urlprops={this.props}/></div>
                    </Tab.Content>
                </Tab>
                <Tab eventKey={2} title="Lasers">
                    <Tab.Content animation={false} className="paneltabcontent">
                      <div><Table data="Laser" urlprops={this.props}/></div>
                    </Tab.Content>
                </Tab>
                <Tab eventKey={3} title="Filaments">
                    <Tab.Content animation={false} className="paneltabcontent">
                      <div><Table data="Filament" urlprops={this.props}/></div>
                    </Tab.Content>
                </Tab>
                <Tab eventKey={4} title="Detector">
                  <Tab.Content animation={false} className="paneltabcontent">
                    <div><Table data="Detector" urlprops={this.props} /></div>
                  </Tab.Content>
                </Tab>
                <Tab eventKey={5} title="Objective">
                  <Tab.Content animation={false} className="paneltabcontent">
                    <div><Table data="Objective" urlprops={this.props}/></div>
                  </Tab.Content>
                </Tab>
                <Tab eventKey={6} title="Filters">
                  <Tab.Content animation={false} className="paneltabcontent">
                    <div><Table data="Filter" urlprops={this.props}/></div>
                  </Tab.Content>
                </Tab>
                <Tab eventKey={7} title="Dichroic">
                  <Tab.Content animation={false} className="paneltabcontent">
                    <div><Table data="Dichroic" urlprops={this.props}/></div>
                  </Tab.Content>
                </Tab>
              </Tabs>
            </Panel>
            <Panel header={<h1>Settings</h1>} >
            <Tabs activeKey={this.state.key} id="controlled-tab-settings" mountOnEnter={true}>
              <Tab eventKey={1} title="LightSource">
                  <Tab.Content animation={false} className="paneltabcontent">
                    <div><Table data="LightSettings" urlprops={this.props}/></div>
                  </Tab.Content>
                </Tab>
              <Tab eventKey={2} title="Detector">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="DetectorSetting" urlprops={this.props} /></div>
                </Tab.Content>
              </Tab>
              <Tab eventKey={3} title="Objective">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="ObjectiveSettings" urlprops={this.props}/></div>
                </Tab.Content>
              </Tab>
              <Tab eventKey={4} title="Filters">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="FilterSetting" urlprops={this.props}/></div>
                </Tab.Content>
              </Tab>
              <Tab eventKey={5} title="General">
                <Tab.Content animation={false} className="paneltabcontent">
                  <div><Table data="generalsettings" urlprops={this.props}/></div>
                </Tab.Content>
              </Tab>
            </Tabs>
            </Panel>
        </PanelGroup>
        </Well>
      </div>

    );
  }
}
export default BottomPanel;
