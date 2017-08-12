import React from 'react';
import { createStructuredSelector } from 'reselect';
import { connect } from 'react-redux';
import { compose } from 'redux';

import injectReducer from 'utils/injectReducer';
import injectSaga from 'utils/injectSaga';

import { makeSelectStores } from './selectors';
import { loadStores } from './actions';
import reducer from './reducer';
import saga from './saga';

export function mapDispatchToProps(dispatch) {
  return {
    loadStores: () => dispatch(loadStores())
  };
}

const mapStateToProps = createStructuredSelector({
  stores: makeSelectStores()
});

class Store extends React.PureComponent {
  componentDidMount() {
    this.props.loadStores();
  }
  render() {
    console.log('store', this.props.stores);
    return <section className="store">store here</section>;
  }
}

const withConnect = connect(mapStateToProps, mapDispatchToProps);

const withReducer = injectReducer({ key: 'store', reducer });
const withSaga = injectSaga({ key: 'store', saga });

export default compose(withReducer, withSaga, withConnect)(Store);
