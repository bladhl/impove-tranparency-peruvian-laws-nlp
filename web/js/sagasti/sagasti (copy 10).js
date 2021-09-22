import { fetchData } from '../../js/laws.js';

document.addEventListener('DOMContentLoaded', e => {
  fetchData('FSagasti_period.json', 'agricultura')
});
