import { LOAD_STORES, LOAD_STORES_SUCCESS, LOAD_STORES_FAILURE } from './constants';

const initialState = {
  stores: {},
  loading: false,
  success: false,
  error: false
};

function storeReducer(state = initialState, action) {
  switch (action.type) {
    case LOAD_STORES:
      return { ...state, loading: true, success: false, error: false };
    case LOAD_STORES_SUCCESS:
      console.log('action', action);
      return { ...state, loading: false, success: true, error: false, stores: action.response };
    case LOAD_STORES_FAILURE:
      console.log('failure action', action);
      return { ...state, loading: false, success: false, error: action.error };
    default:
      return state;
  }
}

export default storeReducer;
