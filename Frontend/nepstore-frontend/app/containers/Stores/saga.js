import { call, put, select, takeLatest } from 'redux-saga/effects';
import { LOAD_STORES } from './constants';
import { storesLoaded, storesLoadingFailure } from './actions';

import request from 'utils/request';
import { DigitalStore } from 'containers/App/saga';

export function* loadStores() {
  // Select username from store
  yield call(DigitalStore.get(`store`, storesLoaded, storesLoadingFailure));
  // const requestURL = `http://tushant.pythonanywhere.com/api/v1/store`;
  //
  // try {
  //   // Call our request helper (see 'utils/request')
  //   const stores = yield call(request, requestURL);
  //   yield put(storesLoaded(response));
  // } catch (err) {
  //   yield put(storesLoadingFailure(err));
  // }
}

/**
 * Root saga manages watcher lifecycle
 */
export default function* storesWatcher() {
  // Watches for LOAD_STORES actions and calls loadStores when one comes in.
  // By using `takeLatest` only the result of the latest API call is applied.
  // It returns task descriptor (just like fork) so we can continue execution
  // It will be cancelled automatically on component unmount
  yield takeLatest(LOAD_STORES, loadStores);
}
