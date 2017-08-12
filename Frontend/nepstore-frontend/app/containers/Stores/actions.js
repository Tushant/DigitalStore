import { LOAD_STORES, LOAD_STORES_SUCCESS, LOAD_STORES_FAILURE } from './constants';

export function loadStores() {
  return {
    type: LOAD_STORES
  };
}

export function storesLoaded(response) {
  return {
    type: LOAD_STORES_SUCCESS,
    response
  };
}

export function storesLoadingFailure(error) {
  return {
    type: LOAD_STORES_FAILURE,
    error
  };
}
