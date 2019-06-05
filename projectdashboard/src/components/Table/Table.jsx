import React, { Component } from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';
import {fetchServerData, fetchPropertyData} from '../../APIHelper';
import '../../bootstrap.css';
import { Modal, Button} from 'react-bootstrap';
import Infobox from './Infobox';


class Table extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      data: this.props.data,
      urls: this.props.urlprops.urls,
      parameters: this.props.urlprops.parameters,
      tabledata: [],
      columns: [],
      show: false,
      infobox : '',
    };
    this.convertSparqlJsonToTableFormat = this.convertSparqlJsonToTableFormat.bind(this);
    this.fetchData = this.fetchData.bind(this);
    this.renderCell = this.renderCell.bind(this);
    this.handleShow = this.handleShow.bind(this);
    this.handleHide = this.handleHide.bind(this);

  }

  componentWillReceiveProps(nextProps) {
    this.setState({
      infobox: nextProps.infobox
    });
    const Example = ({ data }) =>
    Object.entries(data).map(([k, v]) => (
      <div key={k}>
        {k}: {v}
      </div>
    ));

  }

  handleShow(cellValue) {
    this.setState({ show: true });
    fetchPropertyData(this.props.urlprops, cellValue).then((data) => {
      this.setState({infobox: data.response})
    });

  }

  handleHide() {
    this.setState({ show: false });
  }





  renderCell(cellInfo) {
    const cellValue = cellInfo.original[cellInfo.column.id];
    return (
      <div>
        {

          cellValue && cellValue.startsWith("https://w3id.org/reproduceme") ?

          this.renderCellLink(cellInfo) : this.renderValue(cellInfo)

        }
      </div>
    );
  }


  renderValue(cellInfo) {
    return (
        <div>{cellInfo.original[cellInfo.column.id]}</div>
        );
  }

  renderCellLink(cellInfo) {
    return (

      <div>
      <a href='#' onClick={this.handleShow.bind(this, cellInfo.original[cellInfo.column.id])}>{cellInfo.original[cellInfo.column.id]}</a>
      {/* <a href='#' onClick={this.toggleModal.bind(this, cellInfo.original[cellInfo.column.id])}>{cellInfo.original[cellInfo.column.id]}</a> */}
      <Modal
          {...this.props}
          show={this.state.show}
          onHide={this.handleHide}
          dialogClassName="infoboxModal"
        >
          <Modal.Header closeButton>
            <Modal.Title id="contained-modal-title-lg">
              Infobox
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
            {
              this.state.infobox &&
              Object.keys(this.state.infobox).map((infoboxKey) => {
                  const infoboxValue = this.state.infobox[infoboxKey];
                  return (
                      <Infobox
                          infoboxKey={infoboxKey}
                          infoboxValue={infoboxValue}
                      />
                  );
              })
            }
          </Modal.Body>
          <Modal.Footer>
            <Button onClick={this.handleHide}>Close</Button>
          </Modal.Footer>
        </Modal>
      </div>
    );
  }

  convertSparqlJsonToTableFormat(sparql_data) {
    var final_data = {}
    var table_data = []
    var column_data = []
    if (sparql_data) {
      const data = sparql_data.response.results.bindings;
      const header_data = sparql_data.response.head.vars
      var bindings = data;
      for(var i in header_data) {

        column_data.push({
          'Header' : header_data[i],
          'accessor': header_data[i],
          'Cell': this.renderCell
        });
      }
      final_data['column_data'] = column_data
      if (bindings.length !== 0) {
        for(var i in bindings) {
          var binding = bindings[i];
          var tabledata = {};
          for(var n in binding) {
            tabledata[n] =binding[n].value;
          }
          table_data.push(tabledata);
        }
        final_data['table_data'] = table_data
        return final_data

      } else {
        final_data['table_data'] = [];
        return final_data
      }
    } else {
        final_data['column_data'] = []
        final_data['table_data'] = [];
        return final_data
    }

  }

  fetchData(state, instance) {
      fetchServerData(this.props.urlprops, this.props.data).then((data) => {
        var final_data = this.convertSparqlJsonToTableFormat(data);
        this.setState({tabledata: final_data['table_data']});
        this.setState({columns: final_data['column_data']});
        this.setState({loading: false});
      });
  }

  render() {
    return (
      <ReactTable
        data={this.state.tabledata}
        columns={this.state.columns}
        loading={this.state.loading}
        onFetchData={this.fetchData.bind(this)}
        filterable
        defaultPageSize={10}
      />
    );
  }
}


export default Table;
