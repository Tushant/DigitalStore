/*
 * AppConstants
 * Each action has a corresponding type, which the reducer knows and picks up on.
 * To avoid weird typos between the reducer and the actions, we save them as
 * constants here. We prefix them with 'yourproject/YourComponent' so we avoid
 * reducers accidentally picking up actions they shouldn't.
 *
 * Follow this format:
 * export const YOUR_ACTION_CONSTANT = 'yourproject/YourContainer/YOUR_ACTION_CONSTANT';
 */

export const LOAD_REPOS = 'DigitalStore/App/LOAD_REPOS';
export const LOAD_REPOS_SUCCESS = 'DigitalStore/App/LOAD_REPOS_SUCCESS';
export const LOAD_REPOS_ERROR = 'DigitalStore/App/LOAD_REPOS_ERROR';
export const INITIALIZE = 'DigitalStore/App/INITIALIZE';
export const INITIALIZE_SUCCESS = 'DigitalStore/App/INITIALIZE_SUCCESS';
export const INITIALIZE_ERROR = 'DigitalStore/App/INITIALIZE_ERROR';
export const DEFAULT_LOCALE = 'en';
export const API_BASE = 'http://tushant.pythonanywhere.com/api/v1/';
