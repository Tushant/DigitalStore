import { createSelector } from 'reselect';

const selectStores = state => state.store;

const makeSelectStores = () => createSelector(selectStores, storesState => storesState.stores);

export { makeSelectStores };
