/*
 * AppReducer
 *
 * The reducer takes care of our data. Using actions, we can change our
 * application state.
 * To add a new action, add it to the switch statement in the reducer function
 *
 * Example:
 * case YOUR_ACTION_CONSTANT:
 *   return state.set('yourStateVariable', true);
 */

// import { fromJS } from 'immutable';

import {
  LOAD_REPOS_SUCCESS,
  LOAD_REPOS,
  LOAD_REPOS_ERROR,
  INITIALIZE,
  INITIALIZE_SUCCESS,
  INITIALIZE_ERROR
} from './constants';

// The initial state of the App
const initialState = {
  loading: false,
  initialized: false,
  error: false,
  currentUser: false,
  userData: {
    repositories: false
  }
};

function appReducer(state = initialState, action) {
  switch (action.type) {
    case LOAD_REPOS:
      return {
        ...state,
        loading: true,
        error: false,
        userData: { ...userData, repositories: false }
      };
    case INITIALIZE:
      return { ...state, initialized: false };
    case INITIALIZE_SUCCESS:
      return { ...state, initialized: true };
    case INITIALIZE_ERROR:
      return { ...state, error: action.error };
    case LOAD_REPOS_SUCCESS:
      return {
        ...state,
        loading: false,
        currentUser: action.username,
        userData: { ...userData, repositories: false }
      };
    case LOAD_REPOS_ERROR:
      return { ...state, error: action.error, loading: false };
    default:
      return state;
  }
}

export default appReducer;
